from tinkoff.invest import Client


list_ticker: dict[str, str] = {}


def load_list_ticker(token: str):
    with Client(token=token) as client:
        r = client.instruments.shares()
        for i in range(len(r.instruments)):
            list_ticker[r.instruments[i].ticker] = r.instruments[i].figi
        return list_ticker

