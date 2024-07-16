import marshmallow as ma
from marshmallow import fields, ValidationError


class CircuitField(fields.Field):
    def _deserialize(self, value, attr, data, **kwargs):
        if isinstance(value, str) or isinstance(value, list):
            return value
        else:
            raise ValidationError("Field should be str or list")


class Parameters(fields.Field):
    def _deserialize(self, value, attr, data, **kwargs):
        if isinstance(value, dict) or isinstance(value, list):
            return value
        else:
            raise ValidationError("Field should be dict or list")


class CircuitVisualizationRequest:
    def __init__(self, circuit, circuitFormat):
        self.circuit = circuit
        self.circuitFormat = circuitFormat


class CircuitVisualizationRequestSchema(ma.Schema):
    circuit = CircuitField(required=True)
    circuitFormat = ma.fields.Str(required=True)


class OptimizationLandscapeVisualizationRequest:
    def __init__(self, optimizationHistory):
        self.optimizationHistory = optimizationHistory


class OptimizationLandscapeVisualizationRequestSchema(ma.Schema):
    optimizationHistory = ma.fields.List(
        ma.fields.List(ma.fields.Float()), required=True
    )


class ExecutionResultVisualizationRequest:
    def __init__(
        self,
        counts,
    ):
        self.counts = counts


class ExecutionResultVisualizationRequestSchema(ma.Schema):
    counts = ma.fields.Dict(
        keys=ma.fields.Str(), values=ma.fields.Float(), required=True
    )


class ObjectiveVisualizationRequest:
    def __init__(self, evaluatedCostOverview):
        self.evaluatedCostOverview = evaluatedCostOverview


class ObjectiveVisualizationRequestSchema(ma.Schema):
    objFun_hyperparameters = ma.fields.Dict(keys=ma.fields.Float(), required=True)
