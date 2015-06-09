# -*- coding: UTF-8 -*-
## Rollbar init code. You"ll need the following to use Rollbar with Flask.
## This requires the "blinker" package to be installed
from flask import Flask, request, got_request_exception
from poi_analyser_lib.settings import *
from poi_analyser_lib.trainer import Trainer
from poi_analyser_lib.predictor import Predictor
from poi_analyser_lib.logger import log
import os
import rollbar
import rollbar.contrib.flask
import json

app = Flask(__name__)

# @app.before_first_request
# def init_rollbar():
#     """init rollbar module"""
#     rollbar.init(
#         # access token for the demo app: https://rollbar.com/demo
#         ROLLBAR_TOKEN,
#         # environment name
#         "production",
#         # server root directory, makes tracebacks prettier
#         root=os.path.dirname(os.path.realpath(__file__)),
#         # flask already sets up logging
#         allow_logging_basic_config=False)
#
#     # send exceptions from `app` to rollbar, using flask"s signal system.
#     got_request_exception.connect(rollbar.contrib.flask.report_exception, app)

@app.route("/trainingSpecificPOI/", methods=["POST"])
def trainingPOI():
    train_tag = "[Training Process] "
    result = {"code": 1, "message": ""}

    try:
        # Analyse the incoming data.
        data = json.loads(request.data)
        print "Received data is", data
    except ValueError, err_msg:

        log.error(train_tag + " ValueError: %s, params=%s" % (err_msg, request.data))

        result["message"] = "Unvalid params: NOT a JSON Object"
        return json.dumps(result)

    log.info(train_tag + "Received request data")

    try:
        _obs = data["obs"]
        _model = data["model"]
    except KeyError, key:

        log.error(train_tag + " KeyError: There is no key named %s, params=%s" % (key, request.data))

        result["message"] = "Unvalid params: There is NO key named %s" % key
        return json.dumps(result)

    log.debug(train_tag + "Received observation is: %s and model is: %s" % (_obs, _model))

    t = Trainer(_model)
    t.fit(_obs)

    log.info(train_tag + "Fitting is complete")
    log.debug(train_tag + "Fitting model is: %s" % t.modelParams())

    result["code"]    = 0
    result["result"]  = t.modelParams()
    result["message"] = "Training successfully"

    return json.dumps(result)

@app.route("/predictPoi/", methods=["POST"])
def predictPOI():
    predict_tag = "[Predicting Process] "
    result = {"code": 1, "message": ""}

    try:
        # Analyse the incoming data.
        data = json.loads(request.data)
        print "Received data is", data
    except ValueError, err_msg:

        log.error(predict_tag + " ValueError: %s, params=%s" % (err_msg, request.data))

        result["message"] = "Unvalid params: NOT a JSON Object"
        return json.dumps(result)

    log.info(predict_tag + "Received request data")

    try:
        _t = data["seq"]
        _models = data["models"]
    except KeyError, key:

        log.error(predict_tag + " KeyError: There is no key named %s, params=%s" % (key, request.data))

        result["message"] = "Unvalid params: There is NO key named %s" % key
        return json.dumps(result)

    log.debug(predict_tag + "Received sequence is: %s and models are: %s" % (_t, _models))

    p = Predictor(_models)
    scores = p.scores(_t)

    log.info(predict_tag + "Predicting is complete")
    log.debug(predict_tag + "Prediction is: %s" % scores)

    result["code"]    = 0
    result["result"]  = scores
    result["message"] = "Predicting successfully"
    return json.dumps(result)

# @app.route("/", methods=["GET", "POST"])
# def hello():
#     print "in hello"
#     papapa = json.loads("{}")
#     log.info("Im an info message")
#     log.debug("papapa")
#     x = None
#     x[5]
#     return "Hello World!"

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=9010)
