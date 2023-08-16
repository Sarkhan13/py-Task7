from tkinter import *

window = Tk()

window.geometry('500x500')


input1 = Entry(window, font=('Arial',20))

input1.place(x=20,y=50)

def cap():
    quvvet = int(input1.get())**2
    input2 = Entry(window,font=('Arial',20) )
    input2.insert(0,quvvet)
    input2.place(x=20,y=150)

button = Button(window, text='yaz',font=('Arial',10),command=cap)
button.place(x=20,y=90)






window.mainloop()