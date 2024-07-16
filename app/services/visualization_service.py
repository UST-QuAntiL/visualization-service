from qiskit import qasm3, QuantumCircuit
from qiskit.visualization import plot_distribution
from matplotlib import pyplot as plt
import matplotlib as mpl
import io
import base64
import numpy as np


from app.helperfunctions import figure_to_base64
from app.model.visualization_request import (
    CircuitVisualizationRequest,
    OptimizationLandscapeVisualizationRequest,
    ExecutionResultVisualizationRequest,
    ObjectiveVisualizationRequest,
)
from app.services.objective_visualization import MaxCutVisualization, TspVisualization


def visualize_circuit(request: CircuitVisualizationRequest):
    circuits = []
    for c in request.circuit:
        if request.circuit_format == "openqasm3":
            loaded_circ = qasm3.loads(c)
            circuits.append(loaded_circ)
        elif request.circuit_format == "openqasm3":
            circuits.append(QuantumCircuit.from_qasm_str(c))
        else:
            return "Currently only openqasm2 and openqasm3 are supported"

    # TODO visualization
    return None


def visualize_optimization_landscape(request: OptimizationLandscapeVisualizationRequest):
    optimization_path = request.optimization_path
    print(optimization_path);
    xs, ys, vals = np.array([]), np.array([]), np.array([])
    for k in range(len(optimization_path)):
        xs = np.append(xs, optimization_path[k]["params"][0])
        ys = np.append(ys, optimization_path[k]["params"][1])
        vals = np.append(vals, optimization_path[k]["obj_value"])

    # determine radii for each data point, progressively decreasing from 1/30 of the x-axis width to 1/150
    radius_start = (np.max(xs) - np.min(xs)) / 30
    radius_end = radius_start / 5
    radii = np.linspace(radius_start, radius_end, len(vals))

    # prepare color map, coloring the data points according to their values
    cmap = mpl.colormaps["viridis"]
    norm = mpl.colors.Normalize(vmin=np.min(vals), vmax=np.max(vals))

    # prepare and arrange figure/axes
    fig = plt.figure(figsize=tuple(np.array([2, 1]) * 5))
    gs = fig.add_gridspec(2, 2, height_ratios=[12, 1], wspace=0.25, hspace=0.3)
    ax_path = fig.add_subplot(gs[0, 0])
    ax_progress = fig.add_subplot(gs[0, 1])
    ax_cbar = fig.add_subplot(gs[1, 0])

    # plot optimization path
    # -simple version
    # ax_path.plot(xs, ys, zorder=-1, color="black") # simple black line plot

    # -better version with arrows
    # 1) prepare vectors starting at the last point and ending just where the circle of the next point begins (considering its radius)
    vectors = []
    for x_pre, x_suc, y_pre, y_suc, radius in zip(xs[1:], xs[:-1], ys[1:], ys[:-1], radii[1:]):
        vector = np.array([x_pre - x_suc, y_pre - y_suc])
        vlen = np.sqrt(vector[0] ** 2 + vector[1] ** 2)
        vectors.append(vector * (1 - radius / vlen))
    vectors = np.array(vectors)

    # 2) plot the arrows
    ax_path.quiver(xs[:-1], ys[:-1], vectors[:, 0], vectors[:, 1], scale_units='xy', angles='xy', scale=1, headlength=4,
                   headaxislength=4, color='lightgrey')

    # plot the data points as circles
    for i, (val, radius) in enumerate(zip(vals, radii)):
        circle = plt.Circle((xs[i], ys[i]), radius, alpha=1, color=cmap(norm(val)))
        ax_path.add_patch(circle)

    ax_path.set_title("Optimization Path")
    ax_path.set_xlabel("Parameter 1")
    ax_path.set_ylabel("Parameter 2")

    # add the color bar
    fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap),
                 cax=ax_cbar, orientation='horizontal', label='Objective Value')

    # plot the optimization progress
    ax_progress.plot(vals)
    ax_progress.set_xlabel("Iteration")
    ax_progress.set_ylabel("Objective Value")
    ax_progress.set_title("Optimization Progress")

    # plt.show()

    figure_base64 = figure_to_base64(fig)
    plt.close(fig)
    return figure_base64


def visualize_execution_results(request: ExecutionResultVisualizationRequest):
    count_list = request.counts
    if isinstance(count_list, dict):
        count_list = [count_list]

    # Generate visualization of probablity distributions
    plots = []
    for counts in count_list:
        max_number_of_plotted_values = request.max_number_of_plotted_values
        if len(counts.keys()) > max_number_of_plotted_values:
            unused_counts = dict(
                sorted(counts.items(), key=lambda x: x[1], reverse=True)[max_number_of_plotted_values:len(counts.keys())])
            total_frequency_of_unused = sum(unused_counts.values())
            counts = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True)[0:max_number_of_plotted_values])
            counts['combinedLowProbabilities'] = total_frequency_of_unused
        plots.append(figure_to_base64(plot_distribution(counts, sort='value_desc')))

    return plots


def visualize_objective(request: ObjectiveVisualizationRequest):
    costs = request.evaluated_cost_overview
    problem_instance = request.problem_instance

    match request.problem_class:
        case "max-cut" | "maxcut" | "maximumcut":
            return MaxCutVisualization().visualize(counts=costs, problem_instance=problem_instance)
        case "tsp":
            return TspVisualization().visualize(counts=costs, problem_instance=problem_instance)
    return None
