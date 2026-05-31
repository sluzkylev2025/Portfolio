import tkinter as tk
from tkinter import ttk
import psutil

# ================= UPDATE FUNCTION =================

def update_stats():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    # CPU
    cpu_bar["value"] = cpu
    cpu_label.config(text=f"CPU: {cpu}%")
    cpu_label.config(fg=color(cpu))

    # RAM
    ram_bar["value"] = ram
    ram_label.config(text=f"RAM: {ram}%")
    ram_label.config(fg=color(ram))

    # DISK
    disk_bar["value"] = disk
    disk_label.config(text=f"Disk: {disk}%")
    disk_label.config(fg=color(disk))

    root.after(1000, update_stats)

# ================= COLOR LOGIC =================

def color(value):
    if value < 50:
        return "green"
    elif value < 80:
        return "orange"
    else:
        return "red"

# ================= UI =================

root = tk.Tk()
root.title("🖥 System Monitor PRO")
root.geometry("420x320")
root.resizable(False, False)

title = tk.Label(root, text="📊 Монитор системы", font=("Arial", 18, "bold"))
title.pack(pady=10)

# ===== CPU =====
cpu_label = tk.Label(root, text="CPU", font=("Arial", 14))
cpu_label.pack()

cpu_bar = ttk.Progressbar(root, length=300, maximum=100)
cpu_bar.pack(pady=5)

cpu_info = tk.Label(root, text="Процессор — выполняет все вычисления", fg="gray")
cpu_info.pack()

# ===== RAM =====
ram_label = tk.Label(root, text="RAM", font=("Arial", 14))
ram_label.pack(pady=(10,0))

ram_bar = ttk.Progressbar(root, length=300, maximum=100)
ram_bar.pack(pady=5)

ram_info = tk.Label(root, text="ОЗУ — хранит данные запущенных программ", fg="gray")
ram_info.pack()

# ===== DISK =====
disk_label = tk.Label(root, text="Disk", font=("Arial", 14))
disk_label.pack(pady=(10,0))

disk_bar = ttk.Progressbar(root, length=300, maximum=100)
disk_bar.pack(pady=5)

disk_info = tk.Label(root, text="Диск — хранит файлы и систему", fg="gray")
disk_info.pack()

# ================= START =================

update_stats()
root.mainloop()