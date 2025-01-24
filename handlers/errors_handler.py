from aiogram import Router
from aiogram.types import ErrorEvent
import logging

router = Router()

@router.errors()
async def handle_errors(error: ErrorEvent):
    """Глобальный обработчик ошибок"""
    # Получаем текущий логгер
    logger = logging.getLogger(__name__)
    
    try:
        # Логируем ошибку
        logger.error(
            "Произошла ошибка при обработке запроса: %s", 
            str(error.exception),
            exc_info=True
        )
        
        # Получаем объект апдейта (может быть None)
        update = error.update
        if update is None:
            return
        
        # Пытаемся получить объект message
        message = None
        if hasattr(update, 'message'):
            message = update.message
        elif hasattr(update, 'callback_query'):
            message = update.callback_query.message
            
        if message is None:
            return
            
        # Отправляем сообщение пользователю
        await message.answer(
            "😔 Извините, произошла непредвиденная ошибка.\n"
            "Мы уже работаем над её устранением.\n"
            "Пожалуйста, попробуйте позже."
        )
        
    except Exception as e:
        # Логируем ошибку в обработчике ошибок
        logger.critical(
            "Ошибка в обработчике ошибок: %s",
            str(e),
            exc_info=True
        ) 