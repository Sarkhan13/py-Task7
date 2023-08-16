from tkinter import *

import random


window = Tk()


window.geometry('500x500')

window.title('Rəqəm təxmini programı')

label1 = Label(window, text='1-10 arasında təsadüfi bir rəqəm seçildi,zəhmət olmasa təxmininizi yazın.',font=('Arial',11))

label1.place(x=20,y=50)

entry1 = Entry(window, font=('Arial',15))

entry1.place(x=20,y=100)

saygac = 1

def oyun():
    
    global saygac
    
    rdm = int(11*random.random())
    
        
    tex = int(entry1.get())
    if tex == rdm:
        label2 = Label(window, text='Tebrikler! Duzgun reqemi tapdiniz. Cehd sayi: '+ str(saygac),font=('Arial',15),fg='green')
        label2.place(x=20,y=150)
            

    else:
        label3 = Label(window,text='Bextinizi bir daha sinayin. Cehd sayi: ' + str(saygac), font=('Arial',15),fg='red')
        label3.place(x=20,y=150)
        saygac +=1
            
            
            




button1 = Button(window, font=('Arial',11),text='check',command=oyun)

button1.place(x= 260,y=100)

window.mainloop()













