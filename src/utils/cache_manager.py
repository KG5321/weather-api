import json
import os
from datetime import datetime, timedelta
from src.utils.boto_session_manager import BotoSessionManager

class CacheManager:
    def __init__(self) -> None:
        self.cache_ttl = 5*60
        self.s3_bucket_name = os.getenv("S3_BUCKET_NAME")

    async def check_cache(self, city: str):
        five_minutes_ago = datetime.now() - timedelta(minutes=5)
        async with (await BotoSessionManager.get_s3_client()) as client:
            result = await client.list_objects_v2(Bucket=self.s3_bucket_name, Prefix=f"{city}_")
            if 'Contents' in result:
                for obj in result['Contents']:
                    obj_time = datetime.fromtimestamp(int(obj['Key'].split('_')[1].split('.')[0]))
                    if obj_time >= five_minutes_ago:
                        response = await client.get_object(Bucket=self.s3_bucket_name, Key=obj['Key'])
                        return json.loads(await response['Body'].read())
        return None