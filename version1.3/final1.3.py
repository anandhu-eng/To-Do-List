import tkinter
from tkinter import *
from PIL import Image,ImageTk
from database_settings import *
import time
from tkinter import messagebox
task=Tk()
task.iconbitmap('icon.ico')
task.geometry("500x500+700+200")
task.title("TASKS")

#heading
taskheading=Label(task,text="ENTER THE TASK",font=("arial",10,"bold"))
taskheading.pack()
#task input
taskentry=Entry(task,textvar=StringVar())
taskentry.pack()
##taskentry.insert(0,"Enter the task:")
#space to undergo the delete operation
taskdel=Label(task,text="Enter the task you want to delete",font=("arial",10,"bold"))
taskdel.pack()
td=Entry(task,textvar=StringVar())
td.pack()
##td.insert(0,"Enter the task to delete:")
#to refresh the windows
def refresh():
    task.destroy()
    #to open the same python file.
    exec(open("final1.3.py").read(),globals())


#to delete task
def mdeletet():
	taskname=td.get()
	delete_task(taskname)

def delete_task(taskname):
	deletetask="""delete from {} where task='{}'""".format("anandhu",taskname)
	cursor.execute(deletetask)
	mycon.commit()
	td.delete(0, END)
	refresh()
	#view_tasks()




#to view the task which was added
def view_tasks():
	view_task_button.configure(state=DISABLED)
	gettask="""select * from {}""".format("anandhu")
	cursor.execute(gettask)
	list_task=cursor.fetchall()
	length=len(list_task)
	if(length==0):
		messagebox.showerror("ERROR","Nothing To Desplay!\nEmpty task")
		#blank=Button(task,text="          ",font=("arial",10,"bold"),fg="white",bg="grey",state=DISABLED )
		#blank.grid(row=7,column=1)
	else:
		for i in range(1,length+1):
			task_list=Label(task,text=list_task[i-1][0],font=("arial",10,"bold"),padx=10)
			task_list.pack()



#function to record the entered task into the database
def add_task(a):
	task_get=a
	if(task_get==""):
		messagebox.showerror("ERROR","Enter Valid Task")

	else:
		gettask="""select * from {}""".format("anandhu")
		cursor.execute(gettask)
		list_task=cursor.fetchall()
		length=len(list_task)
		db_add="""insert into {} (task,Sl_No) values ('{}',{})""".format("anandhu",task_get,length+1)
		cursor.execute(db_add)
		mycon.commit()
		taskentry.delete(0, END)
		refresh()

def submit():
	Task=taskentry.get()
	add_task(Task)

submitbutton=Button(task,text="Submit Task",fg="white",bg="grey",font=("arial",10,"bold"),command=submit)
submitbutton.pack()

#close
backbutton=Button(task,text="Close",fg="white",bg="grey",font=("arial",10,"bold"),command=task.destroy)
backbutton.pack()


	
#view task button
view_task_button=Button(task,text="View Task",fg="white",bg="grey",font=("arial",10,"bold"),command=view_tasks)
view_task_button.pack()



#print(taskname)
delete_button=Button(task,text="Delete Task",fg="white",bg="grey",font=("arial",10,"bold"),command=mdeletet)
delete_button.pack()









task.mainloop()
