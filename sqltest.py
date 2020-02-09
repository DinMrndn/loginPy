import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=MARUNDAN\SQLEXPRESS;'
                      'Database=DB_Inventory;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute("SELECT * FROM items")

print(len(cursor.fetchall()))

for a in cursor.fetchall():
    print(a)
cursor.commit()