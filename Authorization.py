from tkinter import*
import sqlite3 as sql
from tkinter import messagebox as mb
from tkinter import ttk

conn=sql.connect('Hotel.db')
cur=conn.cursor()

rootLog = Tk()
rootLog.geometry('190x300')
rootLog.title("Авторизация")

l1 = Label(rootLog, text="Логин").pack(pady=10)
e1 = Entry(rootLog)

l2 = Label(rootLog, text="Пароль")

e2 = Entry(rootLog, show='*')

cb1 = ttk.Combobox(rootLog, values=["Админ", "Менеджер"], state='readonly')

def cli(): 
    log = e1.get()
    pas = e2.get()
    cur.execute("Select LoginUser, PasswordUser, Post From Users Where LoginUser =?;", [log])
    row=cur.fetchone()
    try:
        if ((str(row[0])==log) & (str(row[1])==pas) & (str(row[2])=="Админ")):
            if (str(row[2])==cb1.get()):
                rootLog.destroy()
                import MainFormAdmin
            else:
                mb.showinfo("Ошибка", "У вас нет доступа")
        elif ((str(row[0])==log) & (str(row[1])==pas) & (str(row[2])=="Менеджер")):
            if (str(row[2])==cb1.get()):
                rootLog.destroy()
                import MainFormMan
            else:
                mb.showinfo("Ошибка", "У вас нет доступа")
        else:
            mb.showinfo("Ошибка", "Вы ввели неправильный логин или пароль")
                
    except:
        mb.showinfo("Ошибка", "Вы не правильно ввели логин или пароль")
e1.pack(pady=10)
l2.pack(pady=10)
e2.pack(pady=10)
l3 = Label(rootLog, text="Должность").pack(pady=10)
cb1.pack(pady=10)
b1 = Button(rootLog, text="Вход", width=10, command=cli).pack(pady=10)
