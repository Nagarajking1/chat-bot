HEROKU = True 

if HEROKU:
    from os import environ
    ARQ_API_KEY = environ["ARQ_API_KEY"]
    LANGUAGE = environ["LANGUAGE"]
    ARQ_API_KEY = "GNOZRZ-AVRBJA-RWVIKJ-GZVBXZ-ARQ"
    LANGUAGE = "ta"
    ARQ_API_BASE_URL = "https://thearq.tech"
