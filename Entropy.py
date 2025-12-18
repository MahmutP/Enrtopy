import random 
# rastgelelik için kullan.
import string
# string'leri şifre oluşturmada kullanmak için import edildi.
import time
# zaman işleri için.
import os
# komutlarla ekranı temizleme için.
from typing import List, Dict
# spesifik değişken tipleri için.

# Kullanıcı arayüzü kompanentleri için rich kütüphanesi importları.
from rich.console import Console
# Konsol arayüzüne nesneler basmak ve renkli yazılar ve rich unsularını ekrana basmak için.
from rich.table import Table
# tablolar oluştumak için kullanılan kompanent.
from rich.panel import Panel
# Panel oluşturmak için.
from rich.align import Align
# Hizallama için.
from rich.layout import Layout
# Layout sınıfı, terminal ekranını esnek bir şekilde dikey veya yatay parçalara bölerek içerikleri (panel, tablo, metin vb.) 
# bu alanlara düzenli bir ızgara (grid) yapısında yerleştirmenizi sağlar.
from rich.live import Live
# Live sınıfı, terminaldeki bir içeriği (tablo, panel vb.) sürekli temizleyip tekrar yazdırmadan, 
# anlık ve akıcı bir şekilde güncelleyebilmenizi (animasyon gibi) sağlar.
from rich.text import Text
# text nesneleri için.
from rich.progress import track, Progress, SpinnerColumn, BarColumn, TextColumn
# Progressbar ve spinner için.
from rich.prompt import Prompt, IntPrompt, Confirm
# prompt oluşturmak için.
from rich import box
# kutu oluşturmak için.

# custom konsol init'leme
konsol = Console()


class Entropy:
    def __init__(self):
        self.app_name = "Entropy Pass"
        self.version = "v2.2"
        self.word_list = [
            # --- English Words ---
            "sky", "blue", "falcon", "eagle", "mountain", "river", "swift", "silent",
            "storm", "thunder", "pixel", "vector", "cyber", "neon", "solar", "lunar",
            "crypto", "vault", "shield", "guard", "alpha", "bravo", "delta", "echo",
            "shadow", "ghost", "flame", "frost", "iron", "steel", "titan", "atlas",
            "north", "west", "rapid", "hyper", "mega", "giga", "quantum", "laser",
            "orbit", "planet", "star", "comet", "nebula", "dark", "light", "bright",
            "magic", "wizard", "rogue", "ninja", "samurai", "knight", "king", "queen",
            
            # --- Turkish Words (ASCII: No ş,ğ,ü,ö,ç,ı) ---
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

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_banner(self):
        self.clear_screen()
        title_text = Text(f"🛡️ {self.app_name} SYSTEM", style="bold cyan")
        subtitle_text = Text(f"Secure Identity Management Module {self.version}", style="dim white")
        
        header_panel = Panel(
            Align.center(Text.assemble(title_text, "\n", subtitle_text)),
            box=box.DOUBLE_EDGE,
            border_style="bright_blue",
            padding=(1, 2)
        )
        konsol.print(header_panel)

    def show_loading(self, message: str, duration: float = 1.5):
        with konsol.status(f"[bold green]{message}[/bold green]", spinner="dots12"):
            time.sleep(duration)

    def generate_logic(self, length=16, use_symbols=True) -> str:
        char_pool = string.ascii_letters + string.digits
        if use_symbols:
            char_pool += "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        ambiguous = "l1O0I"
        char_pool = "".join([c for c in char_pool if c not in ambiguous])
        
        return "".join(random.choice(char_pool) for _ in range(length))
    
    def generate_memorable_logic(self, word_count=4, separator="-", capitalize=True, add_digit=True) -> str:
        selected_words = random.sample(self.word_list, word_count)
        
        if capitalize:
            selected_words = [w.capitalize() for w in selected_words]
        
        passphrase = separator.join(selected_words)
        
        if add_digit:
            passphrase += f"{separator}{random.randint(0, 99)}"
            
        return passphrase
    
    def analyze_logic(self, password: str) -> Dict:
        score = 0
        pros = []
        cons = []
        
        if len(password) >= 20: score += 40; pros.append("Exceptional Length (Passphrase?)")
        elif len(password) >= 16: score += 30; pros.append("Excellent Length")
        elif len(password) >= 12: score += 20; pros.append("Good Length")
        else: cons.append("Short Length")

        if any(c.isupper() for c in password): score += 10; pros.append("Uppercase")
        if any(c.islower() for c in password): score += 10; pros.append("Lowercase")
        if any(c.isdigit() for c in password): score += 20; pros.append("Digits")
        if any(c in string.punctuation for c in password): score += 20; pros.append("Symbols")
        
        if "-" in password or "_" in password or "." in password:
            score += 10
            pros.append("Good Separation/Entropy")

        score = min(score, 100)

        if score >= 90: color = "bright_green"; status = "SECURE"
        elif score >= 60: color = "yellow"; status = "MODERATE"
        else: color = "red"; status = "VULNERABLE"

        return {"score": score, "color": color, "status": status, "pros": pros, "cons": cons}

    def ui_generate_password(self):
        self.print_banner()
        konsol.print("[bold underline cyan]>> GENERATE: COMPLEX MODE[/bold underline cyan]\n")
        
        length = IntPrompt.ask("[cyan]?[/cyan] Password Length", default=16)
        use_sym = Confirm.ask("[cyan]?[/cyan] Include Symbols", default=True)

        self.show_loading("Encrypting entropy pool...", duration=1.0)
        password = self.generate_logic(length, use_sym)
        self.display_result(password, "GENERATED KEY")

    def ui_generate_memorable(self):
        self.print_banner()
        konsol.print("[bold underline green]>> GENERATE: MEMORABLE MODE[/bold underline green]\n")
        
        word_count = IntPrompt.ask("[green]?[/green] Word Count", default=4)
        separator = Prompt.ask("[green]?[/green] Separator", default="-", choices=["-", "_", ".", " "])
        add_digit = Confirm.ask("[green]?[/green] Add Random Number at end?", default=True)

        self.show_loading("Fetching dictionary words...", duration=0.8)
        self.show_loading("Shuffling logic gates...", duration=0.5)
        
        passphrase = self.generate_memorable_logic(word_count, separator, True, add_digit)
        self.display_result(passphrase, "MEMORABLE PASSPHRASE")

    def display_result(self, text, title):
        konsol.print("\n")
        konsol.print(Panel(
            Align.center(f"[bold white on black] {text} [/bold white on black]"),
            title=f"[bold green]{title}[/bold green]",
            border_style="green",
            box=box.ROUNDED,
            padding=(1, 4)
        ))
        konsol.input("\n[dim]Press Enter to return menu...[/dim]")

    def ui_analyze_password(self):
        self.print_banner()
        konsol.print("[bold underline magenta]>> ANALYZE MODE[/bold underline magenta]\n")

        pwd = Prompt.ask("[magenta]?[/magenta] Enter Password to Scan", password=False)
        self.show_loading("Scanning vulnerability database...", duration=1.2)
        result = self.analyze_logic(pwd)
        
        # Visual Score Bar
        bar_length = 30
        filled_length = int(bar_length * result['score'] // 100)
        bar = "█" * filled_length + "░" * (bar_length - filled_length)
        
        report_text = Text()
        report_text.append(f"\nSECURITY LEVEL: {result['status']}\n", style=f"bold {result['color']}")
        report_text.append(f"INTEGRITY: [{bar}] {result['score']}%\n\n", style=f"{result['color']}")
        
        grid = Table.grid(expand=True)
        grid.add_column()
        grid.add_column()
        
        pros_txt = "\n".join([f"[green]✓ {p}[/green]" for p in result['pros']])
        cons_txt = "\n".join([f"[red]✗ {c}[/red]" for c in result['cons']])
        
        grid.add_row(
            Panel(pros_txt, title="STRENGTHS", border_style="green"),
            Panel(cons_txt, title="WEAKNESSES", border_style="red")
        )

        konsol.print(Panel(Align.center(report_text), title="SCAN RESULT", border_style=result['color'], box=box.HEAVY))
        konsol.print(grid)
        konsol.input("\n[dim]Press Enter to return menu...[/dim]")

    def ui_batch_process(self):
        self.print_banner()
        konsol.print("[bold underline yellow]>> BATCH FACTORY MODE[/bold underline yellow]\n")

        count = IntPrompt.ask("[yellow]?[/yellow] Quantity", default=10)
        
        table = Table(box=box.SIMPLE_HEAD, title="Live Generation Feed")
        table.add_column("Password", style="dim")
        table.add_column("Score", justify="right")
        table.add_column("Verdict", justify="center")

        strong_count = 0
        saved_list = []

        with Live(table, refresh_per_second=10) as live:
            for _ in range(count):
                time.sleep(0.1)
                if random.choice([True, False]):
                    pwd = self.generate_logic(length=random.randint(14, 20))
                else:
                    pwd = self.generate_memorable_logic(word_count=3, add_digit=True)

                res = self.analyze_logic(pwd)
                masked = pwd[:5] + "..." + pwd[-2:] if len(pwd) > 8 else "****"
                
                verdict_icon = "🛡️" if res['score'] >= 80 else "⚠️"
                verdict_style = "green" if res['score'] >= 80 else "red"
                
                table.add_row(masked, str(res['score']), f"[{verdict_style}]{verdict_icon}[/{verdict_style}]")
                
                if res['score'] >= 80:
                    strong_count += 1
                    saved_list.append(pwd)

        konsol.print(Panel(
            f"[bold]Total Processed:[/bold] {count}\n[bold green]High Security Passwords:[/bold green] {strong_count}\n[bold red]Discarded:[/bold red] {count - strong_count}",
            title="BATCH REPORT", border_style="yellow", width=50
        ))
        
        if saved_list:
            with open("vault.txt", "w") as f:
                f.write("\n".join(saved_list))
            konsol.print("[italic green]✓ Exported to 'vault.txt'[/italic green]")
        
        konsol.input("\n[dim]Press Enter to return menu...[/dim]")

    # -------------------------------------------------------------------------
    # MAIN MENU
    # -------------------------------------------------------------------------
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
            
            konsol.print(Align.center(menu_table))
            
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
                konsol.print("\n[bold red]Shutting down Entropy...[/bold red]")
                time.sleep(0.5)
                break

if __name__ == "__main__":
    app = Entropy()
    app.run()
