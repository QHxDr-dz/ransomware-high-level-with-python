🔐 Ransomware Simulation (Educational Use Only)

    ⚠️ Disclaimer:
    This script is for educational and ethical testing in controlled environments only.
    Do NOT use this tool on systems or files you do not own or have explicit permission to test.
    The misuse of this code can be illegal and unethical. The author assumes no responsibility for any damages caused.

📘 Description

This script simulates basic ransomware behavior. It encrypts files inside a specified directory and displays a fullscreen message demanding a payment with a BTC address and a code entry to unlock the files.

It is designed as a learning exercise for cybersecurity students and malware analysts to study:

    File encryption with Python using cryptography.Fernet

    Fullscreen GUI overlays with Tkinter

    Input blocking via Windows API

    Ransomware-style user interaction

⚙️ How It Works

    Target Directory:
    All files inside ~/Desktop/test are encrypted using Fernet symmetric encryption. You can change this path in the TARGET_DIR variable.

    Key Storage:
    A secret encryption key is stored in a file (keyfile.txt) on the desktop unless it already exists.

    Encryption & Decryption:

        If the keyfile.txt does not exist, the script encrypts all files in the target directory.

        If the keyfile.txt exists, the GUI launches immediately and asks for a decryption code.

    GUI Ransom Window:
    A fullscreen black window appears showing a ransom note. It blocks:

        Task switching (Alt+Tab)

        Closing via Alt+F4 or Escape

        Task Manager (partially, via input blocking)

    Unlock Mechanism:
    Entering the correct code (1 in this example) decrypts all files and removes the key.

📂 File Structure

.
├── network_locker.py
└── ~/Desktop/
    └── test/                # <-- All files inside will be encrypted
    └── keyfile.txt          # <-- The encryption key

🧪 Running

python3 network_locker.py

    ⚠️ On Windows, this script attempts to block user input temporarily using ctypes.

🔒 Used Libraries

    cryptography: For symmetric encryption using Fernet

    tkinter: To create the fullscreen ransom note interface

    ctypes: To interact with the Windows API for blocking input (only works on Windows)

    os: For filesystem operations

💡 Educational Takeaways

    How ransomware encrypts and locks user files

    Importance of restricting access to sensitive folders

    Defensive programming against unauthorized file changes

    How to create a controlled, simulated ransomware for malware analysis labs
