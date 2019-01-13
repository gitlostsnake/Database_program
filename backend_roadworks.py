import sqlite3
import time
from datetime import datetime
import backend_inventory
import backend_vehicles

# date_format = '%Y-%m-%d %H:%M'

# Date and time is set as integer and needs to be changed to datetime
# The length will be another date and will do something like
# start_date - end_time = duration_of_roadworks
# Location will be changed eventually from text to OM image or RW drawing

# Connect to the sql database


def connect():
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS road_works(id INTEGER PRIMARY KEY,
                location TEXT, client TEXT, start_date TEXT, end_date TEXT)""")
    conn.commit()
    conn.close()

# ~Not Complete~
def assigned():
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS assigned_to(?,?)""")


def assign_vehicle():
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS assigned_vehicles(?, ?)
                """,
                ())
# ~Not Complete~
# Add new roadworks + changes date strings into datetime objects


def insert(location, client, start_date, end_date):
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO road_works VALUES (NULL, ?, ?, ?, ?)",
                (location, client, start_date, end_date))
    start_date = datetime.strptime(start_date, "%Y-%m-%d %H:%M")
    end_date = datetime.strptime(end_date, "%Y-%m-%d %H:%M")
    conn.commit()
    conn.close()


# view road works
def view():
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM road_works")
    rows = cur.fetchall()
    conn.close()
    return rows


# search function
def search(location="", client="", start_date="", end_date=""):
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM road_works WHERE location=?
                OR client=? OR start_date=? OR end_date=?""",
                (location, client, start_date, end_date))
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


# Update arguments and edit the jobs in the database
def update(id, location, client, start_date, end_date):
    conn = sqlite3.connect("road_works.db")
    cur = conn.cursor()
    cur.execute("""UPDATE road_works SET location=?, client=?,
                start_date=?, end_date=? WHERE id=?""",
                (location, client, start_date, end_date, id))
    conn.commit()
    conn.close()

# Going to do some calculations with the start and end date and return it
# as a row
# def timeleft(start_date, end_date):
#     conn = sqlite3.connect("road_works.db")
#     cur = conn.cursor()
#     cur.execute()

# test datetime object
# print("")

# SENTDEX TUTORIAL FOR DATETIME IN SQLITE3
# def dynamic_data_entry():
    # start_date =


connect()
# Test buttons
# update(4, "Penrith", "HW Martins", 200719, 25)
# insert("A19", "Martins", "2019-02-01 20:00", "2019-03-01 06:00")
# insert("A66", "Penrtith Council", "2019-3-15 06:00", "2019-03-20 15:00")
# insert("A19", "TMNE", "2019-03-16 20:00", "2019-07-16 06:00")
# insert("A66", "Darlington Council", "2019-04-01 06:00", "2019-05-01 06:00")
# print(search(length="1"))
# print("Before clean up")
# print(view())
# delete(3)
# print("After clean up")
# print(view())
# print("All done")


# Testing turning start_date into a datetime object.
# dateObject = datetime.strptime(start_date, "%B %d, %Y")
# print(dateObject.date())
