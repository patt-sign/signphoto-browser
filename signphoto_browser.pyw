import tkinter as tk
from tkinter import PhotoImage
import webview
import threading
import subprocess
import time
import os

# --- KONFIGURACJA ---
URL = "https://signphoto.pl"
EMAIL = "marekpatt@googlemail.com"

# Funkcja naprawy DNS (ukrywa CMD)
def fix_dns():
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    subprocess.run("ipconfig /flushdns", startupinfo=si)
    subprocess.run('netsh interface ip set dns name="Wi-Fi" static 8.8.8.8', startupinfo=si)
    subprocess.run('netsh interface ip add dns name="Wi-Fi" 8.8.4.4 index=2', startupinfo=si)

# Test połączenia DNS
def test_connection():
    try:
        subprocess.check_output("nslookup signphoto.pl 8.8.8.8", shell=True, stderr=subprocess.DEVNULL)
        return True
    except:
        return False

# Buduje i wyświetla główne okno
def main_gui():
    root = tk.Tk()
    root.title("SignPhoto – dostęp")
    root.geometry("500x320")
    root.resizable(False, False)
    try:
        root.iconbitmap("przeico.ico")
    except:
        pass

    # Gradient w tle: od #e6f7ff (jasny błękit) do  (pistacja)
    canvas = tk.Canvas(root, width=500, height=320, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    h = 320
    r1, g1, b1 = 230, 247, 255   # początek (#e6f7ff)
    r2, g2, b2 = 212, 244, 221   # koniec   (#d3d3d3)
    for i in range(h):
        t = i / (h - 1)
        r = int(r1 + t * (r2 - r1))
        g = int(g1 + t * (g2 - g1))
        b = int(b1 + t * (b2 - b1))
        color = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_line(0, i, 500, i, fill=color)

    # Logo w rogu
    try:
        logo = PhotoImage(file="logos.png")
        canvas.create_image(10, 10, anchor="nw", image=logo)
        root.logo = logo
    except:
        pass

    # Status (przesunięty w prawo)
    status = canvas.create_text(
        320, 80,
        text="Sprawdzam połączenie…",
        font=("Segoe UI", 16, "bold"),
        fill="#003366",
        justify="center"
    )

    # Przycisk Napraw połączenie
    def on_fix():
        btn_fix.config(state="disabled")
        canvas.itemconfig(status, text="Naprawiam połączenie…")
        threading.Thread(target=background_fix, daemon=True).start()

    btn_fix = tk.Button(
        root, text="Napraw połączenie", font=("Segoe UI", 12),
        bg="#ffd966", fg="#333333", relief="raised", command=on_fix
    )
    canvas.create_window(150, 200, window=btn_fix, width=160, height=40)

    # Przycisk Otwórz Signphoto
    def on_open():
        root.destroy()
        webview.create_window("SignPhoto", URL, width=1024, height=768, resizable=True)
        webview.start(gui='tkinter')

    btn_open = tk.Button(
        root, text="Otwórz Signphoto", font=("Segoe UI", 12),
        bg="#8fd14f", fg="white", relief="raised", state="disabled", command=on_open
    )
    canvas.create_window(350, 200, window=btn_open, width=160, height=40)

    # W tle: automatyczny test i ewentualna naprawa DNS
    def background_fix():
        fix_dns()
        time.sleep(1)
        if test_connection():
            canvas.itemconfig(
                status,
                text="✅ Połączenie OK\nmożesz otworzyć Signphoto"
            )
            btn_open.config(state="normal")
        else:
            canvas.itemconfig(status, text="❌ Problem z połączeniem. Spróbuj ponownie.")
            btn_fix.config(state="normal")

    threading.Thread(target=background_fix, daemon=True).start()
            # ====== DODAJ TO NA DOLE FUNKCJI main_gui(), PRZED root.mainloop() ======
    copyright_label = tk.Label(
        root, text="© 2025 Marek Patt dla Signphoto",
        font=("Segoe UI", 8), fg="#666666", bg=None
    )
    copyright_label.place(x=10, y=300)  # na dole z lewej strony
    root.mainloop()

if __name__ == "__main__":
    main_gui()
