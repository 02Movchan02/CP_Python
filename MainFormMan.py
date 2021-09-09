from tkinter import*
import importlib

rootM=Tk()
rootM.title("Главная форма Менеджера")
rootM.geometry('270x190')
cli1 = 0
cli2 = 0
cli3 = 0
cli4 = 0
cli5 = 0
def cl():
    global cli1, client
    if (cli1==0):
        import client
        cli1+=1
    else:
        importlib.reload(client)

def rm():
    global cli2, rooms
    if (cli2==0):
        import rooms
        cli2+=1
    else:
        importlib.reload(rooms)
        

def work():
    global cli3, work
    if (cli3==0):
        import work
        cli3+=1
    else:
        importlib.reload(work)

def workView():
    global cli4, workView
    if (cli4==0):
        import workView
        cli4+=1
    else:
        importlib.reload(workView)


b1 = Button(rootM, text="Клиенты", width=25, command=cl).pack(padx=5, pady=10)

b2 = Button(rootM, text="Комнаты", width=25, command=rm).pack(padx=5, pady=10)

b3 = Button(rootM, text="Арендовать", width=25, command=work).pack(padx=5, pady=10)

b4 = Button(rootM, text="Просмотр аренды", width=25, command=workView).pack(padx=5, pady=10)

rootM.mainloop()
