from tkinter import*
import importlib
from tkinter import messagebox as mb

rootA=Tk()
rootA.title("Главная форма Администратора")
rootA.geometry('270x230')
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
        
def workView():
    global cli4, workView
    if (cli4==0):
        import workView
        cli4+=1
    else:
        importlib.reload(workView)


def addUser():
    global cli5, addUser
    if (cli5==0):
        import addUser
        cli5+=1
    else:
        importlib.reload(addUser)

def report():
    global cli3, report
    #mb.showinfo("Подождите!", "Отчёты на стадии разработки")
    if (cli3==0):
        import report
        cli3+=1
    else:
        importlib.reload(report)
    #Здесь нужен ворд или эксель


b1 = Button(rootA, text="Клиенты", width=25, command=cl).pack(padx=5, pady=10)

b2 = Button(rootA, text="Комнаты", width=25, command=rm).pack(padx=5, pady=10)

b4 = Button(rootA, text="Просмотр аренды", width=25, command=workView).pack(padx=5, pady=10)

b5 = Button(rootA, text="Добавление пользователя", width=25, command=addUser).pack(padx=5, pady=10)

b3 = Button(rootA, text="Отчёты", width=25, command=report).pack(padx=5, pady=10)
rootA.mainloop()
