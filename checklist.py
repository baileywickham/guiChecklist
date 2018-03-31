import pymysql.cursors
import asyncio
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='planes',
                             db='checklist',
                             cursorclass=pymysql.cursors.DictCursor)

# All db connections will be enclosed in with statements to handle closing properly.
# Avoid global variable, colorDict should be constant.

# Grabs orders from database.
def update(ordernum):
    with connection.cursor() as cursor:
        cursor.execute('select * from orders where ordernum=' + ordernum) 
        orderDict = cursor.fetchone()
        assert orderDict is not None, "Order number does not exist"
        printer(orderDict) 
        cursor.close()

# Prints the order, color coding for true false. 
def printer(orderDict): 
    print("order:", color(orderDict.pop("ordernum"), "blue"))
    for test in sorted(orderDict):
        if bool(orderDict.get(test)):
            print(test, ":", color(bool(orderDict.get(test)), "green"))
        else:
            print(test, ":", color(bool(orderDict.get(test)), "red"))

# Checks if db has been updated by a seperate script since last sync. 
# Does this by using a closure to preserve the last date, calling startUp true to
# initialize the date. 
def lastUpdatedDate(startUp=False):
    if startUp:
        with connection.cursor() as cursor:
            cursor.execute('show table status from checklist like \'orders\'')
            lastUpdateOfDatabase = cursor.fetchone().get("Update_time") 
            cursor.close()

    def newDate():
        with connection.cursor() as cursor:
            cursor.execute('show table status from checklist like \'orders\'')
            dt = cursor.fetchone().get("Update_time")
            if dt > lastUpdateOfDatabase:
                update()
                lastUpdatedDate = dt
            else:
                print("current updated date is current")
            cursor.close()

# Colors lines of text using acii codes built in a dict. 
def color(text, color):    
    colorDict = {'blue' : '\033[94m', 'green' : '\033[92m', 'red' : '\033[91m', 'endc' : '\033[0m'}
    assert color in colorDict, "color does not exist"
    return colorDict.get(color) + str(text) + colorDict.get("endc") 


def main():
    lastUpdatedDate(True)
    update(input("Enter an ordernumber: "))
    input('\n' + "enter the number of the one you would like to change")

if __name__ == '__main__':
   main()
