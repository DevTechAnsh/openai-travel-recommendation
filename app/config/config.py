from decouple import config


class Settings:
    def __init__(self):
        self.openai_api_key = config("OPENAI_API_KEY")
        self.debug = config("DEBUG", default=False, cast=bool)


settings = Settings()
