from logentries import LogentriesHandler
from exception import EnvVarError
import logging

try:
    from config import LOGENTRIES_TOKEN
except EnvVarError:
    raise
finally:
    log = logging.getLogger('logentries')
    log.setLevel(logging.INFO)
    # Note if you have set up the logentries handler in Django, the following line is not necessary
    log.addHandler(LogentriesHandler(LOGENTRIES_TOKEN))
