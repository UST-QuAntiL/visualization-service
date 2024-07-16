import base64
from io import BytesIO


def visualize_circuit_object(circuit):
    if circuit.depth() < 50:
        try:
            return render_latex(circuit)
        except:
            return render_matplot(circuit)
    else:
        return "Circuit too large to visualize (maximum depth: 50)"


def render_latex(circuit):
    latex_circuit = circuit.draw(output="latex")
    buffered = BytesIO()
    latex_circuit.save(buffered, format="png")
    img_str = base64.b64encode(buffered.getvalue())
    print(img_str)
    return img_str


def render_matplot(circuit):
    latex_circuit = circuit.draw(output="mpl")
    buffered = BytesIO()
    latex_circuit.savefig(buffered, format="png")
    img_str = base64.b64encode(buffered.getvalue())
    print(img_str)
    return img_str
