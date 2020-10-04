from tkinter import *
window=Tk()
window.geometry("500x500")
window.title("HOME")
head=Label(window,text="To-Do List",bg='white',fg='black',relief='solid',font=("arial",20,"bold"))
#relief puts border around that sentence
head.pack(fill=BOTH,pady=2,padx=2)#FILL BOTH STRETCHES THE HEADING TO EITHER SIDE
signin=Button(window,text="sign in",bg="grey",fg="white",relief="groove",font=("arial",10,"bold"),padx=20,pady=10)
signin.place(x=210,y=150)
signup=Button(window,text="sign up",bg="grey",fg="white",relief="groove",font=("arial",10,"bold"),padx=18,pady=10)
signup.place(x=210,y=230)
quits=Button(window,text="Quit",bg="grey",fg="white",relief="groove",font=("arial",10,"bold"),padx=28,pady=10,command=window.destroy)
quits.place(x=210,y=310)

window.mainloop()
