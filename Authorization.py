from tkinter import*
import sqlite3 as sql
from tkinter import messagebox as mb
from tkinter import ttk

conn=sql.connect('Hotel.db')
cur=conn.cursor()

rootLog = Tk()
rootLog.geometry('190x300')
rootLog.title("Авторизация")

LabelLogin = Label(rootLog, text="Логин").pack(pady=10)
EntryLogin = Entry(rootLog)

LabelPassword = Label(rootLog, text="Пароль")

EntryPassword = Entry(rootLog, show='*')

ComboboxPost = ttk.Combobox(rootLog, values=["Админ", "Менеджер"], state='readonly')

def EntranceUser(): 
    log = EntryLogin.get()
    pas = EntryPassword.get()
    cur.execute("Select LoginUser, PasswordUser, Post From Users Where LoginUser =?;", [log])
    row=cur.fetchone()
    try:
        if ((str(row[0])==log) & (str(row[1])==pas) & (str(row[2])=="Админ")):
            if (str(row[2])==ComboboxPost.get()):
                rootLog.destroy()
                import MainFormAdmin
            else:
                mb.showinfo("Ошибка", "У вас нет доступа")
        elif ((str(row[0])==log) & (str(row[1])==pas) & (str(row[2])=="Менеджер")):
            if (str(row[2])==ComboboxPost.get()):
                rootLog.destroy()
                import MainFormMan
            else:
                mb.showinfo("Ошибка", "У вас нет доступа")
        else:
            mb.showinfo("Ошибка", "Вы ввели неправильный логин или пароль")
                
    except:
        mb.showinfo("Ошибка", "Вы не правильно ввели логин или пароль")
EntryLogin.pack(pady=10)
LabelPassword.pack(pady=10)
EntryPassword.pack(pady=10)
LabelPost = Label(rootLog, text="Должность").pack(pady=10)
ComboboxPost.pack(pady=10)
ButtonIn = Button(rootLog, text="Вход", width=10, command=EntranceUser).pack(pady=10)
