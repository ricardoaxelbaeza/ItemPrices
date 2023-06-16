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
# from database import add_to_database
# from database import retrieve_db_value



#initialize

def getProductInfo(self, productName,itemType,itemSize): 
    global name_of_item 
    global item_type #we want 1, 2,3
    global item_size # we want numbers here

    name_of_item = productName
    item_type = itemType
    item_size = itemSize
         

def getLowestAskGoat(productName,itemTypeNum,itemSize):
    if int(itemTypeNum) == 1:
        clothing_sizes = {'s':'0', 'm':'1', 'l':'2', 'xl':'3', 'xxl': '4'} #dictionary
        print("You chose clothing")

        size_of_item = input("What is the size of your item? (s/m/l/xl)? ")
        size = clothing_sizes.pop(size_of_item)
        print(size)
        #store 
            
        item_lowest_ask_goat = get_lowestAsk(name_of_item,size) #goat
        return item_lowest_ask_goat

def getLowestAskStockX(self,productName,itemTypeNum,itemSize):
    if int(itemTypeNum) == 1:
        clothing_sizes = {'s':'0', 'm':'1', 'l':'2', 'xl':'3', 'xxl': '4'} #dictionary
        print("You chose clothing")

        size_of_item = input("What is the size of your item? (s/m/l/xl)? ")
        size = clothing_sizes.pop(size_of_item)
        print(size)
        #store 
            
        item_lowest_ask_stockx = get_lowest_ask_price(name_of_item) #stockx
        return item_lowest_ask_stockx

    #  def getLowestAskStockXSize(self,productName,itemTypeNum,itemSize):
    #      if int(itemTypeNum) == 1:
    #         clothing_sizes = {'s':'0', 'm':'1', 'l':'2', 'xl':'3', 'xxl': '4'} #dictionary
    #         print("You chose clothing")

    #         size_of_item = input("What is the size of your item? (s/m/l/xl)? ")
    #         size = clothing_sizes.pop(size_of_item)
    #         print(size)
    #         #store 
            
    #         item_lowest_ask_size_stockx = get_lowest_ask_size(name_of_item) #stockx
    #         return item_lowest_ask_size_stockx

def getLastSoldPriceGoat(self,productName,itemTypeNum,itemSize):
    if int(itemTypeNum) == 1:
        clothing_sizes = {'s':'0', 'm':'1', 'l':'2', 'xl':'3', 'xxl': '4'} #dictionary
        print("You chose clothing")

        size_of_item = input("What is the size of your item? (s/m/l/xl)? ")
        size = clothing_sizes.pop(size_of_item)
        print(size)
        #store 
            
        item_last_sold_price_goat = get_last_sold_price(name_of_item,size) #goat
        return item_last_sold_price_goat
    
            
            
           
           
            
            # item_highest_bid_stockx = highest_bid_price(name_of_item) #stockx
            # item_highest_bid_size_stockx = highest_bid_size(name_of_item) #stockx






        