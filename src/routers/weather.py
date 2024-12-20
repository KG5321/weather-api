from fastapi import APIRouter, Query, HTTPException, Depends
from src.services.weather_service import WeatherService

router = APIRouter()
# weather_service = WeatherService()

def get_weather_service():
    return WeatherService()

#test comment

@router.get("/weather")
async def get_weather(city: str = Query(..., title="City", description="City name", min_length=1),
                      weather_service: WeatherService = Depends(get_weather_service)) -> dict:
    try:
        weather_data = await weather_service.get_weather(city)
        return weather_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
