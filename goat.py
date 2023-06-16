#https://www.youtube.com/watch?v=cEtROmrxK2E&t=130s
import requests
import json
import cloudscraper
import decimal


#search to get product id
def search(query):
      #bypas bot protection
      headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'dnt': '1',
            'origin': 'https://www.goat.com',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
      }
      #retrieves stored market data through GOAT's api
      url = f'https://ac.cnstrc.com/search/{query.replace(" ","%20")}?c=ciojs-client-2.27.9&key=key_XT7bjdbvjgECO5d8&i=0d562b86-f8cf-4b44-8277-ca435324260e&s=2&num_results_per_page=25&_dt=1653046311601'
      #after obtaining API link, we create an html request
      html = requests.get(url=url, headers=headers)
       #convert html request to a json file
      output = json.loads(html.text)
      # print("goat url", url)
      return output['response']['results'][0]

#same process, this new search allows us to get specific size data
def new_search(query,index_item):
      headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'dnt': '1',
            'origin': 'https://www.goat.com',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"101\", \"Google Chrome\";v=\"101\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1"
      }
      url = f'https://www.goat.com/web-api/v1/product_variants/buy_bar_data?productTemplateId={query}&countryCode=US'
      print(url,"shoesy")
      html = requests.get(url=url, headers=headers) 
      # https://stackoverflow.com/questions/49087990/python-request-being-blocked-by-cloudflare
      scraper = cloudscraper.create_scraper()
      html = scraper.get(url).text 
      output = json.loads(html)
      
      return output[int(index_item)]

# def shoenew_search(query,index_item):
#       headers = {
#             'accept': '*/*',
#             'accept-encoding': 'gzip, deflate, br',
#             'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
#             'dnt': '1',
#             'origin': 'https://www.goat.com',
#             'sec-fetch-dest': 'empty',
#             'sec-fetch-mode': 'cors',
#             'sec-fetch-site': 'cross-site',
#             'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
#             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#             "accept-language": "en-US,en;q=0.9",
#             "cache-control": "no-cache",
#             "pragma": "no-cache",
#             "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"101\", \"Google Chrome\";v=\"101\"",
#             "sec-ch-ua-mobile": "?0",
#             "sec-ch-ua-platform": "\"Windows\"",
#             "sec-fetch-dest": "document",
#             "sec-fetch-mode": "navigate",
#             "sec-fetch-site": "none",
#             "sec-fetch-user": "?1",
#             "upgrade-insecure-requests": "1"
#       }
#       url = f'https://www.goat.com/web-api/v1/product_variants/buy_bar_data?productTemplateId={query}&countryCode=US'
#       # print(url)
#       html = requests.get(url=url, headers=headers) 
#       # https://stackoverflow.com/questions/49087990/python-request-being-blocked-by-cloudflare
#       scraper = cloudscraper.create_scraper()
#       html = scraper.get(url).text 
#       output = json.loads(html)
#       return output[int(index_item)]
#     #   print (y)
#     #   print(html.text)

# def shoeSearch(query):
#       headers = {
#             'accept': '*/*',
#             'accept-encoding': 'gzip, deflate, br',
#             'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
#             'dnt': '1',
#             'origin': 'https://www.goat.com',
#             'sec-fetch-dest': 'empty',
#             'sec-fetch-mode': 'cors',
#             'sec-fetch-site': 'cross-site',
#             'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
#       }
#       url = f'https://www.goat.com/web-api/v1/product_variants/buy_bar_data?productTemplateId={query}&countryCode=US'
#       # print("url for shoes ID: ", url)
#       html = requests.get(url=url,headers=headers)
#       print(html)
#       scraper = cloudscraper.create_scraper()
#       html = scraper.get(url).text 
#       output = json.loads(html.text)
      # print("goat url", url)
      # print (output[0])
      # return output[0]

#CLOTHING/ACCESSORIES
def get_lowestAsk(name_of_item, item_index):
    print('Lowest Ask')
    item = search(name_of_item)
    id = item['data']['id'] #don't touch/change/remove
    # print(id)
    item = new_search(id,item_index)
    print(item, item_index)
    lowestAskSize = item['lowestPriceCents']['amount']
    cents = lowestAskSize
    dollars = decimal.Decimal(cents) / 100
    return(dollars)

def get_last_sold_price(name_of_item, item_index):
    print('Last Sold Price')
    id = getProductID(name_of_item)
    # print(id)
    item = new_search(id,item_index)
    lowestAskSize = item['lastSoldPriceCents']['amount']
    cents = lowestAskSize
    dollars = decimal.Decimal(cents) / 100
    return(dollars)    

def getProductID(name_of_item): #function only for shoes
      item = search(name_of_item)
      # print(item,"ingetProductID")
      id = item['data']['id'] #don't touch/change/remove
      # print("Shoe ID: ", id)
      return(id)

#SHOES

def getShoeLowestAskGoat(id,item_index):
      # print('Shoe Price')
      item = new_search(id,item_index)
      lowestAskSize = item['lowestPriceCents']['amount']
      cents = lowestAskSize
      dollars = decimal.Decimal(cents) / 100
      return(dollars)    

def getShoeLastSoldPriceGoat(id,item_index):
      # print('Shoe Price')
      item = new_search(id,item_index)
      lowestAskSize = item['lastSoldPriceCents']['amount']
      cents = lowestAskSize
      dollars = decimal.Decimal(cents) / 100
      return(dollars)    





    # value = new_item['item_index']['sizeOption']









