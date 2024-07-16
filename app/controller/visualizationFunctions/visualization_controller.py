from flask_smorest import Blueprint
from flask import request
from app.services import visualization_service
from app.model.objective_response import VisualizationResponseSchema
from app.model.objective_request import (
    CircuitVisualizationRequest,
    CircuitVisualizationRequestSchema,
    OptimizationLandscapeVisualizationRequest,
    OptimizationLandscapeVisualizationRequestSchema,
    ExecutionResultVisualizationRequest,
    ExecutionResultVisualizationRequestSchema,
    ObjectiveVisualizationRequestSchema,
    ObjectiveVisualizationRequest,
)

blp = Blueprint(
    "objective",
    __name__,
    url_prefix="/visualize",
    description="compute visualization for",
)


@blp.route("/circuit", methods=["POST"])
@blp.arguments(
    CircuitVisualizationRequestSchema,
    example=dict(circuit="openqasmbla", circuitFormat="openqasm2"),
)
@blp.response(200, VisualizationResponseSchema)
def visualizeCircuit(json: CircuitVisualizationRequest):
    print(json)
    if json:
        return visualization_service.visualizeCircuit(
            CircuitVisualizationRequest(**json)
        )


@blp.route("/optimizationLandscape", methods=["POST"])
@blp.arguments(
    OptimizationLandscapeVisualizationRequestSchema,
    example={
        "optimizationHistory": [],
    },
)
@blp.response(200, VisualizationResponseSchema)
def visualizeOptimizationLandscape(json: OptimizationLandscapeVisualizationRequest):
    print(json)
    if json:
        return visualization_service.visualizeOptimizationLandscape(
            OptimizationLandscapeVisualizationRequest(**json)
        )


@blp.route("/executionResults", methods=["POST"])
@blp.arguments(
    ExecutionResultVisualizationRequestSchema,
    example={
        "counts": {
            "100001": 10,
            "011110": 20,
            "100000": 30,
            "010110": 40,
            "110000": 50,
        },
    },
)
@blp.response(200, VisualizationResponseSchema)
def visualizeExecutionResults(json: ExecutionResultVisualizationRequest):
    print(json)
    if json:
        return visualization_service.generate_knapsack_objective_response(
            ExecutionResultVisualizationRequest(**json)
        )


@blp.route("/objective", methods=["POST"])
@blp.arguments(
    ObjectiveVisualizationRequestSchema,
    example={},
)
@blp.response(200, VisualizationResponseSchema)
def shor_discrete_log(json: ObjectiveVisualizationRequest):
    print(json)
    if json:
        return visualization_service.generate_shor_discrete_log_objective_response(
            ObjectiveVisualizationRequest(**json)
        )
