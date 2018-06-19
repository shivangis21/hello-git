import MySQLdb
db=MySQLdb.connect("localhost","root","2126","Database1")
cursor=db.cursor()
#Q1

sql="""CREATE TABLE BOOKS BOOK_ID INT NOT NULL,
TITLE_ID INT,
LOCATION CHAR(20)
GENRE CHAR(20)
"""
sql2="""CREATE TABLE TITLES TITLE_ID INT NOT NULL,
TITLE CHAR(20),
ISBN INT, 
PUBLISHER CHAR(20),
PUBLISHER_ID INT,
"""
sql3="""SELECT * from BOOKS b JOIN TITLE t 
WHERE 
b.TITLE ID=t.TITLE ID

"""
cursor.execute(sql)
cursor.execute(sql2)
cursor.execute(sql3)

#Q2
sql="INSERT INTO BOOKS VALUES('%d', '%d', '%s', '%s') % (113, 212, "AGRA","Thriller")
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

#q3
sql="SELECT * FROM BOOKS"
cursor.execute(sql)
sql4="UPDATE BOOKS SET GENRE="THRILLER" WHERE LOCATION="DELHI"
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
sql="SELECT * FROM BOOKS"
db.close()

