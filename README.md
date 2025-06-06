🔐 AutoPassCheck
AutoPassCheck is a Python-based GUI application for checking password strength and providing improvement suggestions. Built with Tkinter, this app checks password length, character combinations, and compares against popular wordlists like rockyou.txt.

📦 Main Features
✅ Minimum password length check (8 characters)

✅ Detection of uppercase letters, numbers, and special symbols

✅ Check against the rockyou.txt wordlist

✅ Password status indicator (red/yellow/green)

✅ Suggestions for stronger passwords

✅ Dark mode for eye comfort

📥 Installation
🧱 Prerequisites
Python >= 3.6

Tkinter (usually pre-installed)

📦 Linux
bash
Salin
Edit
sudo apt update
sudo apt install python3 python3-tk
🐧 Arch Linux
bash
Salin
Edit
sudo pacman -S python tk
🪟 Windows
Tkinter is typically included with the Python installer.

🚀 How to Run
1. Clone the Repository
bash
Salin
Edit
git clone https://github.com/cimiesyu/autopasscheck.git
cd autopasscheck
2. Create Folder for Wordlist
bash
Salin
Edit
mkdir -p data
3. Download the rockyou.txt Wordlist
bash
Salin
Edit
wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
mv rockyou.txt data/
4. Run the Application
bash
Salin
Edit
python3 autopass_gui.py
🎮 Usage
Enter your password into the input field

Click Check Password

View the security indicator and recommendations below the table

If the password is weak, click Generate New Password to get a strong password suggestion

📂 Project Structure
bash
Salin
Edit
autopasscheck/
├── autopass_gui.py       # Main GUI interface
├── checker.py            # Password checking functions
├── utils.py              # Utilities and password suggestions
├── data/
│   └── rockyou.txt       # Rockyou wordlist
├── README.md
🐛 Example Outputs
🔴 Too short: "Password is too short, minimum 8 characters"

🟡 Missing numbers/symbols/uppercase letters

🟢 Strong password and not found in the wordlist

💡 Tips
Use a mix of uppercase letters, numbers, and unique symbols

Avoid common or leaked passwords

Update your passwords regularly

📜 License
MIT License © 2025 cimiesyu

🤝 Contribution
Pull requests and suggestions are welcome. Please fork, make your changes, then submit a PR!

📬 Contact
For questions or feedback:
📧 Email: cimiesyu@protonmail.com

⚠️ Disclaimer: This tool is for educational and personal security purposes only. Do not use it without permission on others’ systems!

