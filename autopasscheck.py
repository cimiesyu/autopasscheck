import tkinter as tk
from tkinter import messagebox
import time
import threading

from checker import PasswordChecker

class AutoPassCheckApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AutoPassCheck - Dark Mode")
        self.geometry("580x470")
        self.configure(bg="#1e1e2e")  # Dark background
        self.resizable(False, False)

        # Font
        self.font_title = ("Segoe UI", 22, "bold")
        self.font_label = ("Segoe UI", 13)
        self.font_text = ("Consolas", 12)
        self.font_italic = ("Segoe UI", 11, "italic")

        # Dark theme colors
        self.color_primary = "#89b4fa"   # light blue
        self.color_success = "#a6e3a1"   # green
        self.color_warning = "#f9e2af"   # yellowish
        self.color_danger = "#f38ba8"    # red/pink
        self.color_bg = "#1e1e2e"
        self.color_input_bg = "#313244"
        self.color_text = "#cdd6f4"

        self.create_widgets()

    def create_widgets(self):
        self.label_title = tk.Label(self, text="AutoPassCheck", font=self.font_title,
                                    fg=self.color_primary, bg=self.color_bg)
        self.label_title.pack(pady=(20, 10))

        frame_input = tk.Frame(self, bg=self.color_bg)
        frame_input.pack(pady=10)

        self.label_instruction = tk.Label(frame_input, text="Masukkan password yang ingin dicek:",
                                          font=self.font_label, bg=self.color_bg, fg=self.color_text)
        self.label_instruction.pack(anchor="w", padx=5, pady=(0,5))

        self.entry_password = tk.Entry(frame_input, font=self.font_text, width=40,
                                       bg=self.color_input_bg, fg=self.color_text,
                                       insertbackground=self.color_text, bd=2, relief="groove")
        self.entry_password.pack(padx=5)
        self.entry_password.focus()

        self.btn_check = tk.Button(self, text="Cek Password", font=self.font_label,
                                   bg=self.color_primary, fg="#1e1e2e", activebackground="#74c7ec",
                                   relief="flat", padx=20, pady=8, command=self.start_check)
        self.btn_check.pack(pady=15)

        self.status_label = tk.Label(self, text="", font=("Segoe UI", 15, "bold"),
                                     bg=self.color_bg, fg=self.color_warning)
        self.status_label.pack()

        self.result_text = tk.Text(self, width=65, height=13, font=self.font_text,
                                   bg=self.color_input_bg, fg=self.color_text,
                                   bd=0, relief="flat", wrap="word")
        self.result_text.pack(padx=15, pady=10)
        self.result_text.config(state="disabled")

        self.btn_copy = tk.Button(self, text="Salin Saran Password", font=self.font_label,
                                  bg=self.color_success, fg="#1e1e2e", relief="flat", padx=18, pady=7,
                                  command=self.copy_suggestions)
        self.btn_copy.pack(pady=10)
        self.btn_copy.config(state="disabled")

    def copy_suggestions(self):
        try:
            self.clipboard_clear()
            self.clipboard_append(self.suggestions_text)
            messagebox.showinfo("Sukses", "Saran password berhasil disalin ke clipboard.")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menyalin: {e}")

    def start_check(self):
        password = self.entry_password.get().strip()
        if not password:
            messagebox.showwarning("Peringatan", "Password tidak boleh kosong atau hanya spasi.")
            return
        if " " in password:
            messagebox.showwarning("Peringatan", "Password tidak boleh mengandung spasi.")
            return

        self.btn_check.config(state="disabled")
        self.status_label.config(text="Memeriksa password...", fg=self.color_warning)
        self.result_text.config(state="normal")
        self.result_text.delete("1.0", tk.END)
        self.result_text.config(state="disabled")
        self.btn_copy.config(state="disabled")

        threading.Thread(target=self.check_password, args=(password,), daemon=True).start()

    def check_password(self, password):
        for i in range(6):
            dots = "." * (i % 4)
            self.status_label.config(text=f"Memeriksa password{dots}", fg=self.color_warning)
            time.sleep(0.4)

        checker = PasswordChecker(password)
        issues = checker.run_all_checks()
        self.after(0, self.show_results, issues, checker)

    def show_results(self, issues, checker):
        self.result_text.config(state="normal")
        self.result_text.delete("1.0", tk.END)

        if issues:
            self.status_label.config(text="Password sedang diperbaiki", fg=self.color_warning)

            checklist_issues = []
            special_messages = []

            for issue in issues:
                if any(keyword in issue.lower() for keyword in ["panjang", "huruf besar", "angka", "simbol"]):
                    checklist_issues.append(issue)
                else:
                    special_messages.append(issue)

            for item in checklist_issues:
                self.result_text.insert(tk.END, f"- {item}\n", "issue")
            self.result_text.insert(tk.END, "\n")
            for msg in special_messages:
                self.result_text.insert(tk.END, f"{msg}\n", "special")

            suggestions = checker.suggest_password()
            if suggestions:
                self.result_text.insert(tk.END, "\nSaran password yang lebih kuat:\n", "suggest")
                self.suggestions_text = ""
                for s in suggestions:
                    self.result_text.insert(tk.END, f"  - {s}\n", "suggest")
                    self.suggestions_text += s + "\n"
                self.btn_copy.config(state="normal")
        else:
            self.status_label.config(text="Password kuat!", fg=self.color_success)
            self.result_text.insert(tk.END, "Password sangat kuat! 👍\n", "strong")

        self.result_text.tag_config("issue", foreground=self.color_danger)
        self.result_text.tag_config("special", foreground=self.color_danger, font=self.font_italic)
        self.result_text.tag_config("suggest", foreground=self.color_success)
        self.result_text.tag_config("strong", foreground=self.color_success)

        self.result_text.config(state="disabled")
        self.btn_check.config(state="normal")

if __name__ == "__main__":
    app = AutoPassCheckApp()
    app.mainloop()
