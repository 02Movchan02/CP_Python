import sqlite3 as sql

conn = sql.connect('Hotel.db')

cur=conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Rooms(
RoomID INTEGER UNIQUE PRIMARY KEY,
Type TEXT,
PhoneRoom TEXT,
Places TEXT,
Price_day REAL,
Price_phone REAL DEFAULT 0,
Employment TEXT DEFAULT 'Свободно',
Booking TEXT DEFAULT 'Брони нет',
Photo TEXT);
""");
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS Clients(
ClientID INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
Surname TEXT,
Name TEXT,
Middle_name TEXT,
Passport TEXT UNIQUE,
Phone TEXT
);
""");
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS Work(
WorkID INTEGER PRIMARY KEY AUTOINCREMENT,
RoomNum INT,
ClientNum INT,
Duration_of_Days INT,
Payment REAL,
Status TEXT DEFAULT 'Оплачено');
""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS Users(
UserID INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
Surname TEXT,
Name TEXT,
Passport TEXT UNIQUE,
Adress TEXT,
Email BLOB,
LoginUser TEXT UNIQUE,
PasswordUser TEXT UNIQUE,
Post TEXT);
""")
conn.commit()

cur.execute("SELECT LoginUser FROM Users Where LoginUser = 'admin'")
row = cur.fetchone()
if (row[0]!="admin"):
    cur.execute("INSERT INTO Users (UserID, LoginUser, PasswordUser, Post) values ('1','admin', 'admin', 'Admin')")
    conn.commit()
conn.commit()




