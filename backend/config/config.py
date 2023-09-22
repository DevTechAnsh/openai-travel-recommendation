import os


class Settings:
    def __init__(self):
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        self.ALLOWED_SEASONS = ["summer", "winter", "rainy", "spring"]


settings = Settings()
