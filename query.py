import sqlite3

connector = sqlite3.connect("data.db")
# data = list(connector.execute('select * from student'))
# print(data)

details = []
for i in range(1, 12):
    data = list(connector.execute('select student.sid, sname, vote.gid from student, vote where student.sid = vote.sid and vote.gid = ?', (i,)))
    string = str()
    for j in data:
        if string != "":
            string += ', '
        # string += j[0]
        string += j[1]
    if string == "":
        string = "无"
    details.append(string)
print(details)