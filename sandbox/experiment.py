import sqlite3

conn = sqlite3.connect('node_1_db.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS votingBlock(unix INT, datestamp TEXT, prev_hash TEXT)")

def data_entry():
    c.execute("INSERT INTO votingBlock VALUES(4, '7-27-2017', 'this is hash')")
    conn.commit()
    c.close()
    conn.close()

def read_db():
    c.execute("SELECT * FROM votingBlock")
    data = c.fetchall()
    print(data)


# create_table()
# data_entry()
# print('wow')

read_db()