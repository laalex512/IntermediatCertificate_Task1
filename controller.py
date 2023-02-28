import tkinter as tk
from print_table import print_table
import keys

import File.read_from_file as read_from_file
import File.save_as_file as save_as_file
import File.new_file as new_file

import Note.create_note as create_note
import Note.edit_note_id as edit_note_id
import Note.delete_note_id as delete_note_id

import Filter.filter_note as filter_note


def start():
    global window
    window = tk.Tk()
    window.title("Заметки")
    window.geometry("800x300")

    # Создаем меню:
    menu_bar = tk.Menu(window)
    file_menu = tk.Menu(menu_bar, tearoff=0)

    menu_bar.add_cascade(label="Файл", menu=file_menu)
    file_menu.add_command(label="Новый файл", command=new_file.create)
    file_menu.add_command(label="Открыть файл",
                          command=read_from_file.open_file)
    file_menu.add_command(label="Сохранить файл как...",
                          command=save_as_file.save_file)

    edit_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Заметки", menu=edit_menu)
    edit_menu.add_command(label="Создать новую", command=create_note.create)
    edit_menu.add_command(label="Редактировать существующую",
                          command=edit_note_id.edit_note_askID)
    edit_menu.add_command(label="Удалить существующую",
                          command=delete_note_id.delete_note_askID)

    filter_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Фильтр", menu=filter_menu)
    filter_menu.add_command(label="Фильтровать по дате",
                            command=filter_note.filter)
    filter_menu.add_command(label="Отменить фильтр",
                            command=lambda: print_table(keys.data_from_file))
    window.config(menu=menu_bar)

    # Сразу выводим пустую таблицу
    print_table(())

    window.mainloop()



