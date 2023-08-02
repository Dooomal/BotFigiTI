from tinkoff.invest import Client
from config.config import Config, load_config

list_ticker: dict[str, str] = {}
config: Config = load_config()
token = config.tink_key.token

def load_list_ticker(token: str):
    with Client(token=token) as client:
        r = client.instruments.shares()
        for i in range(len(r.instruments)):
            list_ticker[r.instruments[i].ticker] = r.instruments[i].figi
        return list_ticker
