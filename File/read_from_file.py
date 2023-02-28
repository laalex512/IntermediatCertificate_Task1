import json
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import keys
from print_table import print_table


def open_file():
    inp = askopenfilename()
    keys.data_from_file = []
    if inp == "":
        return
    try:
        with open(inp, encoding="UTF-8") as f:
            keys.data_from_file = json.loads(f.read())
        print_table(keys.data_from_file)
    except Exception:
        messagebox.showerror("Ошибка", "Не удалось открыть файл")
