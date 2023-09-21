from fastapi import APIRouter, Depends, Query

from core.utils import recommend_activities, validate_season

router = APIRouter()


@router.get("/")
async def get_recommendations(
    country: str = Query(..., title="Country",min_length=2, max_length=50),
    season: str = Depends(validate_season),
) -> dict:
    """
    Get recommendations based on a country and season.

    Args:
    - country (str): The country for which recommendations are to be fetched.
    - season (str): The season in which recommendations are desired.

    Returns:
    dict: a dict with 'country', 'season', and 'recommendations' keys.
    """

    try:
        country = country.lower()
        recommendations = await recommend_activities(country, season)
        return {"country": country, "season": season, "recommendations": recommendations}
    except Exception as e:
        return {"error occurred": str(e)}
