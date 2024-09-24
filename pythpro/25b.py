from tkinter import *
from datetime import date
def disp():
    k=e.get().split('-')
    b=int(k[2])
    x=date.today()
    y=x.year
    res=y-b
    l1=Label(f,text="Person's age is "+str(res),font=20,fg="black")
    l1.place(x=300,y=300)
r=Tk()
r.geometry('900x900')
f=Frame(r,height=900,width=900,bg="yellow")
f.place(x=0,y=0)
l=Label(f,text="Enter the date of birth ",font=20,fg='red')
l.place(x=300,y=100)
e=Entry(f,width=20)
e.place(x=300,y=150)
b=Button(f,text="Age",fg="black",command=disp)
b.place(x=300,y=200)
r.mainloop()