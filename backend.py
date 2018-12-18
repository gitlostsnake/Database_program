import sqlite3

def connect():
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS road_works(id INTEGER PRIMARY KEY, location text,
                client text, startdate integer, length interger)""")
    conn.commit()
    conn.close()

### add new roadworks
def insert(location, client, startdate, length):
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO road_works VALUES (NULL, ?, ? ,? ,?)",
                (location, client, startdate, length))
    conn.commit()
    conn.close()

### view road works
def view():
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM road_works")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows


connect()

testing by...
insert("Newcastle", "martins", 230219, 200)
print(view())

### getting errors on line 33, 16. sqlite3.OperationalError no such column: location.
