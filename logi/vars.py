# (c) cl_me_logesh

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    API_ID = int(getenv('API_ID' , 17713634))
    API_HASH = str(getenv('API_HASH' , 'a8c943a69022fef3ac66accc7ba8ce6b'))
    BOT_TOKEN = str(getenv('BOT_TOKEN','6595425109:AAEpNTI3wmmZrXbWXw3IDpQxNgVchTucing'))
    SESSION_NAME = str(getenv('SESSION_NAME', 'BQDBDtr4tZUsOnSNc5iNJDccmIq0yAv-XTZb_IB-k8fHcfT6d9m1BUTruInxo2fuH2ULXEa4mPzyJ0hZ8fmUjnej2bn8jerZOrIupI61sXOdbXSz_7goGy7h4EcS4JFtF-sq0oxKH_ci0inVJMwkhsBNMDDQsOMCSrdkVPsbKzaoNyoUX9Yth4cN_grYvApeHc1_Qhr9t6dVsrGYXrRiLiY5DpaJKoyU3yXom5lTYfuhUmIIqV1amwFkmviig4A8dUkZvpIUgR6lF6zrt6-dfGbjk2R4Ny18s_lZiESQfqZHXJtrMwZBoZphGLw9OR7Ng8mSW5RIxgKDXWXcWVORGuaNAAAAAVbzYxwA'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL','-1001865295027'))
    PORT = int(getenv('PORT', 8888))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '157.245.106.32'))
    OWNER_ID = int(getenv('OWNER_ID', '1955509952'))
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME','cl_me_logesh'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
        "http://{}:{}/".format(FQDN, PORT)
    DATABASE_URL = str(getenv('DATABASE_URL','mongodb+srv://logi:logi@logimee.ufrkju8.mongodb.net/databasefs'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', -1001865295027))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split()))
