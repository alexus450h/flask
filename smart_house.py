from tkinter import *
from tkinter import ttk
import serial,time
import math
root=Tk()
def change(pos):
    r=int(float(pos))
    l['text']=int(float(pos))
    ard.write(bytes(str(r),'utf8'))
    print(r)

ard=serial.Serial('com3','9600')
time.sleep(0.2)
pos=IntVar()
root.geometry('640x480+200+200')
a=ttk.Scale(root,from_=100,to=0,orient=VERTICAL,variable=pos,command=lambda pos:change(pos))
l=Label(root,text='0')
a.pack()
l.pack()
root.mainloop()
