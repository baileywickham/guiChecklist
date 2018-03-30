import pymysql.cursors
import asyncio
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='planes',
                             db='checklist',
                             cursorclass=pymysql.cursors.DictCursor)

# All db connections will be enclosed in with statements to handle closing properly.
# Avoid global variable
colorDict = {'blue' : '\033[94m', 'endc' : '\033[0m'}
def update(ordernum):
    with connection.cursor() as cursor:
        cursor.execute('select * from orders where ordernum=' + ordernum) 
        orderDict = cursor.fetchone()
        assert orderDict is not None, "Order number does not exist"
        printer(orderDict) 

def printer(orderDict): 
    for x in sorted(orderDict):
        print(x, ":", orderDict.get(x))

def lastUpdatedDate(startUp=False):
    if startUp:
        with connection.cursor() as cursor:
            cursor.execute('show table status from checklist like \'orders\'')
            lastUpdateOfDatabase = cursor.fetchone().get("Update_time") 
    def newDate():
        with connection.cursor() as cursor:
            cursor.execute('show table status from checklist like \'orders\'')
            dt = cursor.fetchone().get("Update_time")
            if dt > lastUpdateOfDatabase:
                update()
                lastUpdatedDate = dt
            else:
                print("current updated date is current")
def main():
    lastUpdatedDate(True)
    update(input("Enter an ordernumber: "))

if __name__ == '__main__':
    main()
