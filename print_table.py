from tkinter import ttk
import tkinter as tk
import keys


def print_table(dict):
    my_tree = ttk.Treeview(columns=keys.keys, show="headings")
    my_tree.grid(row=1, column=1)

    for header_unit in keys.keys:
        my_tree.heading(header_unit, text=header_unit)

    my_tree.column("#1", width=40)
    my_tree.column("#2", width=100)
    my_tree.column("#3", width=480)
    my_tree.column("#4", width=160)

    scrollbar = ttk.Scrollbar(orient=tk.VERTICAL, command=my_tree.yview)
    my_tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=2, sticky="ns")
    table = dict_to_list(dict)
    for note in table:
        my_tree.insert("", tk.END, values=note)


def dict_to_list(dict):
    list_to_print = []
    for note in dict:
        list_to_print.append(tuple(note.values()))
    return list_to_print
