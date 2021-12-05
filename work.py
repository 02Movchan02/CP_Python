from tkinter import*
from tkinter import ttk
from tkinter import messagebox as mb
import sqlite3 as sql

conn=sql.connect('Hotel.db')
cur=conn.cursor()

rootWork = Tk()
rootWork.title("Аренда")

l1 = Label(rootWork, text="Номер комнаты")
cb1 = ttk.Combobox(rootWork, state='readonly')

l2 = Label(rootWork, text="Клиент")
cb2 = ttk.Combobox(rootWork, state='readonly')

l3 = Label(rootWork, text="Количество дней")
e1 = Entry(rootWork)

p1 = StringVar()
ch1 = Checkbutton(rootWork, text="Бронь",variable=p1, onvalue="Бронь есть", offvalue="Брони нет")
p1.set("Брони нет")

def zap():
    cur.execute("Select ClientID, Surname, Name From Clients Order by ClientID")
    client=cur.fetchall()
    cb2['values']=client
    conn.commit()
    cur.execute("Select RoomID, Type From Rooms Where Employment = 'Свободно' Order By RoomID")
    room=cur.fetchall()
    cb1['values']=room



def select(event):
    global RoomID, ClientID, price, phone, bron
    s1=cb1.get()
    s=s1.find(" ")
    RoomID=cb1.get()[0:s]
    a1=cb2.get()
    a=a1.find(" ")
    ClientID = cb2.get()[0:a]
    cur.execute("Select Price_day From Rooms Where RoomID = ?;", [str(RoomID)])
    price = cur.fetchone()
    conn.commit()
    cur.execute("Select PhoneRoom From Rooms Where RoomID = ?;", [str(RoomID)])
    ph = cur.fetchone()
    if (ph[0]=="Есть"):
        cur.execute("Select Price_phone From Rooms Where RoomID = ?;", [str(RoomID)])
        phone=cur.fetchone()
    elif (ph[0]=="Нет"):
        phone=[0]
        
def addW(h1,h2,h3):
    try:
        pay = (price[0]*float(h3))+phone[0]
        answer = mb.askyesno(title="Подтверждение", message="К оплате "+str(pay)+" рублей, Подтвердить?")
        if answer:
            cur.execute("Insert into Work (RoomNum, ClientNum, Duration_of_Days, Payment) values (?,?,?,?);", (h1,h2,h3,pay))
            conn.commit()
            cur.execute("UPDATE Rooms Set Employment = 'Занято' Where RoomID = ?;", [str(RoomID)])
            conn.commit()
            if p1.get()=="Бронь есть":
                cur.execute("UPDATE Rooms Set Booking = 'Бронь есть' Where RoomID = ?;", [str(RoomID)])
                conn.commit()
                cur.execute("UPDATE Work Set Status = 'Не оплачено' Where RoomID = ?;", [str(RoomID)])
                conn.commit()
    except:
        mb.showinfo("Ошибка!", "Заполните данные")
cb1.bind('<<ComboboxSelected>>', select)
cb2.bind('<<ComboboxSelected>>', select)

l1.pack(padx=5,pady=5)
cb1.pack(padx=5,pady=5)

l2.pack(padx=5,pady=5)
cb2.pack(padx=5,pady=5)

l3.pack(padx=5,pady=5)
e1.pack(padx=5,pady=5)

ch1.pack(padx=5,pady=5)


zap()
btnAc = Button(rootWork, text="Оформить", command=lambda:addW(h1=RoomID, h2=ClientID, h3=e1.get())).pack(padx=5,pady=5)

rootWork.mainloop()
