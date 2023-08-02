from dataclasses import dataclass
from environs import Env

@dataclass()
class TgBot:
    token: str

@dataclass()
class TinkKey:
    token: str
    account_id: str

@dataclass()
class Config:
    tg_bot: TgBot
    tink_key: TinkKey

def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN')),
        tink_key=TinkKey(
            token=env('TINKOFF_TOKEN'),
            account_id=env('ACCOUNT_ID')))


