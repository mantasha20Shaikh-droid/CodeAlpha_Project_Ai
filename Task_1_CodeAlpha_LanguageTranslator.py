# TASK 1 — Language Translation Tool
   # Install Libraries

print("----Task 1 - Language Translation Tool----")
!pip install deep-translator gradio -q
   # Translation App Code

from deep_translator import GoogleTranslator
import gradio as gr

def translate_text(text, source_lang, target_lang):
    try:
        translated = GoogleTranslator(
            source=source_lang,
            target=target_lang
        ).translate(text)

        return translated

    except Exception as e:
        return str(e)

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Gujarati": "gu",
    "Arabic": "ar"
}

iface = gr.Interface(
    fn=translate_text,
    inputs=[
        gr.Textbox(label="Enter Text"),
        gr.Dropdown(list(languages.values()), label="Source Language"),
        gr.Dropdown(list(languages.values()), label="Target Language")
    ],
    outputs="text",
    title="Language Translation Tool"
)

iface.launch()
