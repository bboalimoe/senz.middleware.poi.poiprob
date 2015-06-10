from unittest import TestCase
from flask_app.app import app
import json

class TestMiddlewarePoi2PoiProb(TestCase):

    def setUp(self):
        super(TestMiddlewarePoi2PoiProb, self).setUp()
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        super(TestMiddlewarePoi2PoiProb, self).tearDown()
        app.config['TESTING'] = False

    def testPredictPoi(self):
        input = {
            "models": [
                {
                    "nMix": 4, "covarianceType": "full", "count": 1000,
                    "params": {
                        "nMix": 4,
                        "covarianceType": "full",
                        "params": {
                            "covars": [[[1.2221303985456107]], [[0.3086663025400781]], [[1.28502444797073]], [[0.26113702790883486]]],
                            "weights": [0.23603795980927875, 0.2527552282253478, 0.2800574289988682, 0.2311493829665058],
                            "means": [[4.536022877901543], [1.4914085123695209], [3.6895831128524326], [6.571810554595958]]
                        }
                    }
                },
                {
                    "nMix": 4, "covarianceType": "full", "count": 500,
                    "params": {
                        "nMix": 4,
                        "covarianceType": "full",
                        "params": {
                            "covars": [[[1.2221303985456107]], [[0.3086663025400781]], [[1.28502444797073]], [[0.26113702790883486]]],
                            "weights": [0.23603795980927875, 0.2527552282253478, 0.2800574289988682, 0.2311493829665058],
                            "means": [[4.536022877901543], [1.4914085123695209], [3.6895831128524326], [6.571810554595958]]
                        }
                    }
                }
            ],
            "seq": [3.9, 1.0, 2.2]
        }
        rv = self.app.post("/predictPoi/", data=json.dumps(input))
        self.assertEqual(200, rv.status_code)
        result = json.loads(rv.data)
        self.assertEqual(0, result['code'])

    def testTrainPoi(self):
        input = {
            "model": {
                "nMix": 4, "covarianceType": "full", "nIter": 50,
                "params": {
                    "nMix": 4,
                    "covarianceType": "full",
                    "params": {
                        "covars": [[[1.2221303985456107]], [[0.3086663025400781]], [[1.28502444797073]], [[0.26113702790883486]]],
                        "weights": [0.23603795980927875, 0.2527552282253478, 0.2800574289988682, 0.2311493829665058],
                        "means": [[4.536022877901543], [1.4914085123695209], [3.6895831128524326], [6.571810554595958]]
                    }
                }
            },
            "obs": [1, 1, 1, 1, 5, 5, 5, 5, 19, 19, 19, 19, 33, 33, 33, 33]
        }
        rv = self.app.post("/trainingSpecificPOI/", data=json.dumps(input))
        self.assertEqual(200, rv.status_code)
        result = json.loads(rv.data)
        self.assertEqual(0, result['code'])