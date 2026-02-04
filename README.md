# 🛡️ Entropy

**Entropy** is a professional, modular, and cryptographically secure password generation and analysis suite.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![C](https://img.shields.io/badge/Language-C-00599C)
![Security](https://img.shields.io/badge/Encryption-CSPRNG-success)

## 🚀 Features

- **Complex Generator**: Cryptographically secure random passwords using logic that filters ambiguous characters.
- **Memorable Passphrases**: XKCD-style memorable passwords (e.g., `Correct-Horse-Battery-Staple`) using English and Turkish wordlists.
- **Strength Analyzer**: Detailed analysis of password entropy, patterns, and structure with visual feedback.
- **Batch Factory**: Generate thousands of passwords instantly with live quality filtering.
- **Modular Architecture**: Clean separation between Logic, UI, and Data.

## 📦 Installation & Usage (Python)

Entropy is now a proper Python package.

### 1. Run Directly (Recommended)
You can run the module directly from the source directory without installation:

```bash
# Ensure you are in the project root
export PYTHONPATH=$PYTHONPATH:$(pwd)/src
python3 -m entropy
```

### 2. Dependencies
Entropy requires `rich` for its user interface.
```bash
pip install rich
```

## ⚡ C Version (High Performance)

The C version has been rewritten for modularity and performance.

### Compilation
```bash
cd c_src
make
```

### Running
```bash
# From project root (after compiling)
./entropy_c_cli
```

## 🏗️ Project Structure

- `src/entropy/`: Main Python package
    - `core/`: Business logic (Generators, Analyzer)
    - `ui/`: Rich text user interface
    - `data/`: Wordlists and static data
- `c_src/`: C implementation source code
