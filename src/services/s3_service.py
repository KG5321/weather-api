import os
import time
import json
from src.utils.boto_session_manager import BotoSessionManager

class S3Service:
    def __init__(self) -> None:
        self.s3_bucket_name = os.getenv("S3_BUCKET_NAME")

    async def upload_weather_data(self, city: str, data: dict):
        timestamp = int(time.time())
        file_name = f"{city}_{timestamp}.json"

        async with (await BotoSessionManager.get_s3_client()) as client:
            await client.put_object(
                Bucket=self.s3_bucket_name,
                Key=file_name,
                Body=json.dumps(data)
            )

        return file_name, f"s3://{self.s3_bucket_name}/{file_name}"