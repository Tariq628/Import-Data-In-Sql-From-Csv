import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)

cursor = mydb.cursor()


sql = """
SELECT estimated_monthly_sales FROM domains_export;
"""
cursor.execute(sql)
result = cursor.fetchall()
for i, a in enumerate(result):
    try:
        dollar = int(float(a[0].replace("USD $", '').replace(',', '')))
        cursor.execute(
            f"UPDATE domains_export SET est_dollars={dollar} WHERE id = {i + 1};")
        print(i, dollar)
        mydb.commit()
    except Exception:
        dollar = 0
        cursor.execute(
            f"UPDATE domains_export SET est_dollars={dollar} WHERE id = {i + 1};")
        mydb.commit()
