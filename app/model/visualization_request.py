import marshmallow as ma
from marshmallow import fields, ValidationError


class CircuitField(fields.Field):
    def _deserialize(self, value, attr, data, **kwargs):
        if isinstance(value, str) or isinstance(value, list):
            return value
        else:
            raise ValidationError("Field should be str or list")


class ParametersField(fields.Field):
    def _deserialize(self, value, attr, data, **kwargs):
        if isinstance(value, dict) or isinstance(value, list):
            return value
        else:
            raise ValidationError("Field should be dict or list")


class AnyField(fields.Field):
    def _deserialize(self, value, attr, data, **kwargs):
        return value


class CircuitVisualizationRequest:
    def __init__(self, circuit, circuit_format):
        self.circuit = circuit
        self.circuit_format = circuit_format


class CircuitVisualizationRequestSchema(ma.Schema):
    circuit = CircuitField(required=True)
    circuit_format = ma.fields.Str(required=True)


class OptimizationLandscapeVisualizationRequest:
    def __init__(self, optimization_path):
        self.optimization_path = optimization_path


class OptimizationLandscapeVisualizationRequestSchema(ma.Schema):
    optimization_path = AnyField()


class ExecutionResultVisualizationRequest:
    def __init__(self, counts, max_number_of_plotted_values=2**6):
        self.counts = counts
        self.max_number_of_plotted_values = max_number_of_plotted_values


class ExecutionResultVisualizationRequestSchema(ma.Schema):
    counts = ma.fields.Dict(
        keys=ma.fields.Str(), values=ma.fields.Float(), required=True
    )
    max_number_of_plotted_values = ma.fields.Integer()


class ObjectiveVisualizationRequest:
    def __init__(self, costs, problem_class, problem_instance):
        self.costs = costs
        self.problem_class = problem_class.lower()
        self.problem_instance = problem_instance


class ObjectiveVisualizationRequestSchema(ma.Schema):
    costs = ma.fields.List(ma.fields.Dict(keys=AnyField()), required=True)
    problem_class = ma.fields.String()
    problem_instance = AnyField()
