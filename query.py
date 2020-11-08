import sqlite3

connector = sqlite3.connect("data.db")
data = list(connector.execute('select * from student'))
print(data)

gid = list(connector.execute("select gid from student where sid='031802113'"))
print(gid[0][0])