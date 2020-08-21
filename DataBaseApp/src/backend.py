import sqlite3 as sq


def connect():
    con = sq.connect("book.db")
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS book"
        "(id INTEGER PRIMARY KEY,"
        "title text,"
        "author text,"
        "year INTEGER ,"
        "isbn integer )"
    )
    con.commit()
    con.close()


def insert(title, author, year, isbn):
    con = sq.connect("book.db")
    cur = con.cursor()
    cur.execute("insert into book values(Null,?,?,?,?)", (title, author, year, isbn))
    con.commit()
    con.close()


def search(title="", author="", year="", isbn=""):
    con = sq.connect("book.db")
    cur = con.cursor()
    cur.execute("select * from book where title =? or author =? or  year =? or isbn =?", (title, author, year, isbn))
    searchlist = cur.fetchall()
    con.close()
    return searchlist


def delete(id):
    con = sq.connect("book.db")
    cur = con.cursor()
    cur.execute("Delete from book where id =?", (id,))
    con.commit()
    con.close()


def upadte(id, title, author, year, isbn):
    con = sq.connect("book.db")
    cur = con.cursor()
    cur.execute("update book set title =? ,author =? ,year =? ,isbn = ? where id =? ", (title, author, year, isbn, id))
    con.commit()
    con.close()


def view():
    con = sq.connect("book.db")
    cur = con.cursor()
    cur.execute("select * from book")
    list_data = cur.fetchall()
    con.close()
    return list_data


connect()
