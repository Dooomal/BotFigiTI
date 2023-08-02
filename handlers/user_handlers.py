from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message
from library.library import load_list_ticker
from config.config import Config, load_config
# from aiogram import F
# from magic_filter import F

config: Config = load_config()
token_t = config.tink_key.token

router: Router = Router()

@router.message(CommandStart())
async def process_command_start(message: Message):
    await message.answer(
        text="Этот бот возвращает FIGI инструмента используемого в Tinkoff invest API")

list_ticker = load_list_ticker(token=token_t)

@router.message()
async def process_ticker_command(message: Message):
    upper_text = message.text.upper()
    if upper_text in list_ticker.keys():
        await message.answer(text=list_ticker[upper_text])
    else:
        await message.answer(text='Я не знаю такой тикер, меня писал джуниор самоучка')





