# Python program to read CSV file line by line
# import necessary packages
import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tariq"
)

# Creating an instance of 'cursor' class
# which is used to execute the 'SQL'
# statements in 'Python'
cursor = mydb.cursor()

# Creating a database with a name
# 'geeksforgeeks' execute() method
# is used to compile a SQL statement
# below statement is used to create
# the 'geeksforgeeks' database


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
