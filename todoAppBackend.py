'''

'''

# required imports
import sqlite3

class Database:

	def __init__(self):
		self.conn = sqlite3.connect("todo.db")
		self.cur = self.conn.cursor()

		self.cur.execute(" CREATE TABLE IF NOT EXISTS task (id INTEGER PRIMARY KEY, \
			task_name TEXT NOT NULL UNIQUE )")
		self.conn.commit()

	def add_task(self, taskname):
		try:
			self.cur.execute("INSERT INTO task VALUES(NULL,?)",(taskname,))
		except Exception as e:
			pass
		finally:
			self.conn.commit()

	def view_all_task(self):
		self.cur.execute("SELECT * FROM task")
		rows= self.cur.fetchall()
		return rows

	def search_task(self,taskname=""):
		self.cur.execute("SELECT * FROM task WHERE task_name LIKE ?", ('%'+taskname+'%',))
		rows= self.cur.fetchall()
		return rows

	def delete_task(self,id):
		self.cur.execute("DELETE FROM task where id=?", (id,))
		self.conn.commit()

	def update_task(self, id,taskname):
		self.cur.execute("UPDATE task SET task_name=? where id=?", (taskname,id))
		self.conn.commit()

	def __del__(self):
		self.conn.close()