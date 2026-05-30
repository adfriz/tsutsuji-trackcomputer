import json
from pathlib import Path
import locale

class Translator:
    def __init__(self):
        self.translations = {}
        self.config_path = Path(__file__).parent / "config.json"
        self.lang_code = self.load_lang_code()
        self.load_language(self.lang_code)

    def load_lang_code(self):
        if self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    return json.load(f).get("language", "en")
            except Exception:
                pass
        
        # Detect system language
        try:
            sys_lang = locale.getdefaultlocale()[0]
            if sys_lang and sys_lang.startswith("ja"):
                return "ja"
        except Exception:
            pass
        return "en"

    def load_language(self, lang_code):
        self.lang_code = lang_code
        if lang_code == "ja":
            # Japanese is default built-in language, keep translations empty (fall back to default UI text)
            self.translations = {}
            return
            
        locales_dir = Path(__file__).parent / "locales"
        file_path = locales_dir / f"{lang_code}.json"
        
        if file_path.exists():
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    self.translations = json.load(f)
            except Exception:
                self.translations = {}

    def save_language(self, lang_code):
        try:
            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump({"language": lang_code}, f, indent=2)
        except Exception:
            pass
        self.load_language(lang_code)

    def get_available_languages(self):
        langs = {"ja": "日本語"}
        locales_dir = Path(__file__).parent / "locales"
        if locales_dir.exists():
            for p in locales_dir.glob("*.json"):
                lang_code = p.stem
                try:
                    with open(p, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        langs[lang_code] = data.get("_LANG_NAME", lang_code.upper())
                except Exception:
                    langs[lang_code] = lang_code.upper()
        return langs

    def get(self, key, default_text=""):
        return self.translations.get(key, default_text)

lang = Translator()
