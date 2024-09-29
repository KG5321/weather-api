from fastapi import APIRouter, Query, HTTPException
from src.services.weather_service import WeatherService

router = APIRouter()
weather_service = WeatherService()


@router.get("/weather")
async def get_weather(city: str = Query(..., title="City", description="City name", min_length=1)) -> dict:
    try:
        weather_data = await weather_service.get_weather(city)
        return weather_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
