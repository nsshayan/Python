import sqlite3

create_table = """
CREATE TABLE emp(
    id   INTEGER PRIMARY KEY AUTOINCREMENT, 
    name VARCHAR(32),
    dept VARCHAR(32)
)
"""

insert_row = """
  INSERT INTO emp(name, dept) VALUES('%s', '%s')
"""


db = sqlite3.connect("empdb.dat")

db.execute(create_table)

cursor = db.cursor()

while True:
    name = raw_input("Enter name (end to exit): ")
    if name == "end": break
    dept = raw_input("Enter department: ")

    cursor.execute(insert_row % (name, dept))

db.commit()
db.close()


