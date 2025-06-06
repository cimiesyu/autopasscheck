# 🔐 AutoPassCheck

AutoPassCheck is a Python-based GUI application for checking password strength and providing improvement suggestions. Built with Tkinter, this app checks password length, character combinations, and compares against popular wordlists like **rockyou.txt**.

## 📦 Main Features  
- ✅ Minimum password length check (8 characters)  
- ✅ Detection of uppercase letters, numbers, and special symbols  
- ✅ Check against the rockyou.txt wordlist  
- ✅ Password status indicator (red/yellow/green)  
- ✅ Suggestions for stronger passwords  
- ✅ Dark mode for eye comfort  

## 📥 Installation

### 🧱 Prerequisites  
- Python >= 3.6  
- Tkinter (usually pre-installed)  

### 🖥️ Installation commands

```bash
# For Debian/Ubuntu
sudo apt update && sudo apt install python3 python3-tk

# For Arch Linux
sudo pacman -S python tk
```

🚀 How to Run

```bash
git clone https://github.com/cimiesyu/autopasscheck.git
cd autopasscheck
mkdir -p data
wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
mv rockyou.txt data/
python3 autopasscheck.py
```

📂 Project Structure

![image](https://github.com/user-attachments/assets/3f6c0db3-f3e9-4cb5-a775-d14170f554f7)





🐛 Example Outputs

![image](https://github.com/user-attachments/assets/3ba504d4-2798-4752-8ca6-6a51c2e190e7)



📜 License
MIT License © 2025 cimiesyu

🤝 Contribution
Pull requests and suggestions are welcome. Please fork, make your changes, then submit a PR!

⚠️ Disclaimer: This tool is for educational and personal security purposes only. Do not use it without permission on others’ systems!

