import numpy as np
from sklearn.mixture import GMM

class Predictor(object):
    def __init__(self, models):
        covars  = []
        means   = []
        weights = []
        n_mix       = 0
        n_mixs      = []
        covar_types = []
        sum         = 0

        for model in models:
            sum   += model["count"]
            n_mix += model["nMix"]
            n_mixs.append(n_mix)
            covar_types.append(model["covarianceType"])

        for model in models:
            params = model["params"]["params"]
            for covar in params["covars"]:
                covars.append(covar)
            for mean in params["means"]:
                means.append(mean)
            for weight in params["weights"]:
                weight *= (float(model["count"])/float(sum))
                weights.append(weight)

        self.gmm = GMM(
            n_components=n_mix,
            covariance_type=self.checkCovarianceType(covar_types)
        )
        self.gmm.covars_  = np.array(covars)
        self.gmm.means_   = np.array(means)
        self.gmm.weights_ = np.array(weights)


    def scores(self, t):
        _t = np.array(t)
        if _t.ndim == 1:
            _t = _t.reshape([len(_t), 1])
        probs = self.gmm.score_samples(_t)[1].tolist()
        return self.gmm.score_samples(_t)[1].tolist()

    def checkCovarianceType(self, covariance_type):
        return covariance_type[0]


if __name__ == "__main__":
    _model = [{'nMix': 4, 'covarianceType': 'full', "count": 500,
              'params': {'nMix': 4, 'covarianceType': 'full', 'params': {
                  'covars': [[[1.2221303985456107]], [[0.3086663025400781]], [[1.28502444797073]], [[0.26113702790883486]]],
                  'weights': [0.23603795980927875, 0.2527552282253478, 0.2800574289988682, 0.2311493829665058],
                  'means': [[4.536022877901543], [1.4914085123695209], [3.6895831128524326], [6.571810554595958]]}}},
              {'nMix': 4, 'covarianceType': 'full', "count": 500,
              'params': {'nMix': 4, 'covarianceType': 'full', 'params': {
                  'covars': [[[1.2221303985456107]], [[0.3086663025400781]], [[1.28502444797073]], [[0.26113702790883486]]],
                  'weights': [0.23603795980927875, 0.2527552282253478, 0.2800574289988682, 0.2311493829665058],
                  'means': [[4.536022877901543], [1.4914085123695209], [3.6895831128524326], [6.571810554595958]]}}}]

    t = [3.0]

    p = Predictor(_model)
    print p.scores(t)
