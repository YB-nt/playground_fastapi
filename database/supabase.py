from supabase import create_client, Client

# TODO doppler 사용하게 되면 전환 필요
import os
from dotenv import load_dotenv, find_dotenv


# TODO 싱글턴 사용해서 데이터 베이스 연결 객체 return


load_dotenv(".config/.env")


class ConnSupabase:
    _instance = None
    _supabase = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._supabase = create_client(
                os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY")
            )
        return cls._instance

    @property
    def client(self) -> Client:
        return self._supabase
