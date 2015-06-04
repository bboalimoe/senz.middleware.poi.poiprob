# -*- coding: UTF-8 -*-

import numpy as np
__author__ = "MeoWoodie"

from flask import Flask, request, url_for, Response, send_file
from poi_analyser_lib.datasets import Dataset
from poi_analyser_lib.trainer import Trainer
from poi_analyser_lib.predictor import Predictor
import json


app = Flask(__name__)

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
    app.debug = True
    app.run(host="0.0.0.0", port=9010)
