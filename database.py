#https://www.youtube.com/watch?v=3vsC05rxZ8c
#https://www.youtube.com/watch?v=91iNR0eG8kE&t=468s
import mysql.connector
#https://stackoverflow.com/questions/50557234/authentication-plugin-caching-sha2-password-is-not-supported
from update import getLowestAskGoat
from goat import get_lowestAsk
from goat import *
from stockx import *
from datetime import datetime
# from test import getDateNTime

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root1234"
)


mycursor = db.cursor(buffered=True)

# mycursor.execute("CREATE DATABASE itemsTable") #comment out/
mycursor.execute("USE itemsTable")
# mycursor.execute("CREATE TABLE Items (ItemTypeNum smallint UNSIGNED, GOATID VARCHAR(100), EnteredName VARCHAR(1000), Name VARCHAR(1000), Color VARCHAR(100), Size VARCHAR(3), RetailPrice smallint UNSIGNED, ReleaseDate VARCHAR(1000), LastUpdated VARCHAR(1000), CountryManufactured VARCHAR(15), GOATLowestAsk smallint UNSIGNED, STOCKXLowestAsk smallint UNSIGNED, STOCKXLowestAskSize VARCHAR(15), GOATLastSoldPrice smallint UNSIGNED, STOCKXLastSoldPrice smallint UNSIGNED, STOCKXLastSoldPriceSize VARCHAR(15), OverUnderRetailStockx smallint UNSIGNED, OverUnderRetailGoat smallint UNSIGNED)")
#this function adds items to database
def add_to_database(itemTypeNum, goatID, enteredname, name, color, size, retail, releaseDate, lastUpdated, origin, lowestAskGoat,lowestAskSTOCKX, lowestAskSTOCKXSize, lastSoldPriceGOAT,lastSoldPriceStockx,lastSoldPriceSizeStockx,overUnderRetailStockx,overUnderRetailGoat):  
    mycursor.execute("INSERT INTO Items (ItemTypeNum,GOATID,EnteredName,Name,Color,Size, RetailPrice, ReleaseDate, LastUpdated, CountryManufactured, GOATLowestAsk, STOCKXLowestAsk, STOCKXLowestAskSize,GOATLastSoldPrice,STOCKXLastSoldPrice,STOCKXLastSoldPriceSize,OverUnderRetailStockx,OverUnderRetailGoat) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(itemTypeNum, goatID, enteredname, name, color, size, retail,releaseDate,lastUpdated,origin,lowestAskGoat,lowestAskSTOCKX, lowestAskSTOCKXSize, lastSoldPriceGOAT,lastSoldPriceStockx,lastSoldPriceSizeStockx,overUnderRetailStockx,overUnderRetailGoat))
    db.commit()



def testupdateGOATLowestAsk(): #changes item price, manually
    cursor =db.cursor()
    name = 'Supreme Pine Green Crewneck Box Logo'
    changeprice = 1000
    sql = "UPDATE Items SET STOCKXLowestAsk =%s WHERE EnteredName ='%s'"%(changeprice,name)
    cursor.execute(sql)
    db.commit()   

def getSizeNum(name,itemType,size):#gets respective size num thats on web for scrape
    clothing_sizes = {'s':'0', 'm':'1', 'l':'2', 'xl':'3', 'xxl': '4'} #dictionary
    sizeOfItem = clothing_sizes.pop(size)
    return sizeOfItem 

def getShoeSizeNum(name,size):
    shoe_sizes = {'4':'0','4.5':'1','5':'2', '5.5':'3','6':'4','6.5':'5','7':'8'} #dictionary
    shoeSizeScrapeNum = shoe_sizes.pop(size) #corresponding num for scrape online goat
    return shoeSizeScrapeNum 

def updateGOATLowestAsk(nameOfItem,itemType,itemSize):
    sizeNum = getSizeNum(nameOfItem,itemType,itemSize) #size of item number that corresponds to scraping size num
    updatedGoatLowestAsk = get_lowestAsk(nameOfItem,sizeNum) #gets updated goat LowestAsk

    cursor =db.cursor()
    name = nameOfItem
    changeprice = updatedGoatLowestAsk
    sql = "UPDATE Items SET GOATLowestAsk =%s WHERE EnteredName ='%s'"%(changeprice,name)
    cursor.execute(sql)
    db.commit()

def updateStockXLowestAsk(nameOfItem):
    updatedStockXLowestAsk = get_lowest_ask_price(nameOfItem) #gets updated Stockx LowestAsk

    cursor =db.cursor()
    name = nameOfItem
    changeprice = updatedStockXLowestAsk
    sql = "UPDATE Items SET STOCKXLowestAsk =%s WHERE EnteredName ='%s'"%(changeprice,name)
    cursor.execute(sql)
    db.commit()

def updateStockXLowestAskSize(nameOfItem):
    updatedStockXLowestAskSize = get_lowest_ask_size(nameOfItem) #gets updated Stockx LowestAsk Size

    cursor =db.cursor()
    name = nameOfItem
    changesize = updatedStockXLowestAskSize
    sql = "UPDATE Items SET STOCKXLowestAskSize ='%s' WHERE EnteredName ='%s'"%(changesize,name) #for size make sure to put '' in %s
    cursor.execute(sql)
    db.commit()

def updateGoatLastSoldPrice(nameOfItem,itemType,itemSize):
    sizeNum = getSizeNum(nameOfItem,itemType,itemSize) #size of item number that corresponds to scraping size num
    updatedGoatLastSoldPrice = get_last_sold_price(nameOfItem,sizeNum) #gets updated Goat Last Sold Price
    
    cursor =db.cursor()
    name = nameOfItem
    changeprice = updatedGoatLastSoldPrice
    sql = "UPDATE Items SET GOATLastSoldPrice =%s WHERE EnteredName ='%s'"%(changeprice,name)
    cursor.execute(sql)
    db.commit()


def updateSHOEGOATLowestAsk(nameOfItem,itemID,itemType,itemSize):
    sizeNum = getShoeSizeNum(nameOfItem,itemSize)
    updatedGoatLowestAsk = getShoeLowestAskGoat(itemID,sizeNum) #gets updated goat LowestAsk

    cursor =db.cursor()
    name = nameOfItem
    changeprice = updatedGoatLowestAsk
    sql = "UPDATE Items SET GOATLowestAsk =%s WHERE EnteredName ='%s'"%(changeprice,name)
    cursor.execute(sql)
    db.commit()

def updateTimeNDate(nameOfItem):
    dateNTime = getDateNTime()
    cursor =db.cursor()
    name = nameOfItem
    sql = "UPDATE Items SET LastUpdated ='%s' WHERE EnteredName ='%s'"%(dateNTime,name)
    cursor.execute(sql)
    db.commit()

def getDateNTime():
    now = datetime.now()
    return(now.strftime('%Y-%m-%d %I:%M:%S'))


def updateItemChanges(): #updates an items lowest ask, lowest ask size, last sold price etc. 
    i = 0
    mycursor.execute("SELECT * FROM Items")
    row = mycursor.fetchone()
   
    while row is not None: #iterates through all entries in the database and updates prices
        nameOfItem = row[2]
        itemType = row[0]
        itemSize = row [5]
        itemID = row[1]

        if itemType == 1 or itemType == 3:
            updateGOATLowestAsk(nameOfItem,itemType,itemSize) #updates Goat Lowest Ask Price
            updateStockXLowestAsk(nameOfItem) #updates StockX Lowest Ask Price
            updateStockXLowestAskSize(nameOfItem) #updates StockX Lowest Ask Price Size
            updateGoatLastSoldPrice(nameOfItem,itemType,itemSize) #updates Goat Last Sold Price
            updateTimeNDate(nameOfItem)
        if itemType == 2:
            updateSHOEGOATLowestAsk(nameOfItem,itemID,itemType,itemSize)
            updateTimeNDate(nameOfItem)

        row = mycursor.fetchone()
        i = i + 1
        print("while loop ran: ", i)


    # for x in range(0,3):
    #     row = mycursor.fetchone()
    #     # itemTypeNum = row[0]
    #     name = row[1]
    #     # size = row[4]
    #     goatLowestAsk = 300 #getLowestAskGoat(name,itemTypeNum,size)
    #     print(row[1])
    #     update(goatLowestAsk,name)      
    #     print("operation done")  
    #     row = mycursor.fetchone()

    # while row is not None:
    #     itemTypeNum = row[0]
    #     name = row[1]
    #     size = row[4]
    #     goatLowestAsk = 300 #getLowestAskGoat(name,itemTypeNum,size)
    #     print(row[1])
    #     update(goatLowestAsk,name)      
    #     print("operation done")  
    #     row = mycursor.fetchone()
    #     # goatLowestAsk = goatLowestAsk + 1
        
        
        
         
    

    # print("hi")
    # mycursor.execute("UPDATE Items SET GOATLowestAsk = 1 WHERE EnteredName = 'Supreme Box Logo Pine Green Crewneck'")

#     mycursor = db.cursor()
#     mycursor.execute("SELECT * FROM Items")
    
#     enteredName = mycursor.fetchone()[0]
#     name = mycursor.fetchone()[1]
#     color = mycursor.fetchone()[2]
#     size = mycursor.fetchone()[3]

   
#     print(result)
   
   
   
   
    # numrows = mycursor.rowcount
    # numrows = numrows + 3
    # print(numrows)
    # for x in range(0,numrows):
    #     row = mycursor.fetchone()
    #     print (row[0])
    
        # result = mycursor.fetchone()[i]    
        # print(result)
        # print(i)   
        # i = i + 1
       




