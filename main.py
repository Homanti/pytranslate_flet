import googletrans
from googletrans import Translator
import flet as ft
import os

selected_language = ''
selected_language2 = ''

def main(page: ft.Page):
    page.title = "PyTranslate"

    translator = Translator()

    def SelectedLanguage(e):
        global selected_language
        selected_language_code = dropLanguage.value
        if selected_language_code:
            selected_language = languages.get(selected_language_code)
            Translation(1)

    def SelectedLanguage2(e):
        global selected_language2
        selected_language_code2 = dropLanguage.value
        if selected_language_code2:
            selected_language2 = languages.get(selected_language_code2)
            Translation(1)

    def Translation(e):
        if not lineMessage.value == '':
            if not selected_language == '':
                if not selected_language2 == '':
                    answer = translator.translate(lineMessage.value, src=selected_language2, dest=selected_language)
                    lineTranslate.value = answer.text
                    page.update()
            else:
                lineTranslate.value = ''
                page.update()

    languages = {value.title(): key for key, value in googletrans.LANGUAGES.items()}

    options = [ft.dropdown.Option(text=language) for language in languages.keys()]

    dropLanguage = ft.Dropdown(
        label="Вибрати мову на яку перекладати",
        options=options,
        on_change=SelectedLanguage2,
    )

    dropLanguage2 = ft.Dropdown(
        label="Вибрати мову з якої перекладати",
        options=options,
        on_change=SelectedLanguage,
    )

    def change(e):
        lineTranslatevalue = lineTranslate.value
        lineMessagevalue = lineMessage.value

        lineTranslate.value = lineMessagevalue
        lineMessage.value = lineTranslatevalue

        dropLanguagevalue = dropLanguage.value
        dropLanguage2value = dropLanguage2.value
        
        dropLanguage.value = dropLanguage2value

        dropLanguage2.value = dropLanguagevalue

        page.update()

    lineTranslate = ft.TextField(label="Переклад", max_lines=5, expand=True, read_only=True)
    lineMessage = ft.TextField(label="Введіть ваш текст", on_change=Translation, max_lines=5, expand=True)
    btnChange = ft.IconButton(icon=ft.icons.CHANGE_CIRCLE, on_click=change)


    page.add(ft.Row([
        lineMessage,
        lineTranslate,
    ]), ft.Row([dropLanguage2, dropLanguage, btnChange]))

ft.app(target=main, view=None, port=int(os.getenv("PORT", 8502)))
