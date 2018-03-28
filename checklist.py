import pymysql.cursors
import asyncio
connection = pymysql.connect(host='localhost', user='root', password='planes', db='checklist', cursorclass=pymysql.cursors.DictCursor)

def main():
    try:
       with connection.cursor() as cursor:
            sql = 'select * from orders where ordernum=' + input("Enter order ID: ")
            cursor.execute(sql)
            # Handle gracefully in production
            assert cursor.fetchone() is not None, "order number does not exist"
            print(cursor.fetchone())
    finally:
        cursor.close()

def update():
   
def printer():

main()
 
