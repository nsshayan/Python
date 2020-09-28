from subprocess import Popen, PIPE

p = Popen(["sqlite3", "staffdb"], stdin=PIPE, stdout=PIPE)

create_statement = """
    CREATE TABLE emp(name VARCHAR(32), dept VARCHAR(32));
    INSERT INTO emp(name, dept) VALUES('john', 'IT');
    INSERT INTO emp(name, dept) VALUES('sam', 'Support');
    SELECT * FROM emp;
    .quit

"""

p.stdin.write(create_statement)

for line in p.stdout: print(line)


