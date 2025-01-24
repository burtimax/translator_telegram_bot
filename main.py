import asyncio
import logging
from aiogram import Bot, Dispatcher
from bot import bot, dp
import handlers

# Настройка логирования
def setup_logging():
    # Создаем форматтер для логов
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Создаем обработчик для записи в файл
    file_handler = logging.FileHandler('bot.log')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    
    # Создаем обработчик для вывода в консоль
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)
    
    # Настраиваем корневой логгер
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

async def main():

    # Настраиваем логирование
    setup_logging()
    
    # Удаляем вебхук перед запуском бота
    await bot.delete_webhook(drop_pending_updates=True)
    
    # Запускаем бота
    try:
        logging.info("Бот запущен")
        await dp.start_polling(bot)
    except Exception as e:
        logging.critical("Критическая ошибка при запуске бота: %s", str(e))
    finally:
        logging.info("Бот остановлен")
        await bot.session.close()

if __name__ == '__main__':
    # Сначала установите библиотеку:
    # pip install reverso-context-api
    asyncio.run(main())
