from typing import List

# --- English Words ---
ENGLISH_WORDS: List[str] = [
    "sky", "blue", "falcon", "eagle", "mountain", "river", "swift", "silent",
    "storm", "thunder", "pixel", "vector", "cyber", "neon", "solar", "lunar",
    "crypto", "vault", "shield", "guard", "alpha", "bravo", "delta", "echo",
    "shadow", "ghost", "flame", "frost", "iron", "steel", "titan", "atlas",
    "north", "west", "rapid", "hyper", "mega", "giga", "quantum", "laser",
    "orbit", "planet", "star", "comet", "nebula", "dark", "light", "bright",
    "magic", "wizard", "rogue", "ninja", "samurai", "knight", "king", "queen",
]

# --- Turkish Words (ASCII: No ş,ğ,ü,ö,ç,ı) ---
TURKISH_WORDS: List[str] = [
    "kirmizi", "beyaz", "siyah", "mavi", "yesil", "sari", "turuncu", "mor", # Colors
    "dag", "deniz", "gunes", "yildiz", "ay", "bulut", "yagmur", "ruzgar",   # Nature
    "aslan", "kaplan", "kartal", "sahin", "kurt", "ayi", "tilki", "yilan",  # Animals
    "demir", "celik", "altin", "gumus", "bakir", "tas", "toprak", "ates",   # Elements
    "cesur", "guclu", "hizli", "sakin", "derin", "yuksek", "uzak", "yakin", # Adjectives
    "kale", "duvar", "kapi", "anahtar", "kilit", "sifre", "dosya", "veri",  # Objects/Tech
    "istanbul", "ankara", "izmir", "toros", "agri", "firat", "dicle",       # Places
    "efsane", "destan", "roman", "siir", "sarki", "nota", "ritim", "ses",   # Culture
    "bilgi", "zeka", "akil", "fikir", "sanat", "bilim", "uzay", "zaman"     # Abstract
]

ALL_WORDS = ENGLISH_WORDS + TURKISH_WORDS
