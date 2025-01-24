# Telegram Translator Bot 🌐

Многофункциональный Telegram бот для перевода текста и голосовых сообщений между русским и английским языками. Использует Google Translate для текста и Hugging Face Whisper для распознавания речи.

## ✨ Возможности

### Текстовые сообщения
- Автоматическое определение языка (русский/английский)
- Мгновенный перевод с сохранением форматирования
- HTML разметка для удобного копирования текста

### Голосовые сообщения
- Распознавание речи через Hugging Face Whisper API
- Автоматический перевод распознанного текста
- Поддержка различных форматов аудио

## 🛠 Технологии
- Python 3.8+
- aiogram 3.x
- Google Translate API
- Hugging Face Whisper API
- python-dotenv

## ⚙️ Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/burtimax/translator_telegram_bot
cd telegram-translator-bot
```

2. Создайте виртуальное окружение и активируйте его:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/macOS
venv\Scripts\activate     # для Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Создайте файл `.env` и добавьте необходимые переменные окружения:
```env
BOT_TOKEN=your_telegram_bot_token
HUGGINGFACE_API_KEY=your_huggingface_api_key
```

## 🚀 Запуск

1. Убедитесь, что виртуальное окружение активировано
2. Запустите бота:
```bash
python main.py
```

## 💡 Использование

1. Найдите бота в Telegram по его имени
2. Отправьте текстовое сообщение на русском или английском языке
3. Получите мгновенный перевод
4. Для перевода голосового сообщения просто отправьте его боту

## 📝 Лицензия

MIT License. Подробности в файле [LICENSE](LICENSE)

## 👥 Вклад в проект

Мы приветствуем ваш вклад в проект! Пожалуйста:

1. Создайте форк репозитория
2. Создайте ветку для ваших изменений
3. Отправьте пулл-реквест

## ⚠️ Примечание

Для работы с API требуется регистрация на соответствующих сервисах:
- [Telegram Bot API](https://core.telegram.org/bots#creating-a-new-bot)
- [Hugging Face](https://huggingface.co/settings/tokens)

