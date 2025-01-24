from googletrans import Translator, LANGUAGES

translator = Translator()

async def google_translate_text(text: str):
    # Определяем язык входного текста
    detected_lang = await translator.detect(text)
    detected_lang = detected_lang.lang
    
    """
    if detected_lang.lang != 'ru' and detected_lang.lang != 'en':
        await message.reply("Я не знаю, как переводить на этот язык.")
        return
    """
    
    # Выбираем язык для перевода
    target_language = 'en' if detected_lang == 'ru' else 'ru'
    
    # Получаем перевод
    translation = await translator.translate( 
        text.strip().lower(), 
        src=detected_lang,
        dest=target_language
    )
    return (translation.text, detected_lang, target_language)
