import pymysql.cursors
from datetime import datetime
connection = pymysql.connect(host='localhost', user='root', password='planes', db='checklist', cursorclass=pymysql.cursors.DictCursor)


def lastUpdatedDate(date): 
    if date is not None:
        lastUpdateofDatabase = date 
    def newDate():
        with connection.cursor() as cursor:
            cursor.execute('show table status from checklist lile \'orders\'')
            dt = cursor.fetchone().get("Update_time")	
            if dt > lastUpdatedDate:
                updateList()
                lastUpdatedDate = dt 
            else:
                print("current updated date is current")
def main():
    with connection.cursor() as cursor:

        sql = 'show table status from checklist like \'orders\''  
        cursor.execute(sql)
        dt = datetime.strptime(cursor.fetchone().get("Update_time"), '%Y-%m-%d %H:%M:%S')
# The goal here is to have a function that checks when the last update to the database was,
# and if ]the newest update is sooner than the old update, cal
main()
