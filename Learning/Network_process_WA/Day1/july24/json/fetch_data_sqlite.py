import sqlite3

select_query = """
    SELECT id, name, dept FROM emp
"""

db = sqlite3.connect("empdb.dat")
cursor = db.execute(select_query)

for emp_id, name, dept in cursor:
    print emp_id, name, dept


db.close()


