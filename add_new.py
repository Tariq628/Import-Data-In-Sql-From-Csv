#  Python program to read CSV file line by line
# import necessary packages
import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database='tariq'
)

cursor = mydb.cursor()


csv.field_size_limit(100000000)


with open('domains_export.csv', encoding='utf-8') as file_obj:
    reader_obj = csv.reader(line.replace('\0', '') for line in file_obj)
    for i, row in enumerate(reader_obj):
        try:
            cursor.execute(
                f"UPDATE domains_export SET technologies='{row[94]}' WHERE id = {i + 1};")
            mydb.commit()
        except Exception as e:
            print(e)
