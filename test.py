import pymysql.cursors
connection = pymysql.connect(host='localhost', user='root', password='planres', db='checklist', cursorclass=pymysql.cursor.DictCursor)
def lastUpdatedDate(date): 
    lastUpdateofDatabase = date 
    def newDate(newDate):
         if newDate > date:
             print("new date is newer")
             # call update function
             return lastupdate = lastUpdatedDate() 	


def main():
    lastUpdatedDate1 = lastUpdatedDate(date)
    if lastUpdatedDate1():
        lastUpdatedDate1 = lastUpdatedDate() 
# The goal here is to have a function that checks when the last update to the database was,
# and if ]the newest update is sooner than the old update, cal
