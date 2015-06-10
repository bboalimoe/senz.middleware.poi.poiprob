from exception import *

def checkCovarianceType(covariance_type):
    if len(covariance_type) < 1:
        raise CovarianceTypeError(None)
    pre_c = covariance_type[0]
    for c_t in covariance_type:
        if c_t not in ["full", "diag", "tied", "spherical"]:
            raise CovarianceTypeError(c_t)
        if pre_c != c_t:
            raise CovarianceTypeError("inconformity")
        pre_c = c_t
    return covariance_type[0]