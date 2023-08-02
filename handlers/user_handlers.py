from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message
from library.library import load_list_ticker
from config.config import Config, load_config

config: Config = load_config()
token_t = config.tink_key.token

router: Router = Router()

@router.message(CommandStart())
async def process_command_start(message: Message):
    await message.answer(text="Этот бот возвращает FIGI инструмента используемого в Tinkoff invest API")

list_ticker = load_list_ticker(token=token_t)

@router.message(Text(text=list_ticker.keys()))
async def process_ticker_command(message: Message):
    await message.answer(text=list_ticker[message.text])


