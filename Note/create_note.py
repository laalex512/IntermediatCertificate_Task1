import datetime
import tkinter as tk
import keys
import print_table


def create():
    global note_window, field_name, field_text
    note_window = tk.Tk()
    note_window.title("Новая заметка")
    note_window.geometry("450x380")

    label_name = tk.Label(note_window, text="Название", font="times 15")
    label_name.grid(row=1, column=1, pady=10)
    label_text = tk.Label(note_window, text="Текст Заметки", font="times 15")
    label_text.grid(row=3, column=1, pady=10)
    field_name = tk.Entry(note_window, width=30, validate="focusout")
    field_name.grid(row=2, column=1, pady=10)
    field_text = tk.Text(note_window, width=50, height=10)
    field_text.grid(row=4, column=1, pady=10, padx=20)
    button_save = tk.Button(note_window, text="Добавить",
                            width=30, height=2, command=insert_note)
    button_save.grid(row=5, column=1)
    note_window.mainloop()


def insert_note():
    current_note = {}
    current_note["ID"] = len(keys.data_from_file)+1
    current_note["Name"] = field_name.get()
    current_note["Text"] = field_text.get("1.0", "end")
    current_note["DateTime"] = str(datetime.datetime.now())
    keys.data_from_file.append(current_note)
    print(keys.data_from_file)
    print_table.print_table(keys.data_from_file)
