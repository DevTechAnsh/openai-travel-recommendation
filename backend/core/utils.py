from fastapi import HTTPException

from config.config import settings
from backend.services.openai_client import get_gpt_recommendations


# function to check if the season is valid
def validate_season(season: str):
    if season.lower() not in settings.ALLOWED_SEASONS:
        raise HTTPException(
            status_code=400,
            detail="Invalid season. Allowed seasons are spring, summer, rainy, and winter.",
        )
    return season


async def recommend_activities(country: str, season: str):
    # Get recommendations for activities in a specific country during a specific season.

    # Craft a prompt based on the country and season
    prompt = f"Suggest top three activities to do in {country} during {season}."

    # Call the openai function based on function
    recommendations = get_gpt_recommendations(prompt)
    return recommendations
