from tkinter import *
def click():
    if b["text"]=="ON":
        f["bg"]="light blue"
        b["text"]="OFF"
    else:
        f["bg"]="yellow"
        b["text"]="ON"

        
r=Tk()
r.geometry('900x900')
f=Frame(r,width=900,height=900,bg="yellow")
f.place(x=0,y=0)
b=Button(f,text="ON",height=5,width=20,command=click)
b.place(x=350,y=350)
r.mainloop()