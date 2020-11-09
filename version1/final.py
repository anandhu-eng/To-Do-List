from tkinter import *
from PIL import Image,ImageTk
from database_settings import *
import time

task=Tk()
task.iconbitmap('l.ico')
task.title("TASKS")

#heading
taskheading=Label(task,text="ENTER THE TASK",font=("arial",10,"bold"))
taskheading.grid(row=1,column=0)
#task input
taskentry=Entry(task,textvar=StringVar())
taskentry.grid(row=2,column=0)
#space to undergo the delete operation
td=Entry(task,textvar=StringVar())
td.grid(row=7,column=0)
#to refresh the windows
def refresh():
    task.destroy()
    #to open the same python file.
    exec(open("final.py").read(),globals())


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
	gettask="""select * from {}""".format("anandhu")
	cursor.execute(gettask)
	list_task=cursor.fetchall()
	length=len(list_task)
	if(length==0):
		nothing=Label(task,text="Nothing To Desplay!",font=("arial",10,"bold"),fg="red")
		nothing.grid(row=8,column=0)
		#blank=Button(task,text="          ",font=("arial",10,"bold"),fg="white",bg="grey",state=DISABLED )
		#blank.grid(row=7,column=1)
	else:
		for i in range(1,length+1):
			task_list=Label(task,text=list_task[i-1][0],font=("arial",10,"bold"),padx=10)
			task_list.grid(row=7+i,column=0)



#function to record the entered task into the database
def add_task(a):
	task_get=a
	if(task_get==""):
		invalid_task=Label(task,text="Enter Valid Task",font=("arial",10,"bold"),fg="red")
		invalid_task.grid(row=8,column=0)

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

submitbutton=Button(task,text="Submit",fg="white",bg="grey",font=("arial",10,"bold"),command=submit)
submitbutton.grid(row=4,column=0)

#back
backbutton=Button(task,text="Back",fg="white",bg="grey",font=("arial",10,"bold"))
backbutton.grid(row=6,column=0)


	
#view task button
view_task_button=Button(task,text="View Task",fg="white",bg="grey",font=("arial",10,"bold"),command=view_tasks)
view_task_button.grid(row=5,column=0)



#print(taskname)
delete_button=Button(task,text="Delete",fg="white",bg="grey",font=("arial",10,"bold"),command=mdeletet)
delete_button.grid(row=7,column=1)









task.mainloop()
