import datetime
import tkinter as tk
from tkinter import messagebox
import keys
import print_table


def delete_note_askID():
    global ask_id_window, field_id
    ask_id_window = tk.Tk()
    ask_id_window.title("Удалить заметку")
    ask_id_window.geometry("250x180")
    label_id = tk.Label(ask_id_window, text="Введите ID:", font="times 15")
    label_id.grid(row=1, column=1, pady=10)
    field_id = tk.Entry(ask_id_window, width=30, validate="focusout")
    field_id.grid(row=2, column=1, pady=10)
    button_edit = tk.Button(ask_id_window, text="Удалить",
                            width=30, height=2, command=delete_note)
    button_edit.grid(row=3, column=1)
    ask_id_window.mainloop()


def delete_note():
    global id
    id = int(field_id.get())
    is_exist_note = False
    for note in keys.data_from_file:
        if id == note["ID"]:
            is_exist_note = True
    if is_exist_note:
        ask_id_window.destroy()
        keys.data_from_file.pop(id-1)
        messagebox.showinfo("Успешно", "Заметка удалена")
    else:
        messagebox.showerror("Ошибка", "Нет заметки с таким ID")
    print_table.print_table(keys.data_from_file)
