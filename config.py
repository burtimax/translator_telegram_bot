from os import getenv
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

# Загружаем конфигурацию из переменных окружения
TOKEN = getenv("BOT_TOKEN")
SOURCE_LANG = getenv("SOURCE_LANG", "ru")  # ru по умолчанию
TARGET_LANG = getenv("TARGET_LANG", "en")  # en по умолчанию
HF_API_TOKEN = getenv("HF_API_TOKEN") 
HF_API_URL = getenv("HF_API_URL") 

# Проверяем наличие токена
if not TOKEN:
    raise ValueError("Не указан токен бота. Проверьте переменную BOT_TOKEN в файле .env")
