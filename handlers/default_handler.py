from aiogram import types, Router, F
from aiogram.filters import Command

router = Router()

@router.message()
async def handle_unknown(message: types.Message):
    """Обработчик для всех остальных типов сообщений"""
    try:
        # Определяем тип сообщения
        message_type = "сообщение"
        if message.photo:
            message_type = "фото"
        elif message.video:
            message_type = "видео"
        elif message.document:
            message_type = "документ"
        elif message.sticker:
            message_type = "стикер"
        elif message.animation:
            message_type = "GIF"


        # await message.reply(
        #     f"🤔 Получено {message_type}, но я не знаю, как его обработать.\n"
        #     f"Я умею работать только с текстовыми и голосовыми сообщениями.\n"
        #     f"Пожалуйста, отправьте текст для перевода."
        # )

        await message.reply(
            f"Я понимаю только голосовые и текстовые сообщения 😔\n\n"
            f"I only understand voice and text messages 😔"
        )
    except Exception as e:
        await message.reply(
            "Извините, произошла ошибка при обработке сообщения.\n\n"
            "Sorry, there was an error processing your message."
        ) 