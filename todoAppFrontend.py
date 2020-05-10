# basic todo application in python
'''
An application to stores the task of the user
user can add, delete, update and search task
'''

# required imports
from tkinter import *
from todoAppBackend import *
from tkinter.messagebox import showerror


window= Tk()

def view_all_command():
	sno=1
	task_list.delete(0,END) # clear the list
	for row in view_all_task():
		task_list.insert(END, (sno, row[1]) )
		sno+=1

def search_command():
	task_list.delete(0,END)
	for row in search_task( str(task_area.get()) ):
		task_list.insert(END, row)

def add_command():
	if str(task_area.get())!="":
		add_task(str(task_area.get()))
	view_all_command()

def delete_command():
	try:
		delete_task(selected_row[0])
		task_area.delete(0,END)
	except Exception:
		pass
	finally:
		view_all_command()

def update_command():
	try:
		update_task(int(selected_row[0]),str(task_area.get()))
	except Exception:
		pass
	finally:
		view_all_command()

def get_selected_row(event):
	try:
		global selected_row
		index = task_list.curselection()
		selected_row = task_list.get(index)
		task_area.delete(0,END)
		task_area.insert(END,selected_row[1])
	except Exception:
		pass

def initDB():
	try:
		connectDB()
	except Exception:
		window.destroy()
		showerror("Error","Something went wrong try again later.")


# Label Frame
frame= LabelFrame(window,padx=15, pady=15)
frame.pack(padx=5, pady=5)

# task name and labe view
task_name_label = Label(frame,text="Task Name")
task_name_label.grid(row=0, column=0)

task_area = Entry(frame)
task_area.grid(row=0,column=1)


# task list view
task_list = Listbox(frame, height=8, width= 30)
task_list.grid(row=1,column=0, rowspan=4, columnspan=2)

task_list_scroll= Scrollbar(frame)
task_list_scroll.grid(row=1,column=2,rowspan=6)

task_list.configure(yscrollcommand=task_list_scroll.set)
task_list_scroll.configure(command=task_list.yview)

task_list.bind('<<ListboxSelect>>', get_selected_row)


# button views
add_button = Button(frame, text="Add Task", command=add_command)
add_button.configure(width=10)
add_button.grid(row=0, column=3)

delete_button = Button(frame, text="Delete Task", command=delete_command)
delete_button.configure(width=10)
delete_button.grid(row=1, column=3, pady=2)

update_button = Button(frame, text="Update Task", command=update_command)
update_button.configure(width=10)
update_button.grid(row=2, column=3)

search_button = Button(frame, text="Search Task", command=search_command)
search_button.configure(width=10)
search_button.grid(row=3, column=3)

view_all_button = Button(frame, text="View All Task", command=view_all_command)
view_all_button.configure(width=10)
view_all_button.grid(row=4, column=3)
view_all_command()

window.mainloop()
initDB()