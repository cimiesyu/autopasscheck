from colorama import init, Fore, Style

# Inisialisasi colorama supaya otomatis reset warna setelah print
init(autoreset=True)

def color_text(text, color):
    colors = {
        "red": Fore.RED + Style.BRIGHT,
        "green": Fore.GREEN + Style.BRIGHT,
        "yellow": Fore.YELLOW + Style.BRIGHT,
        "cyan": Fore.CYAN + Style.BRIGHT,
    }
    return colors.get(color.lower(), "") + text + Style.RESET_ALL
