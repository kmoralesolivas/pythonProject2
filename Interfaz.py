from tkinter import *

root = Tk()
root.state('zoomed')
root.geometry('1280x720')
root.title("Levaduras")
menubar = Menu(root)
root.config(menu=menubar)

frame = Frame()
frame.pack()
frame.config (width=1600, height=1600, bd=10, relief="groove")

configmenu = Menu(menubar, tearoff=0)
configmenu.add_command(label="Índice", command=lambda: frame_temas())
configmenu.add_command(label="Tema 01", command=lambda: frame_01())
configmenu.add_command(label="Tema 02", command=lambda: frame_02())
configmenu.add_command(label="Tema 03", command=lambda: frame_03())
configmenu.add_command(label="Tema 04", command=lambda: frame_04())
configmenu.add_separator()

configmenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(label="Menu", menu=configmenu)


def frame_temas():
    clear()

    miframe = Frame()
    miframe.pack()
    miframe.config(width=1000, height=1000, bd=10, relief="groove")
    milabel = Label(miframe, text="Índice", font=("Arial", 30))
    milabel.place(x=440, y=0)
    milabel2 = Label(miframe, text="Tema 1 Levaduras", font=("Arial", 25))
    milabel2.place(x=0, y=75)
    milabel3 = Label(miframe, text="Tema 2 Falsas Levaduras", font=("Arial", 25))
    milabel3.place(x=0, y=250)
    milabel4 = Label(miframe, text="Tema 3 Candida", font=("Arial", 25))
    milabel4.place(x=0, y=450)
    milabel5 = Label(miframe, text="Tema 4 Morfologia", font=("Arial", 25))
    milabel5.place(x=0, y=650)
    b1 = Button(miframe, text="Entrar", command=lambda: frame_01())
    b1.place(x=300, y=85)
    b2 = Button(miframe, text="Entrar", command=lambda: frame_02())
    b2.place(x=400, y=260)
    b3 = Button(miframe, text="Entrar", command=lambda: frame_03())
    b3.place(x=270, y=460)
    b4 = Button(miframe, text="Entrar", command=lambda: frame_04())
    b4.place(x=300, y=660)

def frame_01():
    clear()
    miframe2 = Frame(root, width=1000, height=1000, bd=10, relief="groove")
    milabel6 = Label(miframe2, text="Tema 1 Levaduras", font=("Arial", 30))
    milabel6.place(x=330, y=0)
    milabel10 = Label(miframe2, text="1", font=("Arial",25 ))
    milabel10.place(x=25, y=100)
    miframe2.pack()
    b5 = Button(miframe2, text="Índice", command=lambda: frame_temas())
    b5.place(x=100, y=25)
    b6 = Button(miframe2, text="Tema 2", command=lambda: frame_02())
    b6.place(x=800, y=25)


def frame_02():
    clear()
    miframe3 = Frame(root, width=1000, height=1000, bd=10, relief="groove")
    miframe3.pack()
    milabel7 = Label(miframe3, text="Tema 2 Falsas levaduras", font=("Arial", 30))
    milabel7.place(x=300,y=0)
    b7 = Button(miframe3, text="Tema 1", command=lambda: frame_01())
    b7.place(x=100, y=25)
    b8 = Button(miframe3, text="Tema 3", command=lambda: frame_03())
    b8.place(x=800, y=25)


def frame_03():
    clear()
    miframe4 = Frame(root, width=1000, height=1000, bd=10, relief="groove")
    miframe4.pack()
    milabel8 = Label(miframe4, text="Tema 3 Candida", font=("Arial", 30))
    milabel8.place(x=350,y=0)
    b9 = Button(miframe4, text="Tema 2", command=lambda: frame_02())
    b9.place(x=100, y=25)
    b10 = Button(miframe4, text="Tema 4", command=lambda: frame_04())
    b10.place(x=800, y=25)


def frame_04():
        clear()
        miframe5 = Frame(root, width=1000, height=1000, bd=10, relief="groove")
        miframe5.pack()
        milabel9 = Label(miframe5, text="Tema 4 Morfologia", font=("Arial", 30))
        milabel9.place(x=350, y=0)
        b11 = Button(miframe5, text="Tema 3", command=lambda: frame_03())
        b11.place(x=100, y=25)
        b12 = Button(miframe5, text="Índice", command=lambda: frame_temas())
        b12.place(x=800, y=25)

def clear():
    list = root.pack_slaves()
    for l in list:
        l.pack_forget()

root.mainloop()