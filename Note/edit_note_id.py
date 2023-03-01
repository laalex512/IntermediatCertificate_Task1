import datetime
import tkinter as tk
from tkinter import messagebox
import keys
import print_table


def edit_note_askID():
    global ask_id_window, field_id
    ask_id_window = tk.Tk()
    ask_id_window.title("Редактировать заметку")
    ask_id_window.geometry("250x180")
    
    label_id = tk.Label(ask_id_window, text="Введите ID:", font="times 15")
    label_id.grid(row=1, column=1, pady=10)
    field_id = tk.Entry(ask_id_window, width=30, validate="focusout")
    field_id.grid(row=2, column=1, pady=10)
    
    button_edit = tk.Button(ask_id_window, text="Редактировать",
                            width=30, height=2, command=edit_note_window)
    button_edit.grid(row=3, column=1)
    
    ask_id_window.mainloop()


def edit_note_window():
    global id
    id = int(field_id.get())
    print(id)
    is_exist_note = False
    for note in keys.data_from_file:
        print(note["ID"])
        if id == note["ID"]:
            is_exist_note = True
    if is_exist_note:
        ask_id_window.destroy()
        global note_window, field_name, field_text
        note_window = tk.Tk()
        note_window.title("Редактор заметки")
        note_window.geometry("450x380")

        label_name = tk.Label(note_window, text="Название", font="times 15")
        label_name.grid(row=1, column=1, pady=10)
        label_text = tk.Label(
            note_window, text="Текст Заметки", font="times 15")
        label_text.grid(row=3, column=1, pady=10)
        
        field_name = tk.Entry(
            note_window, width=30, validate="focusout")
        field_name.grid(row=2, column=1, pady=10)
        field_name.insert(0, keys.data_from_file[id-1]["Name"])
        
        field_text = tk.Text(note_window, width=50, height=10)
        field_text.grid(row=4, column=1, pady=10, padx=20)
        field_text.insert("1.0", keys.data_from_file[id-1]["Text"])
        
        button_save = tk.Button(note_window, text="Изменить",
                                width=30, height=2, command=insert_note)
        button_save.grid(row=5, column=1)
        
        note_window.mainloop()
    else:
        messagebox.showerror("Ошибка", "Нет заметки с таким ID")


def insert_note():
    keys.data_from_file[id-1]["Name"] = field_name.get()
    keys.data_from_file[id-1]["Text"] = field_text.get("1.0", "end")
    keys.data_from_file[id-1]["DateTime"] = str(datetime.datetime.now())
    print_table.print_table(keys.data_from_file)
