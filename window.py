from tkinter import*
from tkinter import ttk
from tkinter.filedialog import*
from PIL import Image, ImageTk
import sqlite3 as sql
import importlib

conn=sql.connect('Hotel.db')
cur=conn.cursor()
rootWind = Tk()
rootWind.title("Комнаты")
i=1
j=1

images=[]


def b1(event):
    f=event.widget['text']
    cur.execute("Select * FROM Rooms Where RoomID=?", [str(f)])
    new=Tk()
    new.title("Информация")

    one_result=cur.fetchall()
    
    lm = Label(new, text="Информация о номере").pack(pady=10)
    treev=ttk.Treeview(new, height=3)
    treev.pack(side='top')
    scrlbar = ttk.Scrollbar(new, orient='vertical', command=treev.yview)
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

    def work():
        rootWind.destroy()
        new.destroy()
        import work
        
    b1 =  Button(new, text="Оформить", width=15, command=work).pack(side='top', padx=10, pady=15)

    for i in one_result:
        treev.insert("", 'end', values=i)
    conn.commit()




cur.execute("Select * FROM Rooms")
rows = cur.fetchall()

for row in rows:
    im=row[8]
    n=row[0]
    img=Image.open(im)
    img.thumbnail((200,200), Image.ANTIALIAS)
    img=ImageTk.PhotoImage(img)
    panel=Label(rootWind, image=img, text=n)
    panel.grid(row=i, column=j, padx=10, pady=15)
    panel.bind('<Button-1>', b1)
    images.append(img)
    j+=1
    if j==5:
        i+=1
        j=1
