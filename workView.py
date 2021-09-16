from tkinter import*
from tkinter import ttk
from tkinter import messagebox as mb
import sqlite3 as sql

conn=sql.connect('Hotel.db')
cur=conn.cursor()

rootView = Tk()
rootView.title("Просмотр аренды")

treev=ttk.Treeview(rootView)
treev.pack(side='left', pady=45)

scrlbar = ttk.Scrollbar(rootView, orient='vertical', command=treev.yview)
scrlbar.pack(side='right', fill='y')
treev.configure(yscrollcommand=scrlbar.set)

treev["columns"] = ("1", "2", "3", "4", "5")

treev['show']='headings'

treev.column("1", width=110, anchor='c')
treev.column("2", width=120, anchor='c')
treev.column("3", width=120, anchor='c')
treev.column("4", width=120, anchor='se')
treev.column("5", width=100, anchor='se')

treev.heading("1", text="Номер комнаты")
treev.heading("2", text="Номер клиента")
treev.heading("3", text="Количество дней")
treev.heading("4", text="Статус")
treev.heading("5", text="К оплате")


def view():
    treev.delete(*treev.get_children())
    cur.execute("Select RoomNum, ClientNum, Duration_of_Days, Status, Payment FROM Work order by RoomNum Limit ?", [lim])
    count = cur.fetchall()
    for i in count:
        treev.insert("", 'end', values=i)
    conn.commit()
frame = LabelFrame(rootView, text='Поиск')
cbS = ttk.Combobox(frame, values=['Все','По Номеру комнаты', 'По Номеру клиента', 'По Количеству дней', 'К оплате'], state='readonly')
cbS.current(0)

def select(event):
    global stat, id_room
    it = treev.selection()[0]
    values=treev.item(it, option="values")
    id_room=values[0]
    stat = values[3]
    rootView.mainloop()

treev.bind('<<TreeviewSelect>>', select)

def search(*args):
    value=var.get()
    if cbS.get()=="По Номеру комнаты":
        cur.execute("select RoomNum, ClientNum, Duration_of_Days, Status, Payment from Work Where RoomNum Like ?",('{}%'.format(entrS.get()),))
        al = cur.fetchall()
        treev.delete(*treev.get_children())
        for i in al:
            treev.insert("", 'end', values=i)
    elif cbS.get()=="По Номеру клиента":
        cur.execute("select RoomNum, ClientNum, Duration_of_Days, Status, Payment from Work Where ClientNum Like ?",('{}%'.format(entrS.get()),))
        al = cur.fetchall()
        treev.delete(*treev.get_children())
        for i in al:
            treev.insert("", 'end', values=i)
    elif cbS.get()=="По Количеству дней":
        cur.execute("select RoomNum, ClientNum, Duration_of_Days, Payment from Work Where Duration_of_Days Like ?",('{}%'.format(entrS.get()),))
        al = cur.fetchall()
        treev.delete(*treev.get_children())
        for i in al:
            treev.insert("", 'end', values=i)
    elif cbS.get()=="К оплате":
        cur.execute("select RoomNum, ClientNum, Duration_of_Days, Status, Payment from Work Where Payment Like ?",('{}%'.format(entrS.get()),))
        al = cur.fetchall()
        treev.delete(*treev.get_children())
        for i in al:
            treev.insert("", 'end', values=i)
var=StringVar(rootView)
var.trace('w', search)

def retu():
    global stat, id_room
    if (stat=="Не оплачено"):
        answer = mb.askyesno(title="Подтверждение", message="Вы действительно хотите оплатить эту бронь?")
        if answer:
            cur.execute("UPDATE Work SET Status = 'Оплачено' Where RoomNum =?;", [str(id_room)])
            conn.commit()
            view()
    else:
        answer = mb.showinfo(title="Предупреждение", message="Эта бронь уже оплачена")


def left():
    global lim, l
    if int(lim) >5:
        lim=int(lim)-int(l)
        treev.delete(*treev.get_children())
        cur.execute("Select * FROM Work order by RoomNum Limit ? ", [lim])
        count = cur.fetchall()
        for i in count:
            treev.insert("", 'end', values=i)
        conn.commit()
    
count = Label(rootView)

def count_label():
    global countEnd
    cur.execute("select count(RoomNum) from Work")
    counEnd = cur.fetchone()
    conn.commit()
    count['text']="Всего "+str(counEnd[0]) +" записей"

def rigth():
    global lim, l
    if (lim<l):
        lim=int(lim)+int(l)
        treev.delete(*treev.get_children())
        cur.execute("Select * FROM Work order by ClientNum Limit ? OFFSET '"+l+"'", [lim])
        count = cur.fetchall()
        for i in count:
            treev.insert("", 'end', values=i)
        conn.commit()
    
def sel(event):
    global lim, l
    lim=cbL.get()
    l=cbL.get()
    view()

cbL = ttk.Combobox(rootView, values=['5', '10','15'], state='readonly')
cbL.current(0)
cbL.bind('<<ComboboxSelected>>', sel)
cbL.place(relx=0.2, rely=0.05)
treev.bind('<<TreeviewSelect>>', select)

lim=cbL.get()
l=cbL.get()

b_left=Button(rootView, text="<-", command=left).place(relx=0.15, rely=0.9)
b_right=Button(rootView, text="->", command=rigth).place(relx=0.30, rely=0.9)

count.place(relx=0.04, rely=0.03)

entrS = Entry(frame, textvariable=var)
ret = Button(frame, text='Оплатить', command=retu).pack(side='bottom', pady=5)
cbS.bind('<<ComboboxSelected>>', search)
cbS.pack(side='top', padx=5, pady=5)
entrS.pack(side='top', padx=5, pady=5)
frame.pack(side='top', padx=5, pady=5)
count_label()
view()
