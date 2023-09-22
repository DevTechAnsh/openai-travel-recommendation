from decouple import config


class Settings:
    def __init__(self):
        self.OPENAI_API_KEY = config("OPENAI_API_KEY")
        self.DEBUG = config("DEBUG", default=False, cast=bool)
        self.ALLOWED_SEASONS = ["summer", "winter", "rainy", "spring"]


settings = Settings()
