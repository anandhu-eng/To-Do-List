from tkinter import *
from PIL import Image,ImageTk
SIP=Tk()
#fn=StringVar()
SIP.geometry("500x500")
SIP.title("SIGN IN PAGE")
si=Label(SIP,text="Sign in using your roll no.",font=("arial",20,"bold"))
si.place(x=70,y=250)
rn=Label(SIP,text="Roll No.:",font=("arial",10,"bold"))
rn.place(x=120,y=310)
enentry=Entry(SIP,textvar=StringVar())
enentry.place(x=190,y=310)
image=Image.open("E:/python/tkinter/to do list/signin.png")
photo=ImageTk.PhotoImage(image)
prof=Label(image=photo)
prof.place(x=130,y=10)
signin=Button(SIP,text="signin",font=("arial",10,"bold"),relief="groove",bg="grey",fg="white")
signin.place(x=230,y=350)
back=Button(SIP,text="back",font=("arial",10,"bold"),relief="groove",bg="grey",fg="white",padx=5)
back.place(x=230,y=390)



SIP.mainloop()
