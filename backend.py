import sqlite3

class Database:

    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute(
        "CREATE TABLE IF NOT EXISTS wine "
        "(id INTEGER PRIMARY KEY , "
        "name TEXT, "
        "date DATE , "
        "grape TEXT, "
        "price FLOAT, "
        "distillery TEXT)"
        )
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def insert(self,name,date,grape,price,dist):
        self.cur.execute(
        "INSERT INTO "
        "wine "
        "values(NULL,?,?,?,?,?)",(name,date,grape,price,dist))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM wine")
        rows=self.cur.fetchall()
        return rows

    def search(self,name="",date="",grape="",price=0,dist=""):
        self.cur.execute("SELECT * "
                "FROM wine "
                "WHERE name=? OR date=? OR grape=? OR price=? OR distillery=?",
                (name,date,grape,price,dist))
        rows = self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM wine WHERE id=?",(id,))
        self.conn.commit()

    def update(self,id,name,date,grape,price,dist):
        self.cur.execute(
        "UPDATE wine "
        "SET name=? OR date=? OR grape=? OR price=? OR distillery=?"
        "WHERE id=?", (name, date, grape, price, dist,id))
        self.conn.commit()

#connect()
#print(search(name="Fanagoria"))
#print(view())