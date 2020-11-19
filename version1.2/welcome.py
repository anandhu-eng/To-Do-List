import tkinter
from tkinter import *
from PIL import Image,ImageTk
from database_settings import *
import time

wlcm=Tk()
#wlcm.eval('tk::PlaceWindow %s center' % wlcm.winfo_pathname(wlcm.winfo_id()))
wlcm.iconbitmap('icon.ico')
wlcm.title("Welcome page")
wlcm.geometry("500x500")

label1=Label(wlcm,text='To_Do_List',fg="white",bg="grey",font=("arial",10,"bold"))
label1.place(x=200,y=20)

label2=Label(wlcm,text='Developed by:Anandhu S',font=("arial",10,"bold"))
label2.place(x=20,y=400)

label3=Label(wlcm,text='College:S C T College of Engineering, Pappanamcode, TVPM',font=("arial",10,"bold"))
label3.place(x=20,y=420)

label4=Label(wlcm,text='Version:1.10',font=("arial",10,"bold"))
label4.place(x=20,y=440)

def continuebutton():
	wlcm.destroy()
	exec(open("final.py").read(),globals())

button1=Button(wlcm,text="Continue-->",font=("arial",10,"bold"),fg="white",bg="grey",command=continuebutton)
button1.place(x=410,y=460)



wlcm.mainloop()