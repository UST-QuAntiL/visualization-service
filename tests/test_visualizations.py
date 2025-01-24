import unittest
import os, sys
import json
import re

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
from app import create_app


class FlaskClientTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        self.app_context.pop()

    def test_circuit_visualization(self):
        response = self.client.post(
            "/visualize/circuit",
            data=json.dumps(
                {
                    "circuit": [
                        "OPENQASM 3;\ninclude 'stdgates.inc';\ninput float[64] beta0;\ninput float[64] gamma0;\nbit[4] c;\nqubit[4] q;\nry(pi/3) q[0];\nry(pi/3) q[1];\nry(2*pi/3) q[2];\nry(2*pi/3) q[3];\nbarrier q[0], q[1], q[2], q[3];\ncx q[1], q[0];\nrz(gamma0) q[0];\ncx q[1], q[0];\ncx q[2], q[0];\nrz(gamma0) q[0];\ncx q[2], q[0];\ncx q[2], q[1];\nrz(gamma0) q[1];\ncx q[2], q[1];\ncx q[3], q[0];\nrz(gamma0) q[0];\ncx q[3], q[0];\ncx q[3], q[1];\nrz(gamma0) q[1];\ncx q[3], q[1];\ncx q[3], q[2];\nrz(gamma0) q[2];\ncx q[3], q[2];\nbarrier q[0], q[1], q[2], q[3];\nry(pi/3) q[0];\nrz(beta0) q[0];\nry(-pi/3) q[0];\nry(pi/3) q[1];\nrz(beta0) q[1];\nry(-pi/3) q[1];\nry(2*pi/3) q[2];\nrz(beta0) q[2];\nry(-2*pi/3) q[2];\nry(2*pi/3) q[3];\nrz(beta0) q[3];\nry(-2*pi/3) q[3];\nbarrier q[0], q[1], q[2], q[3];\nc[3] = measure q[0];\nc[2] = measure q[1];\nc[1] = measure q[2];\nc[0] = measure q[3];\n"
                    ],
                    "circuit_format": "openqasm3",
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        print(response.get_json())

    def test_optimization_visualization(self):
        response = self.client.post(
            "/visualize/optimizationLandscape",
            data=json.dumps(
                {
                    "optimization_path": [
                        {"obj_value": -13.245290375, "params": [1, 1]},
                        {"obj_value": -9.995985500000002, "params": [2, 1]},
                        {"obj_value": -13.258442125000002, "params": [1, 2]},
                        {
                            "obj_value": -12.72029275,
                            "params": [0.000008191262308554492, 2.0040475248634735],
                        },
                        {
                            "obj_value": -11.6112665,
                            "params": [1.4998507844978033, 2.012214468344166],
                        },
                        {
                            "obj_value": -13.689691999999997,
                            "params": [0.7500019906190336, 2.0009976500158997],
                        },
                        {
                            "obj_value": -14.09261225,
                            "params": [0.5000092566916325, 2.0029036887100613],
                        },
                        {
                            "obj_value": -13.930265500000003,
                            "params": [0.25009216512997734, 2.009341649983883],
                        },
                        {
                            "obj_value": -14.424431,
                            "params": [0.5009622760387135, 2.127900055673762],
                        },
                        {
                            "obj_value": -14.52090975,
                            "params": [0.3728513666163408, 2.3425802710802417],
                        },
                        {
                            "obj_value": -15.142845249999999,
                            "params": [0.5757426902796926, 2.4886457043015655],
                        },
                        {
                            "obj_value": -15.000321375,
                            "params": [0.7680111766582451, 2.6484356575079557],
                        },
                        {
                            "obj_value": -14.761449375000003,
                            "params": [0.6718769334689689, 2.5685406809047606],
                        },
                        {
                            "obj_value": -15.404793249999999,
                            "params": [0.535795201978095, 2.5367128258962035],
                        },
                        {
                            "obj_value": -14.835603999999998,
                            "params": [0.41462321546601905, 2.56741054054595],
                        },
                        {
                            "obj_value": -14.872176750000001,
                            "params": [0.569849877942577, 2.5891201635976566],
                        },
                        {
                            "obj_value": -14.758917749999998,
                            "params": [0.5059819200938052, 2.5273463578698943],
                        },
                        {
                            "obj_value": -14.783415000000003,
                            "params": [0.546981594148327, 2.5258038729118986],
                        },
                        {
                            "obj_value": -14.786664750000002,
                            "params": [0.5365381045953941, 2.552320154966266],
                        },
                        {
                            "obj_value": -14.8319475,
                            "params": [0.5285227978838499, 2.5338584792213923],
                        },
                        {
                            "obj_value": -14.879217624999999,
                            "params": [0.5372757626521216, 2.5403276189958186],
                        },
                        {
                            "obj_value": -14.750468375,
                            "params": [0.538167829292392, 2.5336096938187773],
                        },
                        {
                            "obj_value": -14.979846,
                            "params": [0.5338467936367544, 2.53657717118372],
                        },
                        {
                            "obj_value": -15.045762750000003,
                            "params": [0.5364759685473834, 2.536012660776717],
                        },
                        {
                            "obj_value": -14.617321,
                            "params": [0.5360335150426044, 2.537659864015653],
                        },
                        {
                            "obj_value": -14.446960625,
                            "params": [0.5353594195605238, 2.5364925708993535],
                        },
                        {
                            "obj_value": -14.819046000000002,
                            "params": [0.5359393635874721, 2.536909859079087],
                        },
                        {
                            "obj_value": -14.577694499999998,
                            "params": [0.5359486162896689, 2.5365229082988625],
                        },
                        {
                            "obj_value": -14.641329,
                            "params": [0.5356957708428173, 2.5367234771560994],
                        },
                        {
                            "obj_value": -14.75246825,
                            "params": [0.5357898763481472, 2.5366631103285644],
                        },
                    ]
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        print(response.get_json())

    def test_execution_result_visualization(self):
        response = self.client.post(
            "/visualize/executionResults",
            data=json.dumps(
                {
                    "counts": {
                        "100000": 30,
                        "100001": 10,
                        "110000": 50,
                        "011110": 20,
                        "010110": 40,
                    }
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        print(response.get_json())

    def test_objective_maxcut_visualization(self):
        response = self.client.post(
            "/visualize/objective",
            data=json.dumps(
                {
                    "costs": [
                        {
                            "cost": -17,
                            "num_occurrences": 484.81525000000005,
                            "bitstring": "1100",
                        },
                        {
                            "cost": -13,
                            "num_occurrences": 87.94637499999999,
                            "bitstring": "0110",
                        },
                        {
                            "cost": -13,
                            "num_occurrences": 81.42075000000001,
                            "bitstring": "1001",
                        },
                        {"cost": -16, "num_occurrences": 80.969, "bitstring": "0101"},
                        {
                            "cost": -16,
                            "num_occurrences": 71.53025000000001,
                            "bitstring": "1010",
                        },
                        {
                            "cost": -10,
                            "num_occurrences": 51.26362500000002,
                            "bitstring": "1101",
                        },
                        {"cost": -11, "num_occurrences": 33.39325, "bitstring": "0100"},
                        {
                            "cost": -13,
                            "num_occurrences": 33.325500000000034,
                            "bitstring": "1110",
                        },
                        {"cost": -12, "num_occurrences": 30.04375, "bitstring": "1000"},
                        {
                            "cost": 0,
                            "num_occurrences": 16.980500000000003,
                            "bitstring": "0000",
                        },
                        {
                            "cost": -17,
                            "num_occurrences": 9.10774999999999,
                            "bitstring": "0011",
                        },
                        {
                            "cost": -11,
                            "num_occurrences": 7.790250000000017,
                            "bitstring": "1011",
                        },
                        {
                            "cost": 0,
                            "num_occurrences": 6.1002500000000115,
                            "bitstring": "1111",
                        },
                        {
                            "cost": -10,
                            "num_occurrences": 5.671249999999998,
                            "bitstring": "0010",
                        },
                        {
                            "cost": -13,
                            "num_occurrences": 3.0732500000000034,
                            "bitstring": "0001",
                        },
                        {"cost": -12, "num_occurrences": -3.431, "bitstring": "0111"},
                    ],
                    "problem_class": "maxcut",
                    "problem_instance": [
                        [0, 3, 3, 6],
                        [3, 0, 4, 4],
                        [3, 4, 0, 3],
                        [6, 4, 3, 0],
                    ],
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        print(response.get_json())
