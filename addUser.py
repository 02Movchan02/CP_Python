from tkinter import*
import sqlite3 as sql
from tkinter import ttk 
from tkinter import messagebox as mb

conn = sql.connect('Hotel.db')
cur=conn.cursor()

rootAddU = Tk()
rootAddU.title("Добавление нового пользователя")

treev=ttk.Treeview(rootAddU, height=30)
treev.pack(side='left')

def upd():
    answer = mb.askyesno(title="Подтверждение", message="Изменить данные?")
    if answer:
        cur.execute("UPDATE Users SET Surname = ?, Name = ?, Passport = ?, Adress = ?, Email = ?, LoginUser = ?, PasswordUser = ?, Post = ? Where UserID = "+Id+"", (e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get(), e7.get(), cb1.get()))
        conn.commit()
        clear()
        view()
    rootAddU.mainloop()
    

b2 = Button(rootAddU, text="Изменить", width=15, state='disabled', command=upd)

isCheck = IntVar()

def show():
    if (isCheck.get() == 0):
        e7['show']='*'
    else:
        e7['show']=""

pcheck = Checkbutton(rootAddU, text="Показать пароль", variable=isCheck, onvalue=1, offvalue=0, command=show)

def ins(event):
    global Id
    try:
        clear()
        b2['state']='normal'
        it = treev.selection() [0]
        values=treev.item(it, option="values")
        Id=values[0]
        e1.insert(0, values[1])
        e2.insert(0, values[2])
        e3.insert(0, values[3])
        e4.insert(0, values[4])
        e5.insert(0, values[5])
        e6.insert(0, values[6])
        e7.insert(0, values[7])
        cb1.insert(0, values[8])
    except:
        mb.showinfo("Внимание!","Для редактирования необходимо выбрать пользователя")
        b2['state']='disable'
    
scrlbar = ttk.Scrollbar(rootAddU, orient='vertical', command=treev.yview)
scrlbar.pack(side='right', fill='y')
treev.configure(yscrollcommand=scrlbar.set)
treev.bind('<Button-3>', ins)

treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

treev['show']='headings'

treev.column("1", width=50, anchor='c')
treev.column("2", width=120, anchor='c')
treev.column("3", width=120, anchor='c')
treev.column("4", width=120, anchor='c')
treev.column("5", width=120, anchor='c')
treev.column("6", width=140, anchor='c')
treev.column("7", width=100, anchor='c')
treev.column("8", width=130, anchor='c')
treev.column("9", width=110, anchor='c')

treev.heading("1", text="ID")
treev.heading("2", text="Фамилия")
treev.heading("3", text="Имя")
treev.heading("4", text="Паспорт")
treev.heading("5", text="Адрес")
treev.heading("6", text="Электронная почта")
treev.heading("7", text="Логин")
treev.heading("8", text="Пароль")
treev.heading("9", text="Должность")

def view():
    treev.delete(*treev.get_children())
    cur.execute("Select * FROM Users")
    count = cur.fetchall()
    for i in count:
        treev.insert("", 'end', values=i)
    conn.commit()
view()

var = StringVar(rootAddU)
l1 = Label(rootAddU, text="Фамилия").pack(side='top', padx=5, pady=5)
e1 = Entry(rootAddU)

e1.pack(side='top', padx=5, pady=5)

l2 = Label(rootAddU, text="Имя").pack(side='top', padx=5, pady=5)
e2 = Entry(rootAddU)

e2.pack(side='top', padx=5, pady=5)

l3 = Label(rootAddU, text="Паспорт").pack(side='top', padx=5, pady=5)
e3 = Entry(rootAddU, textvariable=var)

e3.pack(side='top', padx=5, pady=5)

l4 = Label(rootAddU, text="Адрес").pack(side='top', padx=5, pady=5)
e4 = Entry(rootAddU)

e4.pack(side='top', padx=5, pady=5)

l5 = Label(rootAddU, text="Электронная почта").pack(side='top', padx=5, pady=5)
e5 = Entry(rootAddU)

e5.pack(side='top', padx=5, pady=5)

l6 = Label(rootAddU, text="Логин").pack(side='top', padx=5, pady=5)
e6 = Entry(rootAddU)

e6.pack(side='top', padx=5, pady=5)

l7 = Label(rootAddU, text="Пароль").pack(side='top', padx=5, pady=5)
e7 = Entry(rootAddU)

e7['show']='*'

e7.pack(side='top', padx=5, pady=5)

l8 = Label(rootAddU, text="Должность").pack(side='top', padx=5, pady=5)
cb1 = ttk.Combobox(rootAddU, values=["Админ", "Менеджер"])

cb1.pack(side='top', padx=5, pady=5)

def clear():
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    e4.delete(0, 'end')
    e5.delete(0, 'end')
    e6.delete(0, 'end')
    e7.delete(0, 'end')
    cb1.delete(0, 'end')         

def AddU():
    if ((e1.get() !="") & (e2.get() !="") & (e3.get() !="") & (e4.get() !="") & (e5.get() !="") & (e6.get() !="") & (e7.get() !="") & (cb1.get() !="")):
        try:
            cur.execute("INSERT INTO Users (Surname, Name, Passport, Adress, Email, LoginUser, PasswordUser, Post) values (?,?,?,?,?,?,?,?)", (e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get(), e7.get(), cb1.get()))
            conn.commit()
            view()
        except:
            mb.showinfo("Ошибка", "Проверьте, все ли поля заполнены")
    else:
        mb.showinfo("Ошибка", "Проверьте, все ли поля заполнены")

b1 = Button(rootAddU, text="Добавить", width=15, command=AddU).pack(side='top', padx=5, pady=10)

b2.pack(side='top', padx=5, pady=10)

pcheck.pack(side='top', padx=5, pady=10)
