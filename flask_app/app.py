## Rollbar init code. You'll need the following to use Rollbar with Flask.
## This requires the 'blinker' package to be installed
from flask import Flask, request
from flask import got_request_exception
from poi_analyser_lib.trainer import Trainer
from poi_analyser_lib.predictor import Predictor
import os
import rollbar
import rollbar.contrib.flask
import json

app = Flask(__name__)

@app.before_first_request
def init_rollbar():
    """init rollbar module"""
    rollbar.init(
        # access token for the demo app: https://rollbar.com/demo
        '5880ff452a72481fb3af605801652a63',
        # environment name
        'production',
        # server root directory, makes tracebacks prettier
        root=os.path.dirname(os.path.realpath(__file__)),
        # flask already sets up logging
        allow_logging_basic_config=False)

    # send exceptions from `app` to rollbar, using flask's signal system.
    got_request_exception.connect(rollbar.contrib.flask.report_exception, app)

@app.route("/trainingGMM/", methods=["POST"])
def trainingPOI():
    # Analyse the incoming data.
    data = json.loads(request.data)
    print "Received data is", data

    _obs = data["obs"]
    _model = data["model"]
    # _location_type = data["config"]["locationType"]

    t = Trainer(_model)
    t.fit(_obs)

    result = json.dumps({"result": t.modelParams(), "code": 0, "message": "Training successfully"})
    return result

@app.route("/predictPoi/", methods=["POST"])
def predictPOI():
    # Analyse the incoming data.
    data = json.loads(request.data)
    print "Received data is", data
    _t = data["seq"]
    _models = data["models"]

    p = Predictor(_models)
    scores = p.scores(_t)

    result = json.dumps({"result": scores, "code": 0, "message": "Predicting successfully"})
    return result


if __name__ == "__main__":
    # app.debug = True
    app.run(host="0.0.0.0", port=9010)
