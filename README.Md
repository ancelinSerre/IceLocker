# Simple password generator CLI 🔑

## Installation

1. Make sure Python >= 3.8.X version is installed:

```
> python --version
```

2. Install program requirements

```
> pip install -r requirements.txt
```
> **Notes**: you are free to use a virtual environment if you prefer, like so:
> ```
> > python -m venv .env
> > source .env/bin/activate 
> > pip install -r requirements.txt
>```

## Usage

You are now ready to generate passwords 😊

```bash
> python password_gen.py
Generated password: 9a>E5DH3
Strength: Reasonable ; Entropy 52
```

For information:

```
usage: password_gen.py [-h] [-l LENGTH] [-a] [-lc] [-uc] [-s] [-d]

Simple password generator

options:
  -h, --help            show this help message and exit
  -l LENGTH, --length LENGTH
                        Password length
  -a, --all             Use lower/upper case characters, digits and specials
  -lc, --lowercase      Use lower case characters
  -uc, --uppercase      Use upper case characters
  -s, --specials        Use special characters
  -d, --digits          Use digits
```