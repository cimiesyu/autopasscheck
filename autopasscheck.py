from colorama import Fore, Style, init
import re

init(autoreset=True)

def password_strength(password):
    score = 0

    # Panjang password minimal 8 karakter
    if len(password) >= 8:
        score += 1
    else:
        print(Fore.RED + "Password terlalu pendek, minimal 8 karakter.")

    # Ada huruf kecil
    if re.search(r'[a-z]', password):
        score += 1
    else:
        print(Fore.RED + "Tambahkan huruf kecil.")

    # Ada huruf besar
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        print(Fore.RED + "Tambahkan huruf besar.")

    # Ada angka
    if re.search(r'\d', password):
        score += 1
    else:
        print(Fore.RED + "Tambahkan angka.")

    # Ada simbol khusus
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        print(Fore.RED + "Tambahkan simbol khusus.")

    return score

def main():
    print(Fore.CYAN + "=== AutoPassCheck ===")
    password = input("Masukkan password yang ingin dicek: ")

    score = password_strength(password)
    print()

    if score == 5:
        print(Fore.GREEN + "Password sangat kuat!")
    elif 3 <= score < 5:
        print(Fore.YELLOW + "Password cukup kuat, tapi bisa diperbaiki.")
    else:
        print(Fore.RED + "Password lemah, perlu diperbaiki.")

if __name__ == "__main__":
    main()
