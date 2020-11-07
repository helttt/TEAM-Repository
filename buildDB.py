import sqlite3
def buildDataBase():
   connector = sqlite3.connect('Information.db')
   connector.execute('''CREATE TABLE IF NOT EXISTS Student (
                   ID     TEXT    NOT NULL,
                   S_group  INT);''')

   connector.execute('''CREATE TABLE IF NOT EXISTS Vote (
                   ID     TEXT    NOT NULL,
                   Votegroup   INT NOT NULL,
                   Vote INT);''')

   connector.commit()
