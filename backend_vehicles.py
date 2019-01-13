import sqlite3


def connect():
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS TMvehicles
                (id INTEGER PRIMARY KEY, FleetNo TEXT,
                RegistrationNo TEXT, WeightLimit TEXT,
                jobIdDay INTERGER, jobIdNight INTERGER)
                """)
    conn.commit()
    conn.close()


def insert(fleet_no, registration_no, weight_limit):
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO TMvehicles VALUES (NULL, ?,?,?)",
                (fleet_no, registration_no, weight_limit))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM TMvehicles")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM TMvehicles WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, fleet_no, registration_no, weight_limit):
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("""
                UPDATE TMvehicles SET fleet_no=?, registration_no=?,
                weight_limit=? WHERE id=?""",
                (fleet_no, registration_no, weight_limit, id))
    conn.commit()
    conn.close()


def view_everything():
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute('SELECT * FROM TMvehicles')
    [print(row) for row in cur.fetchall()]


connect()

# insert("TM560", "LX63 ZFK", "3.5T")
# insert("TM561", "LF63 ZFK", "3.5T")
# insert("TM562", "LX64 ZFK", "3.5T")
# insert("TM563", "LX65 ZFK", "3.5T")
# insert("TM564", "LX66 ZFK", "3.5T")
# insert("TM565", "LX67 ZFK", "3.5T")
# insert("TM566", "LX68 ZFK", "3.5T")
