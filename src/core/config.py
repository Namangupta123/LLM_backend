from pydantic import Basesettings, Field

class Settings(Basesettings):
    app_name: str = "LLM backend service"
    debug: bool = Field(default=False, env="DEBUG_MODE")

    openai_api_key: str = Field(..., env="OPENAI_API_KEY")
    anthropic_api_key: str = Field(..., env="ANTHROPIC_API_KEY")

    redis_host: str = Field(default="localhost", env="REDIS_HOST")
    redis_port: int = Field(default=6379, env="REDIS_PORT")
    redis_db: int = Field(default=0, env="REDIS_DB")

    default_model: str = Field(default="gpt-4", env="DEFAULT_MODEL")
    max_tokens: int = Field(default=1024, env="MAX_TOKENS")

    log_level: str = Field(default="INFO", env="LOG_LEVEL")
    jaeger_host: str = Field(default="localhost", env="JAEGER_HOST")
    jaeger_port: int = Field(default=6831, env="JAEGER_PORT")

    class config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings=Settings()