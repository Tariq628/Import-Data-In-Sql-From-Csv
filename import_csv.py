import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tariq"
)

cursor = mydb.cursor()


t = ''
with open('sample4.csv') as file_obj:
    reader_obj = csv.reader(file_obj)
    for i, row in enumerate(reader_obj):
        sql = """
        INSERT INTO sample4 (Year, Age, Ethnic, Sex, Area, count) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        # val = (f"{row[0]}, {row[1]}")# wrong
        # val = (f"{row[0]}", f"{row[1]}")  # correct
        # print(val)
        val = (row[0],
               row[1],
               row[2],
               row[3],
               row[4],
               row[5],)
        cursor.execute(sql, val)
        print(i)
mydb.commit()
