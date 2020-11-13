import mysql.connector as scon;
mycon=scon.connect(host="localhost",user="root",password="root",database="ToDoList")
cursor=mycon.cursor()
def add(nam):
	table(nam)
	
def addtask(tsk,name):
	task(tsk,name)

task_in='brush_your_teeth'
#function for creating a table for the newly comming users.



def table(nam):
	cretable="""create table {nop} (task varchar(100))""".format(nop=nam)
	cursor.execute(cretable)#creates the table for that user
	

def task(t_name,P_name):
	insert_val="""insert into {nop}(task) values('{p}')""".format(p=t_name,nop=P_name)
	cursor.execute(insert_val)
	mycon.commit()

#search for table name(sigin in)
def search_for_person(person_name):
	print(person_name)
	cursor.execute("show tables")
	n=cursor.fetchall()
	#count the number of rows
	count=len(n)
	print(count)
	for i in range(0,count):
		if (n[i][0]==person_name):
			print()
			return True



	
gettask="""select * from {}""".format("anandhu")
cursor.execute(gettask)
list_task=cursor.fetchall()
length=len(list_task)