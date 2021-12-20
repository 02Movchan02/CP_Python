from tkinter import*
from tkinter import ttk
import sqlite3 as sql
from django.core.paginator import Paginator
from tkinter import messagebox as mb

conn=sql.connect('Hotel.db')
cur=conn.cursor()

rootClient=Tk()
rootClient.title("Клиенты")

treev=ttk.Treeview(rootClient)
treev.pack(side='left', pady=40)

scrlbar = ttk.Scrollbar(rootClient, orient='vertical', command=treev.yview)
scrlbar.pack(side='left', fill='y')
treev.configure(yscrollcommand=scrlbar.set)

treev["columns"] = ("1", "2", "3", "4", "5", "6")

treev['show']='headings'

treev.column("1", width=50, anchor='c')
treev.column("2", width=100, anchor='se')
treev.column("3", width=100, anchor='se')
treev.column("4", width=100, anchor='se')
treev.column("5", width=80, anchor='se')
treev.column("6", width=120, anchor='c')

treev.heading("1", text="Номер клиента")
treev.heading("2", text="Фамилия")
treev.heading("3", text="Имя")
treev.heading("4", text="Отчество")
treev.heading("5", text="Паспорт")
treev.heading("6", text="Номер телефона")

def view():
    global l, page, p
    treev.delete(*treev.get_children())
    cur.execute("Select * FROM Clients")
    obj=cur.fetchall()
    conn.commit()
    p = Paginator(obj, l)
    page = p.page(1)
    count = page.object_list
    for i in count:
        treev.insert("", 'end', values=i)
    conn.commit()

def addC(h1,h2,h3,h4,h5):
    if ((h1 !="") & (h2 !="") & (h3 !="") & (h4 !="") & (h5 !="")):
        try:
            cur.execute("Insert into Clients (Surname, Name, Middle_name, Passport, Phone) values (?,?,?,?,?);", (h1,h2,h3,h4,h5))
            conn.commit()
            view()
            rootAddC.destroy()
        except:
            mb.showinfo("Ошибка!", "Проверьте корректность данных")
    else:
        mb.showinfo("Ошибка!", "Введите данные")

def viewAddForm():
    global rootAddC
    rootAddC = Tk()
    rootAddC.title("Добавление")
    l1 = Label(rootAddC, text="Фамилия")
    e1 = Entry(rootAddC)

    l2=Label(rootAddC, text="Имя")
    e2=Entry(rootAddC)

    l3=Label(rootAddC, text="Отчество")
    e3=Entry(rootAddC)

    l4=Label(rootAddC, text="Номер паспорта")
    e4=Entry(rootAddC)
    
    l5=Label(rootAddC, text="Телефон")
    e5=Entry(rootAddC)
    
    l1.pack(side='top', padx=5, pady=5)
    e1.pack(side='top', padx=5, pady=5)
    l2.pack(side='top', padx=5, pady=5)
    e2.pack(side='top', padx=5, pady=5)
    l3.pack(side='top', padx=5, pady=5)
    e3.pack(side='top', padx=5, pady=5)
    l4.pack(side='top', padx=5, pady=5)
    e4.pack(side='top', padx=5, pady=5)
    l5.pack(side='top', padx=5, pady=5)
    e5.pack(side='top', padx=5, pady=5)
    
    btnAddC = Button(rootAddC, text="Добавить", command=lambda:addC(h1=e1.get(), h2=e2.get(), h3=e3.get(), h4=e4.get(), h5=e5.get()))
    btnAddC.pack(side='top', padx=5, pady=5)
orde = ""
usl = ""
def sort(event):
    global orde, page, p, usl
    if cb1.get()=="В алфавитном порядке":
        if cbSch.get()=="Все":
            treev.delete(*treev.get_children())
            cur.execute("Select * FROM Clients order by ClientID")
            obj=cur.fetchall()
            conn.commit()
            p = Paginator(obj, l)
            page = p.page(1)
            count = page.object_list
            for i in count:
                treev.insert("", 'end', values=i)
            conn.commit()
            orde = "order by Surname"
        else:
            treev.delete(*treev.get_children())
            cur.execute("Select * FROM Clients Where "+usl+" LIKE ? order by "+usl+"", ('{}%'.format(entrS.get()),))
            obj=cur.fetchall()
            conn.commit()
            p = Paginator(obj, l)
            page = p.page(1)
            count = page.object_list
            for i in count:
                treev.insert("", 'end', values=i)
            conn.commit()
            orde = "order by Surname"
    elif cb1.get()=="Не в алфавитном порядке":
        if cbSch.get()=="Все":
            treev.delete(*treev.get_children())
            cur.execute("Select * FROM Clients order by ClientID desc")
            obj=cur.fetchall()
            conn.commit()
            p = Paginator(obj, l)
            page = p.page(1)
            count = page.object_list
            for i in count:
                treev.insert("", 'end', values=i)
            conn.commit()
            orde = "order by Surname desc"
        else:
            orde="order by Surname desc"
            treev.delete(*treev.get_children())
            cur.execute("Select * FROM Clients Where "+usl+" LIKE ? order by "+usl+" desc", ('{}%'.format(entrS.get()),))
            obj=cur.fetchall()
            conn.commit()
            p = Paginator(obj, l)
            page = p.page(1)
            count = page.object_list
            for i in count:
                treev.insert("", 'end', values=i)
            conn.commit()
    elif cb1.get()=="Без сортировки":
        view()

frame = LabelFrame(rootClient, text="Поиск")

cbSch = ttk.Combobox(frame, state='readonly', values=['Все','По Фамилии', 'По Имени', 'По Отчеству', 'По Паспорту', 'По Номеру телефона'])
cbSch.current(0)

def search(*args):
    global orde, usl
    value=var.get()
    if cbSch.get()=="По Фамилии":
        cur.execute("select * from Clients Where Surname Like ? "+orde,('{}%'.format(entrS.get()),))
        obj=cur.fetchall()
        conn.commit()
        p = Paginator(obj, l)
        page = p.page(1)
        al = page.object_list
        treev.delete(*treev.get_children())
        for i in al:
            treev.insert("", 'end', values=i)
        usl = "Surname"
    elif cbSch.get()=="По Имени":
        cur.execute("select * from Clients Where Name Like ?"+orde,('{}%'.format(entrS.get()),))
        obj=cur.fetchall()
        conn.commit()
        p = Paginator(obj, l)
        page = p.page(1)
        al = page.object_list
        treev.delete(*treev.get_children())
        for i in al:
            treev.insert("", 'end', values=i)
        usl = "Name"
    elif cbSch.get()=="По Отчеству":
        cur.execute("select * from Clients Where Middle_name Like ?"+orde,('{}%'.format(entrS.get()),))
        obj=cur.fetchall()
        conn.commit()
        p = Paginator(obj, l)
        page = p.page(1)
        al = page.object_list
        treev.delete(*treev.get_children())
        for i in al:
            treev.insert("", 'end', values=i)
        usl = "Middle_name"
    elif cbSch.get()=="По Паспорту":
        cur.execute("select * from Clients Where Passport Like ?"+orde,('{}%'.format(entrS.get()),))
        obj=cur.fetchall()
        conn.commit()
        p = Paginator(obj, l)
        page = p.page(1)
        al = page.object_list
        treev.delete(*treev.get_children())
        for i in al:
            treev.insert("", 'end', values=i)
        usl = "Passport"
    elif cbSch.get()=="По Номеру телефона":
        cur.execute("select * from Clients Where Phone Like ?"+orde,('{}%'.format(entrS.get()),))
        obj=cur.fetchall()
        conn.commit()
        p = Paginator(obj, l)
        page = p.page(1)
        al = page.object_list
        treev.delete(*treev.get_children())
        for i in al:
            treev.insert("", 'end', values=i)
        usl = "Phone"
var=StringVar(rootClient)
var.trace('w', search)


def left():
    global page, p
    if page.has_previous()==True:
        nump = page.previous_page_number()
        page = p.page(nump)
        treev.delete(*treev.get_children())
        count = page.object_list
        for i in count:
            treev.insert("", 'end', values=i)
        conn.commit()
    else:
        mb.showinfo("Внимание", "Больше назад нельзя")
count = Label(rootClient)

def count_label():
    global countEnd
    cur.execute("select count(ClientID) from Clients")
    counEnd = cur.fetchone()
    conn.commit()
    count['text']="Всего "+str(counEnd[0]) +" записей"

def rigth():
    global page, p
    if page.has_next()==True:
        nump = page.next_page_number()
        page = p.page(nump)
        treev.delete(*treev.get_children())
        count = page.object_list
        for i in count:
            treev.insert("", 'end', values=i)
        conn.commit()
    else:
        mb.showinfo("Внимание", "Дальше нет страниц")

def sel(event):
    global lim, l
    lim=cbL.get()
    l=cbL.get()
    view()
entrS = Entry(frame, textvariable=var)

def upd(h1,h2,h3,h4,h5):
    answer = mb.askyesno(title="Подтверждение", message="Изменить данные?")
    if answer:
        cur.execute("UPDATE Clients SET Surname = ?, Name = ?, Middle_name = ?, Passport = ?, Phone = ? Where ClientID = "+Id+"", (h1,h2,h3,h4,h5))
        conn.commit()
        view()
        mb.showinfo("Успешно!", "Данные изменены")
        new.destroy()

def ins(event):
    global new, Id
    try:
        it = treev.selection()[0]
        values=treev.item(it, option="values")
        Id=values[0]
        new=Tk()
        l1 = Label(new, text="Фамилия").pack(side='top', padx=5, pady=5)
        e1 = Entry(new)

        e1.pack(side='top', padx=5, pady=5)

        l2 = Label(new, text="Имя").pack(side='top', padx=5, pady=5)
        e2 = Entry(new)

        e2.pack(side='top', padx=5, pady=5)

        l3 = Label(new, text="Отчество").pack(side='top', padx=5, pady=5)
        e3 = Entry(new, textvariable=var)

        e3.pack(side='top', padx=5, pady=5)

        l4 = Label(new, text="Паспорт").pack(side='top', padx=5, pady=5)
        e4 = Entry(new)

        e4.pack(side='top', padx=5, pady=5)

        l5 = Label(new, text="Номер телефона").pack(side='top', padx=5, pady=5)
        e5 = Entry(new)

        e5.pack(side='top', padx=5, pady=5)

        bAcc = Button(new, text="Изменить", command=lambda:upd(h1=e1.get(), h2=e2.get(), h3=e3.get(), h4=e4.get(), h5=e5.get())).pack(side='top', padx=5, pady=10)

        e1.insert(0, values[1])
        e2.insert(0, values[2])
        e3.insert(0, values[3])
        e4.insert(0, values[4])
        e5.insert(0, values[5])
     
    except:
        mb.showinfo("Внимание!", "Сначала необходимо выбрать клиента")
        

treev.bind('<Button-3>', ins)

b_left=Button(rootClient, text="<-", command=left).place(relx=0.15, rely=0.9)
b_right=Button(rootClient, text="->", command=rigth).place(relx=0.30, rely=0.9)

cb1 = ttk.Combobox(rootClient, state='readonly', values=['Без сортировки', 'В алфавитном порядке', 'Не в алфавитном порядке'])
cb1.current(0)
cb1.pack(side='top', padx=5, pady=5)

count_label()
count.place(relx=0.04, rely=0.04)
cbL = ttk.Combobox(rootClient, values=['5', '10','15'], state='readonly')
cbL.current(0)
cbL.bind('<<ComboboxSelected>>', sel)
cbL.place(relx=0.2, rely=0.05)

l=cbL.get()

lim=cbL.get()

cb1.bind('<<ComboboxSelected>>', sort)
cbSch.bind('<<ComboboxSelected>>', search)
cbSch.pack(side='top', padx=5, pady=5)
entrS.pack(side='top', padx=5, pady=5)
frame.pack(side='top', padx=5,pady=5)
btnAdd = Button(rootClient, text="Добавить", command=viewAddForm).pack(side='top', padx=5, pady=5)
view()
