# 🛡️ Entropy Rewrite Plan

This document outlines the plan to rewrite the Entropy project from scratch to address security vulnerabilities, structural issues, and maintainability.

## 🎯 Goal
Transform Entropy from a simple monolithic script into a professional, modular, and secure password security suite.

## ⚠️ User Review Required
> [!IMPORTANT]
> **Security Upgrade**: The current version uses `random` (Mersenne Twister) which is **not cryptographically secure**. The new version will STRICTLY use `secrets` (Python) and OS-level CSPRNG (`/dev/urandom` or `BCryptGenRandom`) for the C port.

> [!NOTE]
> **Modularization**: The codebase will be split into a proper Python package structure. This means `main.py` will disappear in favor of a `entropy` command installed via pip/poetry.

## 🏗️ Proposed Architecture

### 1. Python Version (Primary)
We will refactor the single `Entropy.py` into a modern package structure:

```text
Entropy/
├── pyproject.toml       # Modern dependency management (Poetry/UV)
├── README.md
├── src/
│   └── entropy/
│       ├── __init__.py
│       ├── __main__.py  # Entry point
│       ├── core/        # Business Logic (Pure Python, No UI)
│       │   ├── __init__.py
│       │   ├── generator.py  # Secure Password/Passphrase generation
│       │   ├── analyzer.py   # Strength analysis algorithms
│       │   └── exceptions.py
│       ├── data/        # Static Data
│       │   ├── __init__.py
│       │   ├── wordlists.py  # Word banks (English/Turkish)
│       └── ui/          # Interface Layer (Rich)
│           ├── __init__.py
│           ├── app.py        # Main App Controller
│           ├── components.py # Reusable widgets (Panels, Banners)
│           └── theme.py      # Color schemes and styles
└── tests/               # Unit Tests (Pytest)
    ├── test_generator.py
    └── test_analyzer.py
```

### 2. C Version (Performance Port)
The C version will be modularized to separate logic from UI, making it a true library-encapsulated tool.

```text
Entropy/
├── c_src/
│   ├── main.c           # CLI Entry point
│   ├── entropy_core.c   # Logic implementation
│   ├── entropy_core.h   # Headers
│   ├── utils.c          # Helpers (Cross-platform sleep/clear)
│   └── Makefile         # Build script
```

---

## 📅 Implementation Steps

### Phase 1: Setup & Core Logic (Python)
- [ ] Initialize project with `poetry` or `uv`.
- [ ] Create `src/entropy/core/generator.py`:
    - Implement `generate_complex` using `secrets` module.
    - Implement `generate_memorable` using `secrets.choice`.
- [ ] Create `src/entropy/core/analyzer.py`:
    - Improve scoring logic (reward entropy bits, penalize common patterns).
    - Add checks for keyboard patterns (optional).

### Phase 2: UI Overhaul (Python)
- [ ] Create `src/entropy/ui/theme.py` to centralize colors/styles.
- [ ] Build `src/entropy/ui/app.py` using `rich.console` and `rich.prompt`.
- [ ] Implement the "Batch Factory" with a proper `Live` display table detached from logic.

### Phase 3: Testing & CI
- [ ] Write unit tests for `generator` ensuring length and charset requirements.
- [ ] Write unit tests for `analyzer` with known weak/strong passwords.

### Phase 4: C Port Modernization (Optional/Secondary)
- [ ] Rewrite `entropy.c` into multiple files.
- [ ] Replace `rand()` with platform-specific secure RNGs:
    - Linux/Mac: `getrandom()` or `/dev/urandom`
    - Windows: `BCryptGenRandom`

## 🧪 Verification Plan

### Automated Tests
Run the test suite to verify core logic:
```bash
pytest tests/
```

### Manual Verification
1. **Generation Check**:
   - Generate 1000 passwords.
   - Verify no duplicates for complex mode (highly unlikely with secure RNG).
   - Verify character distribution (visual check).
2. **Analysis Check**:
   - Input "123456" -> Should return "VULNERABLE".
   - Input "Correct-Horse-Battery-Staple" -> Should return "SECURE".
3. **UI/UX**:
   - Launch app: `python -m entropy`
   - Test navigation through menus.
   - Verify "Batch Factory" live update speed and visual stability.
