from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich import box
from entropy.ui.theme import COLORS

def create_banner(app_name: str, version: str) -> Panel:
    """Creates the main application banner."""
    title_text = Text(f"🛡️ {app_name} SYSTEM", style=f"bold {COLORS['primary']}")
    subtitle_text = Text(f"Secure Identity Management Module {version}", style=COLORS['dim'])
    
    return Panel(
        Align.center(Text.assemble(title_text, "\n", subtitle_text)),
        box=box.DOUBLE_EDGE,
        border_style="bright_blue",
        padding=(1, 2)
    )

def create_result_panel(text: str, title: str, style: str = "green") -> Panel:
    """Creates a panel to display generated passwords or results."""
    return Panel(
        Align.center(f"[bold white on black] {text} [/bold white on black]"),
        title=f"[bold {style}]{title}[/bold {style}]",
        border_style=style,
        box=box.ROUNDED,
        padding=(1, 4)
    )
