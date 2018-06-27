import sqlite3

def connect():
    conn=sqlite3.connect("winery.db")
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

def insert(name,date,grape,price,dist):
    conn = sqlite3.connect("winery.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO "
        "wine "
        "values(NULL,?,?,?,?,?)",(name,date,grape,price,dist))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("winery.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM wine")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(name="",date="",grape="",price=0,dist=""):
    conn = sqlite3.connect("winery.db")
    cur = conn.cursor()
    cur.execute("SELECT * "
                "FROM wine "
                "WHERE name=? OR date=? OR grape=? OR price=? OR distillery=?",
                (name,date,grape,price,dist))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("winery.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM wine WHERE id=?",
                (id))
    conn.commit()
    conn.close()

def update(id,name,date,grape,price,dist):
    conn = sqlite3.connect("winery.db")
    cur = conn.cursor()
    cur.execute(
        "UPDATE wine "
        "SET name=? OR date=? OR grape=? OR price=? OR distillery=?"
        "WHERE id=?", (name, date, grape, price, dist,id))
    conn.commit()
    conn.close()

#print(search(name="Fanagoria"))
print(view())