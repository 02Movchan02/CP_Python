from tkinter import*
import sqlite3 as sql
from tkinter import messagebox as mb

conn=sql.connect('Hotel.db')
cur=conn.cursor()

rootLog = Tk()

l1 = Label(rootLog, text="Логин").place(relx=0.4, rely=0.1)
e1 = Entry(rootLog)

l2 = Label(rootLog, text="Пароль")

e2 = Entry(rootLog, show='*')

def cli():
    log = e1.get()
    pas = e2.get()
    cur.execute("Select LoginUser, PasswordUser, Post From Users Where LoginUser =?;", [log])
    row=cur.fetchone()
    try:
        if ((str(row[0])==log) & (str(row[1])==pas)):
            if (str(row[2])=="Админ"):
                rootLog.destroy()
                import MainFormAdmin
            elif (str(row[2])=="Менеджер"):
                rootLog.destroy()
                import MainFormMan
        else:
            mb.showinfo("Ошибка", "Вы не правильно ввели логин или пароль")
    except:
        mb.showinfo("Ошибка", "Вы не правильно ввели логин или пароль")
e1.place(relx=0.2, rely=0.25)
l2.place(relx=0.4, rely=0.4)
e2.place(relx=0.2, rely=0.55)
b1 = Button(rootLog, text="Вход", width=10, command=cli).place(relx=0.3, rely=0.7)
