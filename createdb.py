import sqlite3

connector = sqlite3.connect("data.db")
connector.execute('''CREATE TABLE student (
                sid char(9),
                gid int
                );''')
connector.execute('''CREATE TABLE vote (
                sid char(9),
                gid int
                );''')
connector.commit()