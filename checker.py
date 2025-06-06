import gzip
import os
from utils import color_text

ROCKYOU_PATH = "/usr/share/wordlists/rockyou.txt.gz"

class PasswordChecker:
    def __init__(self, password):
        self.password = password
        self.issues = []

    def check_length(self):
        if len(self.password) < 8:
            self.issues.append("Password terlalu pendek, minimal 8 karakter.")

    def check_uppercase(self):
        if self.password.lower() == self.password:
            self.issues.append("Tambahkan huruf besar.")

    def check_digit(self):
        if not any(c.isdigit() for c in self.password):
            self.issues.append("Tambahkan angka.")

    def check_special_char(self):
        special_chars = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|"
        if not any(c in special_chars for c in self.password):
            self.issues.append("Tambahkan simbol khusus.")

    def check_rockyou(self):
        if not os.path.isfile(ROCKYOU_PATH):
            print(color_text("[WARNING] Wordlist RockYou tidak ditemukan. Abaikan pengecekan ini.", "yellow"))
            return

        try:
            with gzip.open(ROCKYOU_PATH, 'rt', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    if self.password == line.strip():
                        self.issues.append("Password ditemukan di wordlist RockYou, sangat lemah!")
                        break
        except Exception as e:
            print(color_text(f"[ERROR] Gagal membaca wordlist RockYou: {e}", "red"))

    def run_all_checks(self):
        self.check_length()
        self.check_uppercase()
        self.check_digit()
        self.check_special_char()
        self.check_rockyou()
        return self.issues
