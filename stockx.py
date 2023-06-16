#https://www.youtube.com/watch?v=bLCx348H0Kw&t=584s
import requests
import json

#Gets user input to how many items they would like to add
# num_of_items = input("How many items would you like to add?")

name_of_item = 'Supreme Box Logo Crewneck (FW22) Dark Pine'
new_name = name_of_item.replace(" ", "%20")

# print (new_name)

def search(query): #retrieves stored market data through stockX's api
    url = f'https://stockx.com/api/browse?_search={query}'
                                                   #name of item goes into query
                                                   #and the corresponding API Link for specific item is obtained

    #bypass bot protection
    headers = {
        'accept': 'application/json',
        'accept-encoding': 'utf-8',
        'accept-language': 'en-GB,en;q=0.9',
        'app-platform': 'Iron',
        'referer': 'https://stockx.com/en-gb',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    #after obtaining API link, we create an html request
    html = requests.get(url=url, headers=headers)
    #convert html request to a json file
    output = json.loads(html.text)
    return output['Products'][0]

    

def getPrices():#Stores prices and other data
    item = search(new_name)
    #Store
    #Lowest Ask
    #Last Sale
    
    #item info  //interesting note: for some they are not under media, browseverticals, they are just the name as is to get data
    itemName = item['title']
    countryOfManufacture = item['countryOfManufacture']
    brand = item['brand']
    color = item['colorway']
    releaseDate = item['releaseDate']
    urlKey = item['urlKey']
    retailPrice = item['retailPrice']   #note: datatype is int
    belowRetail = item['belowRetail']   #note: datatypes is boolean
   
    # #lowest ask info
    lowestAskSize = item['market']['lowestAskSize']
    lowestAsk = item['market']['lowestAsk'] #note: datatype is int
    
    # #bid info
    highestBidSize = item['market']['highestBidSize']
    highestBid = item['market']['highestBid']   #note: datatype is int
    
    # #sale info
    lastSaleSize = item['market']['lastSaleSize']
    lastSale = item['market']['lastSale']   #note: datatype is int

    # #other
    numberOfAsks = item['market']['numberOfAsks']   #note: datatype is int
    annualHigh = item['market']['annualHigh']   #note: datatype is int
    annualLow = item['market']['annualLow'] #note: datatype is int
    pricePremium = item['market']['pricePremium']   #note: datatype is int
    salesLast72Hours = item['market']['salesLast72Hours']   #note: datatype is int
    
    print(salesLast72Hours)


def get_item_name(name_of_item): 
    item = search(name_of_item) 
    itemName = item['title']
    return (itemName)
    
def get_item_color(name_of_item):
    item = search(name_of_item)
    itemColor = item['colorway']
    return (itemColor)

def get_retail_price(name_of_item):
    item = search(name_of_item)
    itemRetail = item['retailPrice']
    return (itemRetail)

def get_country_of_manufacture(name_of_item):
    item = search(name_of_item)
    countryOfManufacture = item['countryOfManufacture']
    return (countryOfManufacture)

def get_lowest_ask_price(name_of_item):
    item = search(name_of_item)
    lowestAskPrice = item['market']['lowestAsk']
    return (lowestAskPrice)

def get_lowest_ask_size(name_of_item):
    item = search(name_of_item)
    lowestAskSize = item['market']['lowestAskSize']
    return (lowestAskSize)

def highest_bid_price(name_of_item):
    item = search(name_of_item)
    highestBid = item['market']['highestBid']
    return (highestBid)

def highest_bid_size(name_of_item):
    item = search(name_of_item)
    highestBidSize = item['market']['highestBidSize']
    return (highestBidSize)

def get_release_date(name_of_item):
    item = search(name_of_item)
    releaseDate = item['releaseDate']
    return (releaseDate)

def get_last_sold_price_stockx(name_of_item):
    item = search(name_of_item)
    lastSoldPrice = item['market']['lastSale']   #note: datatype is int
    return (lastSoldPrice)

def get_last_sold_price_size_stockx(name_of_item):
    item = search(name_of_item)
    lastSaleSize = item['market']['lastSaleSize']
    return (lastSaleSize)

