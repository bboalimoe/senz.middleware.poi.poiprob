__all__ = ["EnvVarError", "FittingError", "ModelParamKeyError", "ModelInitError", "PredictingError", "CovarianceTypeError"]

class PoiMiddlewareError(Exception):
    pass

class EnvVarError(PoiMiddlewareError):
    def __str__(self):
        return "<%s> caused environment variable APP_ENV is not exist" % \
               self.__class__.__name__

class FittingError(PoiMiddlewareError):
    def __init__(self, _x, _model):
        self.X = _x
        self.model = _model

    def __str__(self):
        return "<%s> caused FITTING failed, input X: %s, input Model: %s" % \
               (self.__class__.__name__, self.X, self.model)

class PredictingError(PoiMiddlewareError):
    def __init__(self, _t, _model):
        self.T = _t
        self.model = _model

    def __str__(self):
        return "<%s> caused Predicting failed, input T: %s, input Model: %s" % \
               (self.__class__.__name__, self.T, self.model)

class ModelParamKeyError(PoiMiddlewareError):
    def __init__(self, key):
        self.key = key

    def __str__(self):
        return "<%s> caused KEY error, there is no key named %s" % \
               (self.__class__.__name__, self.key)

class CovarianceTypeError(PoiMiddlewareError):
    def __init__(self, covariance_type):
        self.covarianceType = covariance_type

    def __str__(self):
        if self.covarianceType is None:
            return "<%s> caused COVARIANCE TYPE error, there is no specific covariance type" % \
                   self.__class__.__name__
        elif self.covarianceType == "inconformity":
            return "<%s> caused COVARIANCE TYPE error, inconformity of covariance types in the list occurred" % \
                   self.__class__.__name__
        else:
            return "<%s> caused COVARIANCE TYPE error, there is no covariance type named %s" % \
                   (self.__class__.__name__, self.covarianceType)

class ModelInitError(PoiMiddlewareError):
    def __init__(self, n_component, covariance_type, n_iter):
        self.nComponent = n_component
        self.covarianceType = covariance_type
        self.nIter = n_iter

    def __str__(self):
        return "<%s> caused some errors occurred when gmm init, nComponent: %s, CovarianceType: %s, nIter: %s" % \
               (self.__class__.__name__, self.nComponent, self.covarianceType, self.nIter)
