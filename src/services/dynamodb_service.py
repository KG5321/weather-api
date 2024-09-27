import os
import time
from src.utils.boto_session_manager import BotoSessionManager

class DynamoDBService:
    def __init__(self) -> None:
        self.table_name = os.getenv("DYNAMODB_TABLE_NAME")


    async def log_weather_data(self, city: str, file_name: str, file_url: str):
        timestamp = str(int(time.time()))

        async with (await BotoSessionManager.get_dynamodb_client()) as client:
            await client.put_item(
                TableName=self.table_name,
                Item={
                    'city': {'S': city},
                    'timestamp': {'S': timestamp},
                    'file_name': {'S': file_name},
                    'file_url': {'S': file_url}
            }
    )