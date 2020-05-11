# basic todo application in python
'''
An application to stores the task of the user
user can add, delete, update and search task
'''

# required imports
from tkinter import *
from todoAppBackend import Database
from tkinter.messagebox import showerror

class Todo:
	def __init__(self):
		self.window= Tk()
		
		try:
			self.databaseObj = Database()
		except Exception:
			self.window.destroy()
			showerror("Error","Something went wrong try again later.")
		
		# Label Frame
		self.frame= LabelFrame(self.window,padx=15, pady=15)
		self.frame.pack(padx=5, pady=5)

		# task name and labe view
		self.task_name_label = Label(self.frame,text="Task Name")
		self.task_name_label.grid(row=0, column=0)

		self.task_area = Entry(self.frame)
		self.task_area.grid(row=0,column=1)


		# task list view
		self.task_list = Listbox(self.frame, height=8, width= 30)
		self.task_list.grid(row=1,column=0, rowspan=4, columnspan=2)

		self.task_list_scroll= Scrollbar(self.frame)
		self.task_list_scroll.grid(row=1,column=2,rowspan=6)

		self.task_list.configure(yscrollcommand=self.task_list_scroll.set)
		self.task_list_scroll.configure(command=self.task_list.yview)

		self.task_list.bind('<<ListboxSelect>>', self.get_selected_row)


		# button views
		self.add_button = Button(self.frame, text="Add Task", command=self.add_command)
		self.add_button.configure(width=10)
		self.add_button.grid(row=0, column=3)

		self.delete_button = Button(self.frame, text="Delete Task", command=self.delete_command)
		self.delete_button.configure(width=10)
		self.delete_button.grid(row=1, column=3, pady=2)

		self.update_button = Button(self.frame, text="Update Task", command=self.update_command)
		self.update_button.configure(width=10)
		self.update_button.grid(row=2, column=3)

		self.search_button = Button(self.frame, text="Search Task", command=self.search_command)
		self.search_button.configure(width=10)
		self.search_button.grid(row=3, column=3)

		self.view_all_button = Button(self.frame, text="View All Task", command=self.view_all_command)
		self.view_all_button.configure(width=10)
		self.view_all_button.grid(row=4, column=3)
		
		self.window.mainloop()

	def view_all_command(self):
		sno=1
		self.task_list.delete(0,END) # clear the list
		for row in self.databaseObj.view_all_task():
			self.task_list.insert(END, (sno, row[1]) )
			sno+=1

	def search_command(self):
		self.task_list.delete(0,END)
		for row in self.databaseObj.search_task( str(self.task_area.get()) ):
			self.task_list.insert(END, row)

	def add_command(self):
		if str(self.task_area.get())!="":
			self.databaseObj.add_task(str(self.task_area.get()))
		self.view_all_command()

	def delete_command(self):
		try:
			self.databaseObj.delete_task(selected_row[0])
			self.task_area.delete(0,END)
		except Exception:
			pass
		finally:
			self.view_all_command()

	def update_command(self):
		try:
			self.databaseObj.update_task(int(selected_row[0]),str(self.task_area.get()))
		except Exception:
			pass
		finally:
			self.view_all_command()

	def get_selected_row(self,event):
		try:
			global selected_row
			index = self.task_list.curselection()
			selected_row = self.task_list.get(index)
			self.task_area.delete(0,END)
			self.task_area.insert(END,selected_row[1])
		except Exception:
			pass




if __name__ == '__main__':
	todo= Todo()