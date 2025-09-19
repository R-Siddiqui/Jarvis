import pyperclip
import time
from googletrans import Translator, LANGUAGES
import logging

# Logging setup
logging.basicConfig(filename='translator.log', level=logging.INFO, 
                   format='%(asctime)s - %(levelname)s - %(message)s')

class TextTranslator:
    def __init__(self):
        self.translator = Translator()
        self.last_clipboard = ""

    def log_action(self, action, status, details=""):
        """Log translation actions for debugging."""
        logging.info(f"Action: {action} | Status: {status} | Details: {details}")

    def detect_language(self, text):
        """Detect the language of the input text."""
        try:
            detection = self.translator.detect(text)
            lang_code = detection.lang
            lang_name = LANGUAGES.get(lang_code, "Unknown")
            self.log_action("Language Detection", "Success", f"Detected language: {lang_name}")
            return lang_code, lang_name
        except Exception as e:
            self.log_action("Language Detection", "Error", str(e))
            return None, None

    def translate_to_english(self, text):
        """Translate text to English."""
        try:
            if not text.strip():
                return "No text to translate"
            
            lang_code, lang_name = self.detect_language(text)
            if lang_code == "en":
                self.log_action("Translation", "Skipped", "Text is already in English")
                return f"Text is already in English: {text}"
            
            translated = self.translator.translate(text, dest='en')
            self.log_action("Translation", "Success", f"Translated from {lang_name} to English: {translated.text}")
            return f"Original ({lang_name}): {text}\nTranslated to English: {translated.text}"
        
        except Exception as e:
            self.log_action("Translation", "Error", str(e))
            return f"Error translating text: {str(e)}"

    def monitor_clipboard(self):
        """Monitor clipboard for new text and translate it."""
        print("Monitoring clipboard... Copy any text to translate to English (Ctrl+C to exit).")
        try:
            while True:
                current_clipboard = pyperclip.paste()
                if current_clipboard != self.last_clipboard and current_clipboard.strip():
                    self.last_clipboard = current_clipboard
                    print("\nNew text detected in clipboard:")
                    print(self.translate_to_english(current_clipboard))
                    print("-" * 50)
                time.sleep(1)  # Check clipboard every second
        except KeyboardInterrupt:
            print("\nStopped monitoring clipboard.")
            self.log_action("Clipboard Monitoring", "Stopped", "User interrupted")

if __name__ == "__main__":
    translator = TextTranslator()
    translator.monitor_clipboard()