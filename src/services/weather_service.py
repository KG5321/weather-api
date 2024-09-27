import os
import aiohttp
from src.utils.cache_manager import CacheManager
from src.services.s3_service import S3Service
from src.services.dynamodb_service import DynamoDBService

class WeatherService:
    def __init__(self):
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        self.base_url = os.getenv("OPENWEATHER_BASE_URL")
        self.cache = CacheManager()
        self.s3_service = S3Service()
        self.dynamodb_service = DynamoDBService()


    async def get_weather(self, city: str):
        cached_data = await self.cache.check_cache(city)
        if cached_data:
            return cached_data
        weather_data = await self._fetch_weather(city)
        file_name, file_url = await self.s3_service.upload_weather_data(city, weather_data)
        await self.dynamodb_service.log_weather_data(city, file_name, file_url)
        return weather_data


    async def _fetch_weather(self, city: str):
        url = f"{self.base_url}?q={city}&appid={self.api_key}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    raise Exception(f"Failed to fetch weather data for {city}: {response.status}")
