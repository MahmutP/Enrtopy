import pytest
import string
from entropy.core.generator import generate_complex, generate_memorable

def test_generate_complex_length():
    pwd = generate_complex(length=20)
    assert len(pwd) == 20

def test_generate_complex_symbols():
    pwd = generate_complex(length=50, use_symbols=True)
    assert any(c in string.punctuation for c in pwd)

def test_generate_complex_no_symbols():
    pwd = generate_complex(length=50, use_symbols=False)
    assert not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in pwd)

def test_generate_memorable_word_count():
    pwd = generate_memorable(word_count=4, separator="-", add_digit=False)
    parts = pwd.split("-")
    assert len(parts) == 4

def test_generate_memorable_digit():
    pwd = generate_memorable(word_count=3, add_digit=True)
    # Ends with number?
    last_part = pwd.split("-")[-1]
    assert last_part.isdigit()
