from rich.theme import Theme
from rich.style import Style

COLORS = {
    "primary": "cyan",
    "secondary": "purple",
    "success": "green",
    "warning": "yellow",
    "danger": "red",
    "text": "white",
    "dim": "dim white",
}

custom_theme = Theme({
    "info": "dim cyan",
    "warning": "magenta",
    "danger": "bold red",
    "success": "bold green",
    "title": "bold cyan underline",
    "header": "bold white on blue",
    "prompt.choices": "magenta",
    "input.password": "dim",
})
