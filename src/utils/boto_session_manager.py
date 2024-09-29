import os
from typing import Optional
import aioboto3


class BotoSessionManager:
    _session: Optional[aioboto3.Session] = None

    @classmethod
    def get_session(cls) -> aioboto3.Session:
        if cls._session is None:
            cls._session = aioboto3.Session(
                aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                region_name=os.getenv('AWS_REGION')
            )
        return cls._session

    @classmethod
    async def get_client(cls, service_name: str) -> aioboto3.Session.client:
        session = cls.get_session()
        return session.client(service_name)

    @classmethod
    async def get_s3_client(cls) -> aioboto3.Session.client:
        return cls.get_client('s3')

    @classmethod
    async def get_dynamodb_client(cls) -> aioboto3.Session.client:
        return cls.get_client('dynamodb')
