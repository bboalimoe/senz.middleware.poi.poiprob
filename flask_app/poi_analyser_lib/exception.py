__all__ = ["EnvVarError"]

class PoiMiddlewareError(Exception):
    pass

class EnvVarError(PoiMiddlewareError):
    def __str__(self):
        return "[%s] caused environment variable APP_ENV is not exist" % self.__class__.__name__

# class