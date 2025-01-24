from . import text_handler
from . import voice_handler
from . import default_handler
from . import errors_handler
from bot import dp

# Подключаем все роутеры
dp.include_router(errors_handler.router)  # Обработчик ошибок первым!
dp.include_router(text_handler.router)
dp.include_router(voice_handler.router)
dp.include_router(default_handler.router) 