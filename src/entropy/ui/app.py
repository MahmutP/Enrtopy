import time
import sys
import random
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich.prompt import Prompt, IntPrompt, Confirm
from rich.live import Live
from rich import box
from rich.text import Text

from entropy import __version__
from entropy.ui.theme import custom_theme, COLORS
from entropy.ui.components import create_banner, create_result_panel
from entropy.core.generator import generate_complex, generate_memorable
from entropy.core.analyzer import analyze_password

console = Console(theme=custom_theme)

class EntropyApp:
    def __init__(self):
        self.app_name = "Entropy Pass"
        
    def clear_screen(self):
        console.clear()

    def print_banner(self):
        self.clear_screen()
        console.print(create_banner(self.app_name, __version__))

    def show_loading(self, message: str, duration: float = 1.0):
        with console.status(f"[bold green]{message}[/bold green]", spinner="dots12"):
            time.sleep(duration)

    def ui_generate_password(self):
        self.print_banner()
        console.print("[bold underline cyan]>> GENERATE: COMPLEX MODE[/bold underline cyan]\n")
        
        length = IntPrompt.ask("[cyan]?[/cyan] Password Length", default=16)
        use_sym = Confirm.ask("[cyan]?[/cyan] Include Symbols", default=True)

        self.show_loading("Encrypting entropy pool...", duration=0.8)
        
        try:
            password = generate_complex(length, use_sym)
            console.print("\n")
            console.print(create_result_panel(password, "GENERATED KEY"))
        except ValueError as e:
            console.print(f"[bold red]Error:[/bold red] {e}")
            
        console.input("\n[dim]Press Enter to return menu...[/dim]")

    def ui_generate_memorable(self):
        self.print_banner()
        console.print("[bold underline green]>> GENERATE: MEMORABLE MODE[/bold underline green]\n")
        
        word_count = IntPrompt.ask("[green]?[/green] Word Count", default=4)
        separator = Prompt.ask("[green]?[/green] Separator", default="-", choices=["-", "_", ".", " "])
        add_digit = Confirm.ask("[green]?[/green] Add Random Number at end?", default=True)

        self.show_loading("Fetching dictionary words...", duration=0.8)
        
        passphrase = generate_memorable(word_count, separator, True, add_digit)
        console.print("\n")
        console.print(create_result_panel(passphrase, "MEMORABLE PASSPHRASE", style="magenta"))
        
        console.input("\n[dim]Press Enter to return menu...[/dim]")

    def ui_analyze_password(self):
        self.print_banner()
        console.print("[bold underline magenta]>> ANALYZE MODE[/bold underline magenta]\n")

        pwd = Prompt.ask("[magenta]?[/magenta] Enter Password to Scan", password=False)
        self.show_loading("Scanning vulnerability database...", duration=1.0)
        
        result = analyze_password(pwd)
        
        # Visual Score Bar
        score = result['score']
        bar_length = 30
        filled_length = int(bar_length * score // 100)
        bar = "█" * filled_length + "░" * (bar_length - filled_length)
        
        report_text = Text()
        report_text.append(f"\nSECURITY LEVEL: {result['status']}\n", style=f"bold {result['color']}")
        report_text.append(f"INTEGRITY: [{bar}] {score}%\n\n", style=f"{result['color']}")
        
        grid = Table.grid(expand=True)
        grid.add_column()
        grid.add_column()
        
        pros_txt = "\n".join([f"[green]✓ {p}[/green]" for p in result['pros']])
        cons_txt = "\n".join([f"[red]✗ {c}[/red]" for c in result['cons']]) if result['cons'] else "[dim]No specific weaknesses found.[/dim]"
        
        grid.add_row(
            Panel(pros_txt, title="STRENGTHS", border_style="green"),
            Panel(cons_txt, title="WEAKNESSES", border_style="red")
        )

        console.print(Panel(Align.center(report_text), title="SCAN RESULT", border_style=result['color'], box=box.HEAVY))
        console.print(grid)
        console.input("\n[dim]Press Enter to return menu...[/dim]")

    def ui_batch_process(self):
        self.print_banner()
        console.print("[bold underline yellow]>> BATCH FACTORY MODE[/bold underline yellow]\n")

        count = IntPrompt.ask("[yellow]?[/yellow] Quantity", default=10)
        
        table = Table(box=box.SIMPLE_HEAD, title="Live Generation Feed")
        table.add_column("Password", style="dim")
        table.add_column("Score", justify="right")
        table.add_column("Verdict", justify="center")

        strong_count = 0
        saved_list = []

        with Live(table, refresh_per_second=10) as live:
            for _ in range(count):
                time.sleep(0.05) # Simulation speed
                
                # Randomly choose between complex and memorable for demo variety
                if random.choice([True, False]):
                    pwd = generate_complex(length=random.randint(14, 20))
                else:
                    pwd = generate_memorable(word_count=3, add_digit=True)

                res = analyze_password(pwd)
                masked = pwd[:5] + "..." + pwd[-2:] if len(pwd) > 8 else "****"
                
                verdict_icon = "🛡️" if res['score'] >= 80 else "⚠️"
                verdict_style = "green" if res['score'] >= 80 else "red"
                
                table.add_row(masked, str(res['score']), f"[{verdict_style}]{verdict_icon}[/{verdict_style}]")
                
                if res['score'] >= 80:
                    strong_count += 1
                    saved_list.append(pwd)

        console.print(Panel(
            f"[bold]Total Processed:[/bold] {count}\n[bold green]High Security Passwords:[/bold green] {strong_count}\n[bold red]Discarded:[/bold red] {count - strong_count}",
            title="BATCH REPORT", border_style="yellow", width=50
        ))
        
        if saved_list:
            with open("vault.txt", "w") as f:
                f.write("\n".join(saved_list))
            console.print("[italic green]✓ Exported to 'vault.txt'[/italic green]")
        
        console.input("\n[dim]Press Enter to return menu...[/dim]")

    def run(self):
        while True:
            self.print_banner()
            
            menu_table = Table(show_header=False, box=box.ROUNDED, border_style="bright_blue")
            menu_table.add_column("Opt", justify="center", style="cyan bold", width=5)
            menu_table.add_column("Desc", style="white")
            
            menu_table.add_row("1", "Generate Complex Password (Random)")
            menu_table.add_row("2", "Generate Memorable Passphrase (XKCD)")
            menu_table.add_row("3", "Analyze Password Strength")
            menu_table.add_row("4", "Batch Generation (Vault Mode)")
            menu_table.add_row("5", "[red]Exit System[/red]")
            
            console.print(Align.center(menu_table))
            
            choice = Prompt.ask("\n[bold cyan]COMMAND[/bold cyan]", choices=["1", "2", "3", "4", "5"], default="1")
            
            if choice == "1":
                self.ui_generate_password()
            elif choice == "2":
                self.ui_generate_memorable()
            elif choice == "3":
                self.ui_analyze_password()
            elif choice == "4":
                self.ui_batch_process()
            elif choice == "5":
                console.print("\n[bold red]Shutting down Entropy...[/bold red]")
                break
