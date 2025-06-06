from checker import PasswordChecker
from utils import color_text

def main():
    print(color_text("=== AutoPassCheck ===", "cyan"))
    password = input("Masukkan password yang ingin dicek: ")

    checker = PasswordChecker(password)
    issues = checker.run_all_checks()

    if issues:
        for issue in issues:
            # merah untuk issue berat, kuning untuk yang kurang penting
            color = "red" if "wordlist" in issue or "pendek" in issue else "yellow"
            print(color_text(issue, color))
        print(color_text("\nPassword lemah, perlu diperbaiki.", "red"))
    else:
        print(color_text("Password kuat.", "green"))

if __name__ == "__main__":
    main()
