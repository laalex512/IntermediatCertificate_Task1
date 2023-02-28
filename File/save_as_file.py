import json
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile
import keys


def save_file():
    for note in keys.data_from_file:
        note["DateTime"] = str(note["DateTime"])
    out_line = json.dumps(keys.data_from_file)
    out_file = asksaveasfile(mode="w", defaultextension=".json")
    try:
        out_file.write(out_line.rstrip())
    except Exception:
        messagebox.showerror("Ошибка", "Не удалось сохранить файл")
