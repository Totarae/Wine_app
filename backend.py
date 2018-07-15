import sqlite3

class Database:

    def __init__(self,db):
        conn=sqlite3.connect(db)
        cur=conn.cursor()
        cur.execute(
        "CREATE TABLE IF NOT EXISTS wine "
        "(id INTEGER PRIMARY KEY , "
        "name TEXT, "
        "date DATE , "
        "grape TEXT, "
        "price FLOAT, "
        "distillery TEXT)"
        )
        conn.commit()
        conn.close()

    def insert(self,name,date,grape,price,dist):
        conn = sqlite3.connect("winery.db")
        cur = conn.cursor()
        cur.execute(
        "INSERT INTO "
        "wine "
        "values(NULL,?,?,?,?,?)",(name,date,grape,price,dist))
        conn.commit()
        conn.close()

    def view(self):
        conn = sqlite3.connect("winery.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM wine")
        rows=cur.fetchall()
        conn.close()
        return rows

    def search(self,name="",date="",grape="",price=0,dist=""):
        conn = sqlite3.connect("winery.db")
        cur = conn.cursor()
        cur.execute("SELECT * "
                "FROM wine "
                "WHERE name=? OR date=? OR grape=? OR price=? OR distillery=?",
                (name,date,grape,price,dist))
        rows = cur.fetchall()
        conn.close()
        return rows

    def delete(self,id):
        conn = sqlite3.connect("winery.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM wine WHERE id=?",(id,))
        conn.commit()
        conn.close()

    def update(self,id,name,date,grape,price,dist):
        conn = sqlite3.connect("winery.db")
        cur = conn.cursor()
        cur.execute(
        "UPDATE wine "
        "SET name=? OR date=? OR grape=? OR price=? OR distillery=?"
        "WHERE id=?", (name, date, grape, price, dist,id))
        conn.commit()
        conn.close()

#connect()
#print(search(name="Fanagoria"))
#print(view())