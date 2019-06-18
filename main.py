import logging

import aiocron
from aiogram.utils import executor, exceptions

import config
from bot.handlers import bot, dp
from utils import generate_chat_name

logging.basicConfig(level=logging.INFO)


@aiocron.crontab('0 0 * * *')
async def update_title():
    try:
        await bot.set_chat_title(config.LITREEV_CHAT_ID, generate_chat_name())
    except (exceptions.ChatAdminRequired, exceptions.BotKicked, exceptions.ChatNotFound, exceptions.BadRequest):
        pass


executor.start_polling(dp)
