from tkinter import*
from tkinter import ttk
import sqlite3 as sql
from tkinter import messagebox as mb
from tkinter.filedialog import*
from PIL import Image, ImageTk
import os
from django.core.paginator import Paginator
conn=sql.connect('Hotel.db')
cur=conn.cursor()

rootRoom=Tk()
rootRoom.title("Комнаты")

c = Canvas(rootRoom)

treev=ttk.Treeview(rootRoom)
treev.pack(side='left')

scrlbar = ttk.Scrollbar(rootRoom, orient='vertical', command=treev.yview)
scrlbar.pack(side='right', fill='y')
treev.configure(yscrollcommand=scrlbar.set)

treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

treev['show']='headings'

treev.column("1", width=50, anchor='c')
treev.column("2", width=120, anchor='se')
treev.column("3", width=120, anchor='se')
treev.column("4", width=100, anchor='se')
treev.column("5", width=80, anchor='se')
treev.column("6", width=100, anchor='se')
treev.column("7", width=100, anchor='se')
treev.column("8", width=130, anchor='se')
treev.column("9", width=110, anchor='se')

treev.heading("1", text="Номер комнаты")
treev.heading("2", text="Тип")
treev.heading("3", text="Наличие телефона")
treev.heading("4", text="Мест")
treev.heading("5", text="Цена в сутки")
treev.heading("6", text="Цена за телефон")
treev.heading("7", text="Состояние")
treev.heading("8", text="Бронь")
treev.heading("9", text="Фото")

def view():
    global l, page, p
    cur.execute("Select * from Rooms ")
    obj = cur.fetchall()
    conn.commit()
    p = Paginator(obj, l)
    page = p.page(1)
    treev.delete(*treev.get_children())
    count = page.object_list
    for i in count:
        treev.insert("", 'end', values=i)
    conn.commit()
    cb1.current(0)
    cb2['values']=""

def ph():
    global photo
    imagefile=askopenfile(filetypes=[('JPG images', '.jpg'), ('PNG images', '.png'), ('JPEG images', '.jpg')])
    full_name=os.path.basename(str(imagefile))
    s1=os.path.splitext(full_name)[0]
    s2=os.path.splitext(full_name)[1]
    s=s2.find( "'" )
    photo=s1+s2[0:s]
    print(photo)

def add(h1,h2,h3,h4,h5,h6,h7):
    try:
        cur.execute("INSERT INTO Rooms (RoomID, Type, PhoneRoom, Places, Price_day, Price_phone, Photo) values (?, ?, ?, ?, ?, ?, ?)", (h1,h2,h3,h4,h5,h6,h7))
        conn.commit()
        view()
        new_wnd.destroy()
    except:
        mb.showinfo("Ошибка", "Поля заполнены некорректно")

 
def rmadd():
       
    global new_wnd
    new_wnd=Tk()
    new_wnd.title("Добавление комнаты")

    def dig(*args):
        value1 = var1.get()
        if value1 != "":
            if value1.isdigit()==False:
                mb.showinfo("Ошибка", "Здесь должно быть число")
                e1.delete(0, 'end')
                
        value2 = var2.get()
        if value2 != "":
            if value2.isdigit()==False:
                mb.showinfo("Ошибка", "Здесь должно быть число")
                e2.delete(0, 'end')
                
        value3 = var3.get()
        if value3 != "":
            if value3.isdigit()==False:
                mb.showinfo("Ошибка", "Здесь должно быть число")
                e3.delete(0, 'end')

        value4 = var4.get()
        if value4 != "":
            if value4.isdigit()==False:
                mb.showinfo("Ошибка", "Здесь должно быть число")
                e4.delete(0, 'end') 
            

    var1 = StringVar(new_wnd)
    var1.trace('w', dig)

    var2 = StringVar(new_wnd)
    var2.trace('w', dig)

    var3 = StringVar(new_wnd)
    var3.trace('w', dig)

    var4 = StringVar(new_wnd)
    var4.trace('w', dig)

    
    l1 = Label(new_wnd,text="Номер комнаты").pack(side='top', pady=10, padx=5)
    e1 = Entry(new_wnd, textvariable=var1)
    
    l2 = Label(new_wnd,text="Тип")
    cb1 = ttk.Combobox(new_wnd, values=["Люкс","Полулюкс","Обычный"])
    cb1.current(0)
    
    l3 = Label(new_wnd,text="Телефон в номере")
    cb2 = ttk.Combobox(new_wnd, values=["Нет","Есть"])
    
    l4 = Label(new_wnd,text="Мест")
    e2 = Entry(new_wnd, textvariable=var2)
    
    l5 = Label(new_wnd,text="Стоимость в сутки")
    e3 = Entry(new_wnd, textvariable=var3)
    
    l6 = Label(new_wnd,text="Стоимость за телефон")
    e4 = Entry(new_wnd, textvariable=var4)
    
    btnP = Button(new_wnd,text="Выбор фото", width=10, command=ph)

    

    
    btnAcc = Button(new_wnd, text="Добавить", width=10, command=lambda:add(h1=e1.get(), h2=cb1.get(), h3=cb2.get(), h4=e2.get(), h5=e3.get(), h6=e4.get(), h7=photo))
    e1.pack(side='top', pady=10, padx=5)
    l2.pack(side='top', pady=10, padx=5)
    cb1.pack(side='top', pady=10, padx=5)
    l3.pack(side='top', pady=10, padx=5)
    cb2.pack(side='top', pady=10, padx=5)
    l4.pack(side='top', pady=10, padx=5)
    e2.pack(side='top', pady=10, padx=5)
    l5.pack(side='top', pady=10, padx=5)
    e3.pack(side='top', pady=10, padx=5)
    l6.pack(side='top', pady=10, padx=5)
    e4.pack(side='top', pady=10, padx=5)
    btnP.pack(side='top', pady=10, padx=5)
    btnAcc.pack(side='top', pady=10, padx=5)

    



cb1 = ttk.Combobox(rootRoom, values=['Без фильтрации','По номеру комнаты','По наличию телефона', 'По типу комнаты', 'Бронь', 'Состояние'], state='readonly')
cb1.current(0)
cb2 = ttk.Combobox(rootRoom, state='readonly')

def cb_zap(event):
    if cb1.get()=="По номеру комнаты":
        cur.execute("Select RoomID From Rooms order by RoomID")
        row = cur.fetchall()
        cb2['values']=row
    elif cb1.get()=="По наличию телефона":
        cb2['values']='Есть', 'Нет'
    elif cb1.get()=="По типу комнаты":
        cb2['values']='Обычный', 'Люкс', 'Полулюкс'
    elif cb1.get()=="Бронь":
        cb2['values']='Брони нет', 'Бронь есть'
    elif cb1.get()=="Состояние":
        cb2['values']='Занято', 'Свободно'
    elif cb1.get()=="Без фильтрации":
        cb2['values']=""
        
def select(event):
    c.delete("all")
    it = treev.selection()[0]
    values=treev.item(it, option="values")
    imya=values[8]
    image=loadi(str(imya))
    c.create_image(200,140, image=image)
    rootRoom.mainloop()

def loadi(name):
    img=Image.open(name)
    img.thumbnail((350,350), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img, master=c)

def osv():
    it = treev.selection()[0]
    values=treev.item(it, option="values")
    id_r=values[0]
    answer = mb.askyesno(title="Подтверждение", message="Вы точно хотите изменить статус номера?")
    if answer:
        cur.execute("UPDATE Rooms SET Employment = 'Свободно' Where RoomID = ?;", [str(id_r)])
        conn.commit()
        view()
    rootRoom.mainloop()



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
count = Label(rootRoom)

def count_label():
    global countEnd
    cur.execute("select count(RoomID) from Rooms")
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
    global l, p
    l=cbL.get()
    view()

def delet():
    it = treev.selection()[0]
    values=treev.item(it, option="values")
    id_r=values[0]
    answer = mb.askyesno(title="Подтверждение", message="Вы точно хотите удалить выбранную запись?")
    if answer:
        cur.execute("DELETE FROM Rooms Where RoomID = ?;", [str(id_r)])
        conn.commit()
        view()
    rootRoom.mainloop()


def search(event):
    treev.delete(*treev.get_children())
    if cb1.get()=="По номеру комнаты":
        cur.execute("Select * From Rooms WHERE RoomID = ?", [cb2.get()])
        row = cur.fetchall()
        for i in row:
            treev.insert("", 'end', values=i)
        conn.commit()
    elif cb1.get()=="По наличию телефона":
        cur.execute("Select * From Rooms WHERE PhoneRoom = ?", [cb2.get()])
        row = cur.fetchall()
        for i in row:
            treev.insert("", 'end', values=i)
        conn.commit()
    elif cb1.get()=="По типу комнаты":
        cur.execute("Select * From Rooms WHERE Type = ?", [cb2.get()])
        row = cur.fetchall()
        for i in row:
            treev.insert("", 'end', values=i)
        conn.commit()
    elif cb1.get()=="Бронь":
        cur.execute("Select * From Rooms WHERE Booking = ?", [cb2.get()])
        row = cur.fetchall()
        for i in row:
            treev.insert("", 'end', values=i)
        conn.commit()
    elif cb1.get()=="Состояние":
        cur.execute("Select * From Rooms WHERE Employment = ?", [cb2.get()])
        row = cur.fetchall()
        for i in row:
            treev.insert("", 'end', values=i)
        conn.commit()


All = Button(rootRoom, text="Все", command=view)
All.place(relx=0.4, rely=0.05)
cbL = ttk.Combobox(rootRoom, values=['5', '10','15'], state='readonly')
cbL.current(0)
cbL.bind('<<ComboboxSelected>>', sel)
cbL.place(relx=0.2, rely=0.05)
treev.bind('<<TreeviewSelect>>', select)
#lim=cbL.get()

l=cbL.get()

cb1.bind('<<ComboboxSelected>>', cb_zap)
cb1.place(relx=0.46, rely=0.05)
cb2.bind('<<ComboboxSelected>>', search)
cb2.place(relx=0.57, rely=0.05)
b_left=Button(rootRoom, text="<-", command=left).place(relx=0.15, rely=0.9)
b_right=Button(rootRoom, text="->", command=rigth).place(relx=0.30, rely=0.9)
c.pack(side='top', padx=20, pady=3)
count_label()
view()
count.place(relx=0.04, rely=0.03)
b_add=Button(rootRoom,text="Добавить", command=rmadd).pack(side='left', padx=5, pady=10)

b_remove=Button(rootRoom, text="Освободить", command=osv).pack(side='left', padx=5, pady=10)

b_del=Button(rootRoom, text="Удалить", command=delet).pack(side='left', padx=5, pady=10)
