__all__ = ["LOGENTRIES_TOKEN", "ROLLBAR_TOKEN"]
import os
from exception import *

# Settings

LOGENTRIES_DEV_TOKEN = "1ecd5d3b-50ef-4901-98e6-90913fccd247"
LOGENTRIES_PROD_TOKEN = "1ecd5d3b-50ef-4901-98e6-90913fccd247"
LOGENTRIES_LOCAL_TOKEN = "1ecd5d3b-50ef-4901-98e6-90913fccd247"

ROLLBAR_DEV_TOKEN = "5880ff452a72481fb3af605801652a63"
ROLLBAR_PROD_TOKEN = "5880ff452a72481fb3af605801652a63"
ROLLBAR_LOCAL_TOKEN = "5880ff452a72481fb3af605801652a63"

# Configuration

try:
    application_env = os.environ["APP_ENV"]
except KeyError, key:
    print "KeyError: There is no env var named %s" % key
    print "The local env will be applied"
    application_env = "local"
    raise EnvVarError()
finally:
    LOGENTRIES_TOKEN = ""
    ROLLBAR_TOKEN = ""

    if application_env == "dev":
        LOGENTRIES_TOKEN = LOGENTRIES_DEV_TOKEN
        ROLLBAR_TOKEN = ROLLBAR_DEV_TOKEN
    elif application_env == "prod":
        LOGENTRIES_TOKEN = LOGENTRIES_PROD_TOKEN
        ROLLBAR_TOKEN = ROLLBAR_PROD_TOKEN
    elif application_env == "local":
        LOGENTRIES_TOKEN = LOGENTRIES_LOCAL_TOKEN
        ROLLBAR_TOKEN = ROLLBAR_LOCAL_TOKEN
# else:
#     raise