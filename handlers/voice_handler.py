from aiogram import types, Router, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from pathlib import Path
import requests
import traceback
import sys
from bot import bot
from googletrans import Translator
from config import HF_API_TOKEN, HF_API_URL
from handlers.utils import google_translate_text

router = Router()# или "tiny", "small", "medium", "large"
translator = Translator()

@router.message(F.voice)
async def handle_voice(message: types.Message):
    """Обработчик голосовых сообщений"""
    try:
        # Создаем директорию для временных файлов
        temp_dir = Path("temp_voice")
        temp_dir.mkdir(exist_ok=True)
        
        # Получаем информацию о голосовом сообщении
        voice = message.voice
        file_id = voice.file_id
        
        # Пути к временным файлам
        ogg_path = temp_dir / f"{file_id}.ogg"
        mp3_path = temp_dir / f"{file_id}.mp3"
        
        # Отправляем сообщение о начале обработки
        processing_msg = await message.reply("🎧 Обрабатываю голосовое сообщение...")
        
        try:
            # Скачиваем файл
            file_id = voice.file_id

            # Получаем информацию о файле
            file_info = await bot.get_file(file_id)
            file_path = file_info.file_path

            # Скачиваем файл
            downloaded_file = await bot.download_file(file_path)
            save_path = ogg_path
            
            with open(save_path, "wb") as new_file:
                new_file.write(downloaded_file.read())
            
            audio_file_path = ogg_path

            # Function to send audio to the API
            def transcribe_audio(api_token, api_url, audio_file):
                with open(audio_file, "rb") as f:
                    url = "https://api-inference.huggingface.co/models/openai/whisper-large-v3-turbo"
                    payload = f
                    headers = {
                    'Authorization': f'Bearer {HF_API_TOKEN}',
                    'Content-Type': 'audio/ogg'
                    }

                    response = requests.request("POST", url, headers=headers, data=payload)
                return response.json()

            # Transcribe the audio
            result = transcribe_audio(HF_API_TOKEN, HF_API_URL, audio_file_path)

            # Print the transcription
            if "text" in result:
                print("Transcription:", result["text"])
            else:
                print("Error:", result)
            
            transcribed_text = result["text"]

            result = await google_translate_text(transcribed_text)
            
            # Определяем эмодзи и текст направления перевода
            direction = "🇷🇺 → 🇬🇧" if result[2] == 'en' else "🇬🇧 → 🇷🇺"
            
            # Формируем ответ
            response = (
                f"🎤 Распознанный текст:\n{transcribed_text}\n\n"
                f"🔄 Перевод {direction}:\n<code>{result[0]}</code>"
            )
            
            # Отправляем результат
            await processing_msg.edit_text(
                response
            )
            
        finally:
            # Удаляем временные файлы
            if ogg_path.exists():
                ogg_path.unlink()
            if mp3_path.exists():
                mp3_path.unlink()
        
    except Exception as e:
        # Выводим подробную информацию об ошибке в консоль
        print("\n" + "="*50 + " VOICE PROCESSING ERROR " + "="*50, file=sys.stderr)
        print(f"Error: {str(e)}", file=sys.stderr)
        print("\nTraceback:", file=sys.stderr)
        print(traceback.format_exc(), file=sys.stderr)
        print("="*116 + "\n", file=sys.stderr)
        
        await message.reply(
            "😔 Извините, произошла ошибка при обработке голосового сообщения. "
            "Пожалуйста, попробуйте позже."
        )
