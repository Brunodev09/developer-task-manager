import sqlite3
from sys import exit

NO_COL = "no such column"
NO_TABLE = "no such table"
EXISTS = "already exists"

class sql:
    try:
        def __init__(self):
            self.conn = sqlite3.connect('dtv-bdv.db')
            self.c = self.conn.cursor()

        def get_cursor(self):
            return self.c

        def get_conn(self):
            return self.conn

        def close_conn(self):
            self.conn.close()

        def commit(self):
            self.conn.commit()

        def select_all_tasks(self, table, value):
            t = (value,)
            self.c.execute('SELECT * FROM tasks WHERE symbol=?', t)

        def run_test_queries(self):
            try:
                t = ('test_db_task',)
                self.c.execute('SELECT * FROM tasks WHERE task_name=?', t)
                # print(self.c.fetchall())
                print('>> Sqlite3 db is running fine...')
                return True
            except sqlite3.Error as err:
                if NO_COL in str(err):
                    print(err)
                    print(">> This shouldn't happen. Choose JSON instead in next init.")
                    exit(1)
                elif NO_TABLE in str(err):
                    self.c.execute('''CREATE TABLE tasks
                        (task_name text, date_start text, date_finish text, paused text, d integer, h integer, m integer)''')
                    self.c.execute("INSERT INTO tasks VALUES ('test_db_task', '24-01-2020', '24-01-2020', 'false', 0, 2, 20)")
                    self.conn.commit()
                    print('>> Sqlite3 db is running this table for the first time in this computer...')
                    print (self.c.fetchone())
                    return True
    except Exception as e:
        print(e)                


