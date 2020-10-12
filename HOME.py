from tkinter import *
from PIL import Image,ImageTk
def signin():
    window.destroy()
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



def signup():
    window.destroy()#quits the previous home window
    sup=Tk()
    sup.title("SIGN UP PAGE")
    sup.geometry("500x500")
    name=Label(sup,text="Name:",font=("arial",10,"bold"))
    name.place(x=120,y=180)
    entryname=Entry(sup,textvar=StringVar())
    entryname.place(x=180,y=180)
    subbutton=Button(sup,text="SignUp",font=("arial",10,"bold"),relief="groove",bg="grey",fg="white")
    subbutton.place(x=210,y=230)
    image=Image.open("E:/python/tkinter/to do list/signup.png")
    photo=ImageTk.PhotoImage(image)
    prof=Label(image=photo)
    prof.place(x=220,y=120)
    sup.mainloop()


window=Tk()
window.geometry("500x500")
window.title("HOME")
head=Label(window,text="To-Do List",bg='white',fg='black',relief='solid',font=("arial",20,"bold"))
#relief puts border around that sentence
head.pack(fill=BOTH,pady=2,padx=2)#FILL BOTH STRETCHES THE HEADING TO EITHER SIDE
signin=Button(window,text="sign in",bg="grey",fg="white",relief="groove",font=("arial",10,"bold"),
              padx=20,pady=10,command=signin)
signin.place(x=210,y=150)
signup=Button(window,text="sign up",bg="grey",fg="white",relief="groove",font=("arial",10,"bold"),padx=18,pady=10,command=signup)
signup.place(x=210,y=230)
quits=Button(window,text="Quit",bg="grey",fg="white",relief="groove",font=("arial",10,"bold"),
             padx=28,pady=10,command=window.destroy)
quits.place(x=210,y=310)

window.mainloop()


