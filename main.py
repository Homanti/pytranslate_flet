import flet as ft
import googletrans
from googletrans import Translator

selected_language = ''

def main(page: ft.Page):
    page.title = "PyTranslate"

    translator = Translator()

    def SelectedLanguage(e):
        global selected_language
        selected_language_code = dropLanguage.value
        if selected_language_code:
            selected_language = languages.get(selected_language_code)
            Translation2()

    def Translation(e):
        if not lineMessage.value == '':
            if not selected_language == '':
                answer = translator.translate(lineMessage.value, dest=selected_language)
                lineTranslate.value = answer.text
                page.update()
            else:
                lineTranslate.value = ''
                page.update()

    def Translation2():
        if not lineMessage.value == '':
            if not selected_language == '':
                answer = translator.translate(lineMessage.value, dest=selected_language)
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
        on_change=SelectedLanguage,
    )

    def change(e):
        lineTranslatevalue = lineTranslate.value
        lineMessagevalue = lineMessage.value

        lineTranslate.value = lineMessagevalue
        lineMessage.value = lineTranslatevalue

        a = translator.detect(lineTranslate.value)

        dropLanguage.value = googletrans.LANGUAGES[a.lang].capitalize()

        page.update()

    lineTranslate = ft.TextField(label="Переклад", max_lines=5, expand=True, read_only=True)
    lineMessage = ft.TextField(label="Введіть ваш текст", on_change=Translation, max_lines=5, expand=True)
    btnChange = ft.IconButton(icon=ft.icons.CHANGE_CIRCLE, on_click=change)


    page.add(ft.Row([
        lineMessage,
        lineTranslate,
    ]), ft.Row([dropLanguage, btnChange]))

if __name__ == '__main__':
    ft.app(target=main)
