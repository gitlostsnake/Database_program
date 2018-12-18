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
    conn.close()
    return rows

# search function
def search(location="", client="", startdate="", length=""):
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM road_works WHERE location=? OR client=? OR startdate=? OR length=?",
                (location, client, startdate, length))
    rows = cur.fetchall()
    conn.close()
    return rows

# delete road works
def delete(id):
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM road_works WHERE id=?",(id,))
    conn.commit()
    conn.close()


connect()


# Test functions
# insert("Location of work", "Client", startdate 18/12/18= 181218, length in # of days= 12)
# print(search(argument=""))
# print(view(###this will list all items))
# delete(1) ### deletes the first item.
