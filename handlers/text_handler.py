from aiogram import types, Router, F
from aiogram.filters import Command
from googletrans import Translator, LANGUAGES
from config import SOURCE_LANG, TARGET_LANG
import traceback
import sys
from handlers.utils import google_translate_text

router = Router()
translator = Translator()

@router.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply(
        "Привет! Я бот-переводчик.\n"
        "Отправьте мне текст на русском или английском языке, "
        "и я переведу его на другой язык."
    )

@router.message(F.text)
async def translate_text(message: types.Message):
    if message.text.startswith('/'):
        return
    
    try:
        result = await google_translate_text(message.text)

        # Определяем эмодзи и текст направления перевода
        direction = "🇷🇺 → 🇬🇧" if result[2] == 'en' else "🇬🇧 → 🇷🇺"
        
        # Формируем ответное сообщение
        response = (
            f"🔄 Перевод {direction}:\n\n"
            f"<code>{result[0]}</code>"
        )
        
        await message.reply(response)
    except ValueError as e:
        if str(e) == 'invalid source language':
            await message.reply(
                "Извините, я не могу перевести этот текст. Попроуйте другой текст."
            )
            return
        raise  # Пробрасываем остальные ValueError дальше
    except Exception as e:
        # Выводим подробную информацию об ошибке в консоль
        print("\n" + "="*50 + " TRANSLATION ERROR " + "="*50, file=sys.stderr)
        print(f"Error: {str(e)}", file=sys.stderr)
        print(f"User text: {message.text}", file=sys.stderr)
        print("\nTraceback:", file=sys.stderr)
        print(traceback.format_exc(), file=sys.stderr)
        print("="*116 + "\n", file=sys.stderr)

        await message.reply(
            "Извините, произошла ошибка при переводе. "
            "Пожалуйста, попробуйте позже."
        ) 