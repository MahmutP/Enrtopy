import secrets
import string
from typing import List, Optional
from entropy.data.wordlists import ALL_WORDS

def generate_complex(length: int = 16, use_symbols: bool = True) -> str:
    """
    Generates a cryptographically secure random password.
    
    Args:
        length (int): Length of the password.
        use_symbols (bool): Whether to include special symbols.
        
    Returns:
        str: The generated password.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    char_pool = string.ascii_letters + string.digits
    if use_symbols:
        char_pool += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Remove ambiguous characters (visual clarity)
    ambiguous = "l1O0I"
    char_pool = "".join([c for c in char_pool if c not in ambiguous])

    if not char_pool:
        raise ValueError("Character pool is empty after filtering.")

    return "".join(secrets.choice(char_pool) for _ in range(length))

def generate_memorable(word_count: int = 4, separator: str = "-", 
                      capitalize: bool = True, add_digit: bool = True,
                      custom_words: Optional[List[str]] = None) -> str:
    """
    Generates a memorable passphrase using the XKCD method.
    
    Args:
        word_count (int): Number of words in the passphrase.
        separator (str): Character to separate words.
        capitalize (bool): Whether to capitalize each word.
        add_digit (bool): Whether to append a random 2-digit number.
        custom_words (list): Optional custom list of words to choose from.
        
    Returns:
        str: The generated passphrase.
    """
    pool = custom_words if custom_words else ALL_WORDS
    
    selected_words = [secrets.choice(pool) for _ in range(word_count)]
    
    if capitalize:
        selected_words = [w.capitalize() for w in selected_words]
    
    passphrase = separator.join(selected_words)
    
    if add_digit:
        # secrets.randbelow(100) returns 0..99
        passphrase += f"{separator}{secrets.randbelow(100)}"
        
    return passphrase
