import sqlite3
def connect():
    #connection object
    conn=sqlite3.connect("book.db")
    #curser object
    cur=conn.cursor()
    #execute sql statement
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title text, author text, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()


#add entry
def add(title,author, year,isbn):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author, year,isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("SELECT * from book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="", year="", isbn=""):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("SELECT * from book WHERE title=? OR author=? OR year=? or isbn=?",(title,author, year, isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):

    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("Update book SET title=?,author=?,year=?,isbn=? where id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()









connect()
#insert("the sea", "John Tablet", 1918,91312132)
#insert("the earth", "Jina Smith", 1921,58312132)
delete(3)
view()
print(search(author="John Tablet"))