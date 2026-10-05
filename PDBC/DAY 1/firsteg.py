"""import sqlite3
conn=sqlite3.connect("database.db")
cur=conn.cursor()
cur.execute('''CREATE TABLE if not exists PREMIUM_E141(name varchar(20),age int,address varchar(20))''')
cur.execute('DELETE FROM PREMIUM_E141')
cur.execute(''' INSERT INTO PREMIUM_E141 VALUES('PARA',21,'BALGLORE')''')
cur.execute(''' INSERT INTO PREMIUM_E141 VALUES('RAVA',22,'MUMBAI')''')
cur.execute(''' INSERT INTO PREMIUM_E141 VALUES('MARA',23,'PUNE')''')
res=cur.execute('''SELECT * FROM Preium_E141''')
print(res.fetchall())
conn.commit()
conn.close()"""

"""
import sqlite3
conn=sqlite3.connect("database.db")
cur=conn.cursor()
cur.execute('''CREATE TABLE if not exists P_E141(name varchar(20),age int,address varchar(20))''')
cur.execute('DELETE FROM P_E141')
cur.execute(''' INSERT INTO P_E141 VALUES('A',1,'BALGLORE')''')
cur.execute(''' INSERT INTO P_E141 VALUES('B',2,'MUMBAI')''')
cur.execute(''' INSERT INTO P_E141 VALUES('C',3,'PUNE')''')
res=cur.execute('''SELECT * FROM P_E141''')
print(res.fetchall())
conn.commit()
conn.close()
"""

