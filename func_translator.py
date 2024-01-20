import requests, uuid, json

# Ключ и базовые настройки для работы с API Bing Translator
key = "afdb5430fbad4dabb359e87a3a600cdf"
endpoint = "https://api.cognitive.microsofttranslator.com"
location = "westeurope"

# Функция для определения языка текста
def detect_language(text):
    path = '/detect?api-version=3.0'
    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4()),
    }

    body = [{'text': text}]

    try:
        request = requests.post(constructed_url, headers=headers, json=body)
        response = request.json()

        if response and 'language' in response[0]:
            return response[0]['language']
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def translate_text(text, to_lang, from_lang=None):

    if from_lang == 'auto':
        from_lang = None

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'to': to_lang,
    }
    if from_lang:
        params['from'] = from_lang

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4()),
    }

    body = [{'text': text}]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    return response[0]['translations'][0]['text']