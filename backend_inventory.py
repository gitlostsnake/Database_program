import sqlite3


def connect():
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS TMinventory
                (id INTEGER PRIMARY KEY, name TEXT,
                amount TEXT, price TEXT, warning_level TEXT,
                amount_taken TEXT, job_ids INTERGER)
                """)
    conn.commit()
    conn.close()


def insert(name, amount, price, warning_level):
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO TMinventory VALUES (NULL, ?,?,?,?)",
                (name, amount, price, warning_level))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM TMinventory")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM TMinventory WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, name, amount, price, warning_level):
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("""UPDATE TMinventory SET name=?,
                amount =?, price =?, warning_level=? WHERE id=?""",
                (name, amount, price, warning_level, id))
    conn.commit()
    conn.close()


connect()
# update(6, "2 Lane Wicket", "30", "NE MORE MONEY PLEASE!", "25%")
# delete(6)
# print(view())
# print("Now we will add the plate back in...")
# Test buttons
# insert("Frames", "200", "N/A", "20%")
# insert("SandBars", "400", "N/A", "20%")
# insert("SandBags", "800", "N/A", "20%")
# insert("Blue Arrow", "70", "N/A", "30%")
# insert("Man At Work", "70", "N/A", "30%")
# insert("2 Lane Wicket", "30", "N/A", "25%")
# print(view())
