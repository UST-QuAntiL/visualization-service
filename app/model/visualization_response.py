import marshmallow as ma
import json


class VisualizationResponse:
    def __init__(self, visualization):
        super().__init__()
        self.visualization = visualization

    def to_json(self):
        json_objective_response = {
            "visualization": self.visualization,
        }
        return json_objective_response


class VisualizationResponseSchema(ma.Schema):
    visualization = ma.fields.String()
