import os, sys
import json
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile, askopenfilename

file_name = NONE
counter = 0

def new_file():
    global file_name
    file_name = "Без названия"
    text.delete('1.0', END)

def save_as():
    global data
    out = asksaveasfile(mode="w", defaultextension=".txt")
    data = text.get('1.0', END)
    try:
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror("Ошибка", "Не получилось сохранить файл!")
    data2 = text.get('1.0', '1.15')
    new_button = Button(frame_base, text=data2, command=open_name_file)
    new_button.pack(side=TOP, pady=5, padx=5)

def open_file():
    global file_name
    root.name_file = askopenfile(mode='r')
    if root.name_file is None:
        return
        file_name = root.name_file.name
    root.data = root.name_file.read()
    text.delete('1.0', END)
    text.insert('1.0', root.data)
    data2 = text.get('1.0', '1.15')
    new_button = Button(frame_base, text=data2, command=open_name_file)
    new_button.pack(side=TOP, pady=5, padx=5)

def restart_font():
    global font
    font = str(entry.get())
    if font == "":
        messagebox.showerror("Ошибка", "Поле ввода шрифта пусто")
    else:
        text.config(font=font)

def autosave():
    way = "last.json"
    text_save = text.get('1.0', END)
    with open(way, "w") as f:
        json.dump(text_save, f, indent=4, ensure_ascii=False)
    root.after(30000 * 1, autosave)

def open_name_file():
    print(root.name_file)
    with open(name, "r") as fn:
        text.delete('1.0', END)
        text.insert('1.0', root.data)

def about():
    window = Toplevel(root)
    window.geometry('620x300')
    f = open("reference.txt", "r", encoding='utf-8')
    text_obj = f.read()
    print(text_obj)
    text = Text(window)
    text.insert(1.0, text_obj)
    text.pack(fill=BOTH)
    window.grab_set()

root = Tk()
root.title("Notes")
root.resizable(width=True, height=True)
root.geometry("1200x700")


font = StringVar()


frame_ent = Frame(root, bg="grey")
frame_ent.place(relheight=0.05)

text = Text(root, font=font, width=400, height=300)
text.place(relheight=0.9, relwidth=0.90, rely=0.05)

entry = Entry(frame_ent, textvariable=font, width=600, font=20)
entry.pack(side=TOP)

frame_base = Frame(root)
frame_base.place(relheight=0.95, relx=0.9, rely=0.05)

menu_bar = Menu(root)
file_menu = Menu(menu_bar)
file_menu2 = Menu(menu_bar)
second_menu = Menu(file_menu2)

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
