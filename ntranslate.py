import argparse
from googletrans import Translator, LANGUAGES
import random

def translate_file(file_path, n, back_to_english):
    # Initialize the translator
    translator = Translator()
    
    # Read the input file
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Select n random languages
    selected_langs = random.sample(list(LANGUAGES), n)    

    # Sequentially translate the text
    current_text = text
    prev_lang = 'auto'
    for lang in selected_langs:
        translated = translator.translate(current_text, dest=lang, src=prev_lang)
        current_text = translated.text
        print(f"Translated to {LANGUAGES[lang]}: {current_text[:15]}...")  # Showing a snippet for demonstration
        prev_lang = lang

    # Optionally translate back to English
    if back_to_english:
        translated_back = translator.translate(current_text, dest='en')
        current_text = translated_back.text
        print("\nTranslated back to English.")

    # Output the final text
    print("\nFinal translated text:\n")
    print(current_text)

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Translate a text file through multiple languages sequentially.')
    parser.add_argument('file_path', type=str, help='Path to the text file to be translated.')
    parser.add_argument('n', type=int, help='Number of languages to translate through.')
    parser.add_argument('--eng-end', action='store_true', help='Translate the text back to English at the end.')

    args = parser.parse_args()

    # Perform the translation
    translate_file(args.file_path, args.n, args.eng_end)

if __name__ == "__main__":
    main()
