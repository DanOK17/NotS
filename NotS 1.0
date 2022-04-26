import os
import sys
import json
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

file_name = NONE


def new_file():
    global file_name
    file_name = "Без названия"
    text.delete('1.0', END)


def save_as():
    out = asksaveasfile(mode="w", defaultextension=".txt")
    data1 = text.get('1.0', END)
    try:
        out.write(data1.rstrip())
    except Exception:
        messagebox.showerror("Ошибка", "Не получилось сохранить файл!")


def open_file():
    global file_name
    root.name_file = askopenfile(mode='r')
    if root.name_file is None:
        return
        file_name = root.name_file.name
    root.data = root.name_file.read()
    text.delete('1.0', END)
    text.insert('1.0', root.data)


def restart_font():
    font_to_restart = str(entry.get())
    if font_to_restart == "":
        messagebox.showerror("Ошибка", "Поле ввода шрифта пусто")
    else:
        text.config(font=font_to_restart)


def autosave():
    way_json = "last.json"
    text_save = text.get('1.0', END)
    with open(way_json, "w") as fk:
        json.dump(text_save, fk, indent=4, ensure_ascii=False)
    root.after(30000 * 1, autosave)


def about():
    window = Toplevel(root)
    window.geometry('620x300')
    fl = open("reference.txt", "r", encoding='utf-8')
    text_obj = fl.read()
    print(text_obj)
    text_widget = Text(window)
    text_widget.insert(1.0, text_obj)
    text_widget.pack(fill=BOTH)
    window.grab_set()


root = Tk()
root.title("Notes")
root.resizable(width=True, height=True)
root.geometry("1200x700")


font = StringVar()


frame_ent = Frame(root, bg="grey")
frame_ent.place(relheight=0.05)

text = Text(root, font=font, width=400, height=300)
text.place(relheight=0.95, relwidth=1.0, rely=0.04)

entry = Entry(frame_ent, textvariable=font, width=600, font=20)
entry.pack(side=TOP)


menu_bar = Menu(root)
file_menu = Menu(menu_bar)
file_menu2 = Menu(menu_bar)
file_menu3 = Menu(menu_bar)

file_menu.add_command(label="Новая заметка", command=new_file)
file_menu.add_command(label="Открыть файл", command=open_file)
file_menu.add_command(label="Сохранить как", command=save_as)
file_menu2.add_command(label="Изменить шрифт", command=restart_font)
file_menu3.add_command(label="Открыть справку", command=about)


menu_bar.add_cascade(label="Файлы", menu=file_menu)
menu_bar.add_cascade(label="Вид", menu=file_menu2)
menu_bar.add_cascade(label="Справка", menu=file_menu3)


way = "last.json"
with open(way, "r") as f:
    insert = json.load(f)
    print(f"{insert}")
text.insert("1.0", insert)


root.config(menu=menu_bar)

autosave()

root.mainloop()
