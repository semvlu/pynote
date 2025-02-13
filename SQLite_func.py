import sqlite3
def newdata(id,name,sms):
    conn= sqlite3.connect("0421.db")
    c=conn.cursor()
    c.execute("INSERT INTO books VALUES(?,?,?)",(id,name,sms))
    conn.commit()
    conn.close()
def newdata1(list):
    conn= sqlite3.connect("0421.db")
    c=conn.cursor()
    c.executemany("INSERT INTO books VALUES(?,?,?)",(list)) #execute many
    conn.commit()
    conn.close()
def delete(id):
    conn= sqlite3.connect("0421.db")
    c=conn.cursor()
    c.executemany("DELETE FROM books WHERE id=(?)",(id))
    conn.commit()
    conn.close()
def update(id):
    conn= sqlite3.connect("0421.db")
    c=conn.cursor()
    c.executemany("UPDATE books SET name='Hello World' WHERE id=(?)",(id))
    conn.commit()
    conn.close()
def read():
    conn= sqlite3.connect("0421.db")
    c=conn.cursor()
    c.execute("SELECT * FROM books")
    all=c.fetchall()
    print(all)
    conn.commit()
    conn.close()
