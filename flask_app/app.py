# -*- coding: UTF-8 -*-

__author__ = "MeoWoodie"

from flask import Flask, request, url_for, Response, send_file
from poi_analyser_lib.datasets import Dataset
from poi_analyser_lib.trainer import Trainer
import json


app = Flask(__name__)

@app.route("/trainingGMM/", methods=["POST"])
def trainingGMM():
    # Analyse the incoming data.
    data = json.loads(request.data)
    print "Received data is", data

    _obs = data["obs"]
    _model = data["model"]
    _location_type = data["config"]["locationType"]

    t = Trainer(_model)
    t.fit(_obs)

    result = json.dumps({"result": t.modelParams(), "code": 0, "message": "Training successfully"})
    return result

@app.route("/predictPoi/", methods=["POST"])
def classifyGMMHMM():
    if request.method != "POST":
        err_msg = "Your request method is illegal"
        return {"massage": err_msg, "code": 1}
    # Analyse the incoming data.
    data = json.loads(request.data)
    print "Received data is", data
    # The training event
    _seq = data["seq"]
    _models = data["models"]
    _config = data["config"]

    result = classifier.classifyByGMMHMM(_seq, _models, _config)

    result = json.dumps({"result": result, "code": 0, "message": "Classifing successfully"})
    return result


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=9010)
