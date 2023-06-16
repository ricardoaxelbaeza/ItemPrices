
from goat import get_lowestAsk
from goat import get_last_sold_price
from stockx import get_item_name
from stockx import get_item_color
from stockx import get_retail_price
from stockx import get_country_of_manufacture
from stockx import get_lowest_ask_price
from stockx import get_lowest_ask_size
from stockx import highest_bid_price
from stockx import highest_bid_size
from database import add_to_database
from database import updateItemChanges
from database import testupdateGOATLowestAsk
from stockx import get_release_date
from goat import getProductID
from goat import getShoeLowestAskGoat
from database import getDateNTime
from goat import getShoeLastSoldPriceGoat
from stockx import get_last_sold_price_stockx
from stockx import get_last_sold_price_size_stockx
# from goat import getShoePrice




# from database import update


def getUsersNumOfItems(): #gets the num of items a user wants to add
    numOfItems = int(input("How many items would you like to add? "))
    i = 0
    if(numOfItems) == 0:
            print("ran")
            updateItemChanges() #updates/refreshes last sold price, etc. in database
    else: 
        for i in range(int(numOfItems)):
            print("Entries Left : ", numOfItems - i)
            if (numOfItems) > 0: 
                addItem() #add items to database


def addItem():

    print("Make sure you enter the name as it appears on StockX")
    #asks the user for their items name
    name_of_item = input("What is the name of your item? ")
    #ask the user for item type(clothing, shoes or accessory)
    itemType = identifyItemType() # itemType number
    

    if int(itemType) == 1: #clothing
        clothingSizeL = getClothingSizeLetter() 
        clothingSizeN = getClothingSizeNum(clothingSizeL) #for indexing into Json file
        #retrieve scraped data from StockX and GOAT and write it to the DB
        retrieveScrapedDataAndWriteToDB(name_of_item,clothingSizeN,itemType,clothingSizeL)

    if int(itemType) == 2: #shoes
        print("You selected shoes")
        shoeSizeL = getShoeSizeL()
        shoeSizeNumScrape = getShoeSizeN(shoeSizeL) #respective goat scrape num
        shoeID = getShoeID(name_of_item) #gets id from goat
        shoeretrieveScrapedDataAndWriteToDB(name_of_item,shoeID,shoeSizeNumScrape,itemType,shoeSizeL)
        # shoePrice = getShoePrice(shoeID,shoeSizeNumScrape)
        # print("price of shoes:", shoePrice)

#         print("You chose shoes")
    if int(itemType) == 3: #accessory
        accessoryN = 0 #accessory number
        accessoryL = ''
        retrieveScrapedDataAndWriteToDB(name_of_item,accessoryN,itemType,accessoryL)


def identifyItemType():
    item_type_num = input("Enter Item Type: (1) Clothing, (2) Shoes, (3) Accessory: ")

    while ((int(item_type_num) > 3) or (int(item_type_num) < 1)) : #makes user select correct choice
        shoe_or_clothing = input("Please Enter Your Correct Item Type: (1) Clothing, (2) Shoes, (3) Accessory: ")
        if int(shoe_or_clothing) <= 3:
            break

    return item_type_num

# def getDateNTime():
#     now = datetime.now()
#     return now.strftime('%Y-%m-%d %I:%M:%S')

def getClothingSizeLetter():
    print("You chose clothing.")
    size_of_item = input("What is the size of your item? (s/m/l/xl)? ")
    return size_of_item

def getClothingSizeNum(size_of_item):
    clothing_sizes = {'s':'0', 'm':'1', 'l':'2', 'xl':'3', 'xxl': '4'} #dictionary
    size = clothing_sizes.pop(size_of_item)
    return size

                                                #number             #letter
#function that calls functions in goat.py and stockx.py to retrieve data from StockX and GOAT
#other data is also formulated (lastupdated)
def retrieveScrapedDataAndWriteToDB(name_of_item,size,item_type_num,size_of_item):
    lastUpdated = getDateNTime()
    entered_name = name_of_item
    productID = getProductID(name_of_item)
    item_type = item_type_num #data that could hopefully be useful for going through
    item_size = size_of_item
    item_name = get_item_name(name_of_item) #stockx
    item_color = get_item_color(name_of_item) #stockx
    item_retail_price = get_retail_price(name_of_item) #stockx
    item_country_of_manufacture = get_country_of_manufacture(name_of_item)#stockx
    item_lowest_ask_goat = get_lowestAsk(name_of_item,size) #goat
    item_last_sold_price_goat = get_last_sold_price(name_of_item,size) #goat
    item_lowest_ask_stockx = get_lowest_ask_price(name_of_item) #stockx
    item_lowest_ask_size_stockx = get_lowest_ask_size(name_of_item) #stockx
    item_highest_bid_stockx = highest_bid_price(name_of_item) #stockx
    item_highest_bid_size_stockx = highest_bid_size(name_of_item) #stockx
    itemReleaseDate = get_release_date(name_of_item)
    lastSoldPriceStockx = get_last_sold_price_stockx(name_of_item) #stockx
    lastSoldPriceSizeStockx = get_last_sold_price_size_stockx(name_of_item) #stockx

    overUnderRetailStockx = lastSoldPriceStockx - item_retail_price
    overUnderRetailGoat = item_last_sold_price_goat - item_retail_price

    add_to_database(item_type,productID,entered_name ,item_name, item_color,item_size, item_retail_price,itemReleaseDate,lastUpdated,item_country_of_manufacture,item_lowest_ask_goat,item_lowest_ask_stockx,item_lowest_ask_size_stockx,item_last_sold_price_goat,lastSoldPriceStockx,lastSoldPriceSizeStockx,overUnderRetailStockx,overUnderRetailGoat)

                                                     #number             #letter ()
def shoeretrieveScrapedDataAndWriteToDB(name_of_item,shoeID,shoeSizeNumScrape,item_type_num,size_of_item):
    lastUpdated = getDateNTime()
    entered_name = name_of_item
    productID = getProductID(name_of_item)
    item_name = get_item_name(name_of_item) #stockx
    item_color = get_item_color(name_of_item) #stockx
    item_country_of_manufacture = get_country_of_manufacture(name_of_item)#stockx
    item_size = size_of_item
    itemReleaseDate = get_release_date(name_of_item)
    item_lowest_ask_stockx = get_lowest_ask_price(name_of_item) #stockx
    item_retail_price = get_retail_price(name_of_item) #stockx
    item_lowest_ask_size_stockx = get_lowest_ask_size(name_of_item) #stockx
    item_lowest_ask_goat = getShoeLowestAskGoat(shoeID,shoeSizeNumScrape)
    item_last_sold_price_goat = getShoeLastSoldPriceGoat(shoeID,shoeSizeNumScrape)
    item_type = item_type_num #data that could hopefully be useful for going through
    lastSoldPriceStockx = get_last_sold_price_stockx(name_of_item) #stockx
    lastSoldPriceSizeStockx = get_last_sold_price_size_stockx(name_of_item) #stockx

    overUnderRetailStockx = lastSoldPriceStockx - item_retail_price
    overUnderRetailGoat = item_last_sold_price_goat - item_retail_price
    
    add_to_database(item_type,productID,entered_name ,item_name, item_color,item_size, item_retail_price,itemReleaseDate,lastUpdated,item_country_of_manufacture,item_lowest_ask_goat,item_lowest_ask_stockx,item_lowest_ask_size_stockx,item_last_sold_price_goat,lastSoldPriceStockx,lastSoldPriceSizeStockx,overUnderRetailStockx,overUnderRetailGoat)

    # add_to_database(item_type,entered_name ,item_name, item_color,item_size, item_retail_price,itemReleaseDate,item_country_of_manufacture,item_lowest_ask_goat,item_lowest_ask_stockx,item_lowest_ask_size_stockx,item_last_sold_price_goat)

def getShoeSizeL():
    shoeSize = input("Enter shoe size: ")
    return shoeSize

def getShoeSizeN(shoeSize):
    shoeSize = input("Enter shoe size: ")
    shoe_sizes = {'4':'0','4.5':'1','5':'2', '5.5':'3','6':'4','6.5':'5','7':'8','7.5':'9','8':'10','8.5':'11','9':'12','9.5':'13','10':'14','10.5':'15','11':'16','11.5':'17','12':'18','12.5':'19','13':'20','13.5':'21','14':'22s'} #dictionary
    shoeSizeScrapeNum = shoe_sizes.pop(shoeSize) #corresponding num for scrape online goat
    return shoeSizeScrapeNum

def getShoeID(shoeName):
    productID = getProductID(shoeName)
    return(productID)


getUsersNumOfItems()



#Gets user input to how many items they would like to add
# getUsersNumOfItems(name_of_item,size):



# if int(num_of_items) > 0:
#     print("Make sure you enter the name as it appears on StockX")
#     name_of_item = input("What is the name of your item? ")
    
#     item_type_num = input("Enter Item Type: (1) Clothing, (2) Shoes, (3) Accessory: ")

#     while ((int(item_type_num) > 3) or (int(item_type_num) < 1)) : #makes user select correct choice
#         shoe_or_clothing = input("Please Enter Your Correct Item Type: (1) Clothing, (2) Shoes, (3) Accessory: ")
#         if int(shoe_or_clothing) <= 3:
#             break
#     if int(item_type_num) == 1:
#         clothing_sizes = {'s':'0', 'm':'1', 'l':'2', 'xl':'3', 'xxl': '4'} #dictionary
#         print("You chose clothing")

#         size_of_item = input("What is the size of your item? (s/m/l/xl)? ")
#         size = clothing_sizes.pop(size_of_item)
#         print(size)

#         #store 

#         entered_name = name_of_item

#         item_type = item_type_num #data that could hopefully be useful for going through
#         item_size = size_of_item
#         item_name = get_item_name(name_of_item) #stockx
#         item_color = get_item_color(name_of_item) #stockx
#         item_retail_price = get_retail_price(name_of_item) #stockx
#         item_country_of_manufacture = get_country_of_manufacture(name_of_item)#stockx
       
#         item_lowest_ask_goat = get_lowestAsk(name_of_item,size) #goat
#         item_last_sold_price_goat = get_last_sold_price(name_of_item,size) #goat

#         item_lowest_ask_stockx = get_lowest_ask_price(name_of_item) #stockx
#         item_lowest_ask_size_stockx = get_lowest_ask_size(name_of_item) #stockx

#         item_highest_bid_stockx = highest_bid_price(name_of_item) #stockx
#         item_highest_bid_size_stockx = highest_bid_size(name_of_item) #stockx

#         add_to_database(item_type,entered_name ,item_name, item_color,item_size, item_retail_price,item_country_of_manufacture,item_lowest_ask_goat,item_lowest_ask_stockx,item_lowest_ask_size_stockx,item_last_sold_price_goat)
    

#     elif int(shoe_or_clothing) == 2:
#         # shoe_sizes = {'4':'0','4.5':'1','5':'2', } #dictionary
#         print("You chose shoes")

#     elif int(shoe_or_clothing) == 3:
#         # shoe_sizes = {'4':'0','4.5':'1','5':'2', } #dictionary
#         print("You chose shoes")
#     else:
#         print("You chose an accessory")


# else: 
#     #here we'll take the items stored and run through them
#     updateItemChanges()
#     # testupdateGOATLowestAsk()
    

