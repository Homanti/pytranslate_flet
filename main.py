import flet as ft
from func_translator import translate_text, detect_language
import os

selected_language = ''
selected_language_from = ''

def main(page: ft.Page):
    page.title = "PyTranslate"

    def SelectedLanguage(e):
        global selected_language
        selected_language_code = dropLanguage.value
        if selected_language_code:
            selected_language = languages.get(selected_language_code)
            Translation(1)

    def SelectedLanguageFrom(e):
        global selected_language_from
        selected_language_code2 = dropLanguage_from.value
        if selected_language_code2:
            selected_language_from = languages.get(selected_language_code2)
            Translation(1)

    def Translation(e):
        if not lineMessage.value == '':
            if not selected_language == '':
                if not selected_language_from == '':
                    answer = translate_text(lineMessage.value, selected_language, selected_language_from)
                    lineTranslate.value = answer
                    page.update()
        if lineMessage.value == '':
            lineTranslate.value = ''
            page.update()

    langlist = {'auto': 'Визначити мову', 'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic',
                'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali',
                'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa',
                'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian',
                'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian',
                'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian',
                'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa',
                'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian',
                'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese',
                'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean',
                'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian',
                'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay',
                'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian',
                'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto',
                'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian',
                'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi',
                'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese',
                'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai',
                'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek', 'vi': 'vietnamese',
                'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'}

    langlist2 = {'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian',
                 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian',
                 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa',
                 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian',
                 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian',
                 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian',
                 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa',
                 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian',
                 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese',
                 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean',
                 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian',
                 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay',
                 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian',
                 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto',
                 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian',
                 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona',
                 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish',
                 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu',
                 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek',
                 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'}

    languages = {value.title(): key for key, value in langlist.items()}

    languages2 = {value.title(): key for key, value in langlist2.items()}

    options = [ft.dropdown.Option(text=language) for language in languages.keys()]

    options2 = [ft.dropdown.Option(text=language) for language in languages2.keys()]

    def change(e):
        if not lineMessage.value == '':
            global selected_language
            global selected_language_from

            if selected_language_from == 'auto':
                selected_language_value = langlist[detect_language(lineMessage.value)].capitalize()
                selected_language_from_value = langlist[selected_language].capitalize()

            lineTranslatevalue = lineTranslate.value
            lineMessagevalue = lineMessage.value

            lineTranslate.value = lineMessagevalue
            lineMessage.value = lineTranslatevalue

            dropLanguage.value = selected_language_value
            dropLanguage_from.value = selected_language_from_value

            page.update()

    if page.width < 600: # для мобілок
        lineTranslate = ft.TextField(label="Переклад", max_lines=5, read_only=True, min_lines=3)
        lineMessage = ft.TextField(label="Введіть ваш текст", on_change=Translation, max_lines=5, min_lines=3)
        btnChange = ft.IconButton(icon=ft.icons.CHANGE_CIRCLE, on_click=change)

        dropLanguage = ft.Dropdown(
            label="Вибрати мову на яку перекладати",
            options=options2,
            on_change=SelectedLanguage,
            width=400,
        )

        dropLanguage_from = ft.Dropdown(
            label="Вибрати мову з якої перекладати",
            options=options,
            on_change=SelectedLanguageFrom,
            width=400,
        )

        page.add(ft.Column([
            lineMessage,
            lineTranslate,
        ]), ft.Column([dropLanguage_from, btnChange, dropLanguage], alignment=ft.MainAxisAlignment.CENTER))

    else:
        lineTranslate = ft.TextField(label="Переклад", max_lines=5, expand=True, read_only=True, min_lines=3)
        lineMessage = ft.TextField(label="Введіть ваш текст", on_change=Translation, max_lines=5, expand=True, min_lines=3)
        btnChange = ft.IconButton(icon=ft.icons.CHANGE_CIRCLE, on_click=change)

        dropLanguage = ft.Dropdown(
            label="Вибрати мову на яку перекладати",
            options=options2,
            on_change=SelectedLanguage,
            width=400,
        )

        dropLanguage_from = ft.Dropdown(
            label="Вибрати мову з якої перекладати",
            options=options,
            on_change=SelectedLanguageFrom,
            width=400,
        )

        page.add(ft.Row([
            lineMessage,
            lineTranslate,
        ]), ft.Row([dropLanguage_from, btnChange, dropLanguage], alignment=ft.MainAxisAlignment.CENTER))

#ft.app(target=main)
ft.app(target=main, view=None, port=int(os.getenv("PORT", 8502)))
