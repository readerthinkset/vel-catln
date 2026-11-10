"""VELOCITY CATALAN - language pack, brand and motion design constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
FPS = 30

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY CATALAN"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "CATALAN"
HANDLE = "@velocitycatalan"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {
    "code": "ca",
    "name": "Catalan",
    "native_name": "Català",
    "history_key": "catalan",
    "english_voice": "en-US-AvaNeural",
    "english_fallback_voice": "en-US-GuyNeural",
    "native_voice": "ca-ES-EnricNeural",
    "native_fallback_voice": "ca-ES-JoanaNeural",
    "native_engine": "edge",
    "native_lang_code": "ca",
    "english_rate": "-2%",
    "native_rate": "-6%",
    "english_pitch": "+0Hz",
    "native_pitch": "+0Hz",
    "native_label": "CATALÀ",
    "translit_label": "SAY IT LIKE",
    "greeting": "Hola!",
    "encouragement": "Molt bé!",
    "rtl": False,
    "char_tiles": False,
    "script_font": "",
}
# ==== LANGUAGE PACK END ====

AI_MODEL = os.getenv("AI_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 4.0
OUTRO_DURATION = 5.2
EN_CARD_IN = 0.55
GAP_EN_NATIVE = 0.5
NATIVE_CARD_LEAD = 0.35
GAP_BEFORE_REPEAT = 0.8
TAIL_HOLD = 1.4
MAX_REEL_DURATION = 88.0

# ---------------------------------------------------------------- palette

INK = "#3C3C3C"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#A560E8"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

PALETTE = [GREEN, BLUE, PURPLE, ORANGE, RED, YELLOW, TEAL, PINK]

# ---------------------------------------------------------------- categories
# (english, native, icon, accent)

# ==== CATEGORY TABLE START ====
CATEGORY_TABLE = [
    ("Greetings", "Salutacions", "hand", "#1CB0F6"),
    ("Basic Phrases", "Frases Bàsiques", "chat", "#58CC02"),
    ("Common Expressions", "Expressions Comunes", "chat", "#1CB0F6"),
    ("Travel", "Viatge", "plane", "#1CB0F6"),
    ("Restaurant", "Restaurant", "fork", "#FF7A00"),
    ("Shopping", "Compres", "bag", "#E056A0"),
    ("Emergency", "Emergència", "siren", "#FF4B4B"),
    ("Family Terms", "Termes Familiars", "heart", "#E056A0"),
    ("Numbers", "Números", "hash", "#A560E8"),
    ("Time", "Temps", "clock", "#00A889"),
    ("Motivation", "Motivació", "rocket", "#A560E8"),
    ("Love", "Amor", "heart", "#FF4B4B"),
    ("Success", "Èxit", "trophy", "#F5A700"),
    ("Wisdom", "Saviesa", "book", "#A560E8"),
    ("Happiness", "Felicitat", "smile", "#F5A700"),
    ("Self Improvement", "Automillora", "leaf", "#58CC02"),
    ("Gratitude", "Gratitud", "heart", "#FF7A00"),
    ("Friendship", "Amistat", "users", "#00A889"),
    ("Hope", "Esperança", "sun", "#FF7A00"),
    ("Creativity", "Creativitat", "palette", "#E056A0"),
    ("Inner Peace", "Pau Interior", "lotus", "#00A889"),
    ("Confidence", "Confiança", "shield", "#1CB0F6"),
    ("Perseverance", "Perseverança", "mountain", "#FF7A00"),
    ("Inspiration", "Inspiració", "sparkles", "#A560E8"),
    ("Positive Life", "Vida Positiva", "sun", "#58CC02"),
    ("Courage", "Coratge", "shield", "#FF4B4B"),
    ("Kindness", "Amabilitat", "heart", "#E056A0"),
    ("Patience", "Paciència", "hourglass", "#00A889"),
    ("Forgiveness", "Perdó", "hands", "#FF7A00"),
    ("Strength", "Força", "dumbbell", "#FF4B4B"),
    ("Joy", "Alegria", "smile", "#F5A700"),
    ("Balance", "Equilibri", "scale", "#00A889"),
    ("Growth", "Creixement", "sprout", "#58CC02"),
    ("Purpose", "Propòsit", "target", "#A560E8"),
    ("Mindfulness", "Atenció Plena", "lotus", "#00A889"),
    ("Daily Routine", "Rutina diària", "calendar", "#1CB0F6"),
    ("Weather", "Temps", "cloud", "#1CB0F6"),
    ("Feelings", "Sentiments", "smile", "#E056A0"),
    ("Food", "Menjar", "fork", "#FF7A00"),
    ("Health", "Salut", "heart", "#58CC02"),
    ("Work", "Feina", "briefcase", "#1CB0F6"),
    ("Technology", "Tecnologia", "chip", "#A560E8"),
    ("Nature", "Natura", "leaf", "#58CC02"),
    ("Animals", "Animals", "paw", "#FF7A00"),
    ("Colors", "Colors", "palette", "#E056A0"),
    ("Directions", "Direccions", "compass", "#1CB0F6"),
    ("Body Parts", "Parts del cos", "hand", "#00A889"),
    ("Clothes", "Roba", "shirt", "#E056A0"),
    ("Music", "Música", "music", "#A560E8"),
    ("Sports", "Esports", "ball", "#FF7A00"),
    ("Holidays", "Festes", "gift", "#FF4B4B"),
    ("Education", "Educació", "book", "#1CB0F6"),
    ("Culture", "Cultura", "globe", "#00A889"),
    ("Finance", "Finances", "coin", "#58CC02"),
    ("Relationships", "Relacions", "users", "#E056A0"),
]
# ==== CATEGORY TABLE END ====

CATEGORIES = [c[0] for c in CATEGORY_TABLE]
CATEGORIES_NATIVE = {c[0]: c[1] for c in CATEGORY_TABLE}
CATEGORY_META = {c[0]: {"native": c[1], "icon": c[2], "accent": c[3]} for c in CATEGORY_TABLE}
MAX_RECENT_CATEGORIES = 25

# ==== HASHTAGS START ====
HASHTAGS = [
    "#learncatalan",
    "#catalanlessons",
    "#catalanforbeginners",
    "#languagelearning",
    "#catalanvocabulary",
    "#velocitycatalan",
    "#dailycatalan",
    "#catalan",
    "#learnlanguages",
    "#speakcatalan",
    "#bilingual",
    "#languagetips",
]
# ==== HASHTAGS END ====
