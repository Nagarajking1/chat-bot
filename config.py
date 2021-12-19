HEROKU = True 

if HEROKU:
    from os import environ
    bot_token = environ["bot_token"]
    ARQ_API_KEY = environ["ARQ_API_KEY"]
    LANGUAGE = environ["LANGUAGE"]


    bot_token = "16901971:AAFqdM_SQE1PB2P1xLr67k"
    ARQ_API_KEY = "GNOZRZ-AVRBJA-RWVIKJ-GZVBXZ-ARQ"
    LANGUAGE = "ta"
    ARQ_API_BASE_URL = "https://thearq.tech"
