from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # 오타 수정: JMT -> JWT, SECTET -> SECRET
    JWT_SECRET_KEY: str
    OPENAI_API_KEY: str

    model_config = SettingsConfigDict(
        env_file=".env"
    )

# .env 파일을 읽어서 환경변수 값을 객체로 생성
settings = Settings()