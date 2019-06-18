import random

from aiogram import types
from aiogram.utils import exceptions
from aiogram.utils.markdown import code, bold

from bot import bot, dp
from utils import generate_chat_name

ANSWERS = {
    'message_not_from_admin': 'Ёбаный рот этого казино, блядь. Ты кто такой, сука, чтоб это сделать?',
    'admin_required': 'Дайте права, чтобы я мог автоматически менять название чата, мешки с костями'
}


async def is_admin(message: types.Message):
    member = await bot.get_chat_member(message.chat.id, message.from_user.id)
    return member.is_admin()


def is_group(message: types.Message):
    return 'group' in message.chat.type


@dp.message_handler(commands='set_new_name')
async def new_name_handler(message: types.Message):
    new_name = generate_chat_name()

    if is_group(message) and is_admin(message):
        try:
            await message.chat.set_title(new_name)
        except (exceptions.ChatAdminRequired, exceptions.BadRequest):
            await message.reply(f'{code(new_name)}\n\n{bold(ANSWERS["admin_required"])}')

    elif is_group(message):
        if not random.randint(0, 5):
            return await message.reply(ANSWERS['message_not_from_admin'])
        await message.reply(code(new_name))

    else:
        await message.reply(code(new_name))
