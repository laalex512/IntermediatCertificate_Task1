import keys
import datetime
import tkinter as tk
from tkinter import messagebox
from print_table import print_table


def filter():
    global filter_window
    global start_year_field, start_month_field, start_day_field, start_hour_field, start_minute_field
    global finish_year_field, finish_month_field, finish_day_field, finish_hour_field, finish_minute_field
    filter_window = tk.Tk()
    filter_window.title("Фильтр")
    filter_window.geometry("780x250")

    # Начало фильтра:
    start_label = tk.Label(
        filter_window, text="Начало Фильтра", font="times 15")
    start_label.grid(row=1, column=0)

    start_year_label = tk.Label(
        filter_window, text="Год", font="times 15")
    start_year_label.grid(row=2, column=1)
    start_year_field = tk.Entry(filter_window, width=20, validate="focusout")
    start_year_field.grid(row=3, column=1)

    start_month_label = tk.Label(
        filter_window, text="Месяц", font="times 15")
    start_month_label.grid(row=2, column=2)
    start_month_field = tk.Entry(filter_window, width=20, validate="focusout")
    start_month_field.grid(row=3, column=2)

    start_day_label = tk.Label(
        filter_window, text="День", font="times 15")
    start_day_label.grid(row=2, column=3)
    start_day_field = tk.Entry(filter_window, width=20, validate="focusout")
    start_day_field.grid(row=3, column=3)

    start_hour_label = tk.Label(
        filter_window, text="Час", font="times 15")
    start_hour_label.grid(row=2, column=4)
    start_hour_field = tk.Entry(filter_window, width=20, validate="focusout")
    start_hour_field.grid(row=3, column=4)

    start_minute_label = tk.Label(
        filter_window, text="Минута", font="times 15")
    start_minute_label.grid(row=2, column=5)
    start_minute_field = tk.Entry(filter_window, width=20, validate="focusout")
    start_minute_field.grid(row=3, column=5)

    # Конец фильтра:
    finish_label = tk.Label(
        filter_window, text="Конец Фильтра", font="times 15")
    finish_label.grid(row=4, column=0)

    finish_year_label = tk.Label(
        filter_window, text="Год", font="times 15")
    finish_year_label.grid(row=5, column=1)
    finish_year_field = tk.Entry(filter_window, width=20, validate="focusout")
    finish_year_field.grid(row=6, column=1)

    finish_month_label = tk.Label(
        filter_window, text="Месяц", font="times 15")
    finish_month_label.grid(row=5, column=2)
    finish_month_field = tk.Entry(filter_window, width=20, validate="focusout")
    finish_month_field.grid(row=6, column=2)

    finish_day_label = tk.Label(
        filter_window, text="День", font="times 15")
    finish_day_label.grid(row=5, column=3)
    finish_day_field = tk.Entry(filter_window, width=20, validate="focusout")
    finish_day_field.grid(row=6, column=3)

    finish_hour_label = tk.Label(
        filter_window, text="Час", font="times 15")
    finish_hour_label.grid(row=5, column=4)
    finish_hour_field = tk.Entry(filter_window, width=20, validate="focusout")
    finish_hour_field.grid(row=6, column=4)

    finish_minute_label = tk.Label(
        filter_window, text="Минута", font="times 15")
    finish_minute_label.grid(row=5, column=5)
    finish_minute_field = tk.Entry(
        filter_window, width=20, validate="focusout")
    finish_minute_field.grid(row=6, column=5)

    # Кнопка отфильтровать:
    but4 = tk.Button(filter_window, width=20, height=2,
                     text="Применить фильтр", command=accept_filter)
    but4.grid(row=7, column=0, padx=10)

    filter_window.mainloop()


def accept_filter():
    try:
        # Преобразовываем введенную инфрмацию в объекты datetime
        pattern_datetime_format = "%Y-%m-%d %H:%M"
        start_date_string = start_year_field.get() + "-" + start_month_field.get() + "-" + \
            start_day_field.get() + " " + start_hour_field.get() + \
            ":" + start_minute_field.get()
        finish_date_string = finish_year_field.get() + "-" + finish_month_field.get() + "-" + \
            finish_day_field.get() + " " + finish_hour_field.get() + \
            ":" + finish_minute_field.get()
        start_date = datetime.datetime.strptime(
            start_date_string, pattern_datetime_format)
        finish_date = datetime.datetime.strptime(
            finish_date_string, pattern_datetime_format)

        filter_window.destroy()

        result_list = []
        pattern_datetime_format = "%Y-%m-%d %H:%M:%S.%f"
        for note in keys.data_from_file:
            current_datetime = datetime.datetime.strptime(
                note["DateTime"], pattern_datetime_format)
            if current_datetime > start_date and current_datetime < finish_date:
                result_list.append(note)
        print_table(result_list)
    except Exception:
        messagebox.showerror("Ошибка", "Ошибка ввода даты или времени!")


# filter()
