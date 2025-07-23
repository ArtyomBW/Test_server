import os

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile

from bot.functions import save_user_to_db
router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    user={
        'full_name': message.from_user.username,
        'email': f"{message.from_user.id}@gmail.com",
        'phone_number': None,
        'user_id': message.from_user.id,
    }

    await save_user_to_db(**user)

    qr_path = f"media/qr_codes/qrcode.png"
    if os.path.exists(qr_path):
        photo = FSInputFile(qr_path)
        await message.answer_photo(photo, caption=f"Sizning QR Codingiz")
    else:
        await message.answer("QR Code topilmadi :(")


@router.message()
async def echo_handler(message: Message) -> None:

    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")






