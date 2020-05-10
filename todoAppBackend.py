'''

'''

# required imports
import sqlite3

def connectDB():
	conn = sqlite3.connect("todo.db")
	cur = conn.cursor()

	cur.execute(" CREATE TABLE IF NOT EXISTS task (id INTEGER PRIMARY KEY, \
		task_name TEXT NOT NULL UNIQUE )")
	conn.commit()
	conn.close()

def add_task(taskname):
	conn = sqlite3.connect("todo.db")
	cur = conn.cursor()
	try:
		cur.execute("INSERT INTO task VALUES(NULL,?)",(taskname,))
	except Exception as e:
		pass
	finally:
		conn.commit()
		conn.close()

def view_all_task():
	conn = sqlite3.connect("todo.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM task")
	rows= cur.fetchall()
	conn.close()
	return rows

def search_task(taskname=""):
	conn = sqlite3.connect("todo.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM task WHERE task_name LIKE ?", ('%'+taskname+'%',))
	rows= cur.fetchall()
	conn.close()
	return rows

def delete_task(id):
	conn = sqlite3.connect("todo.db")
	cur = conn.cursor()
	cur.execute("DELETE FROM task where id=?", (id,))
	conn.commit()
	conn.close()

def update_task(id,taskname):
	conn = sqlite3.connect("todo.db")
	cur = conn.cursor()
	cur.execute("UPDATE task SET task_name=? where id=?", (taskname,id))
	conn.commit()
	conn.close()

connectDB()