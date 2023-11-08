from scrapy.http import TextResponse
import requests
import pprint
import pandas as pd

#######################################################get all data link
##make link
URL = requests.get("https://binebi.ge/gancxadebebi?deal_types=1&home_types=985&q=%E1%83%98%E1%83%A7%E1%83%98%E1%83%93%E1%83%94%E1%83%91%E1%83%90%20%E1%83%91%E1%83%98%E1%83%9C%E1%83%90%20%E1%83%A0%E1%83%A3%E1%83%A1%E1%83%97%E1%83%90%E1%83%95%E1%83%A8%E1%83%98&city=3&page=1&sort=id%2Cdesc")
response = TextResponse(URL.url, body=URL.text, encoding='utf-8')
# print(url.text)
print(response)
##get datas on 1st page
items = response.css("div.item-info span.item-title h2 a::attr(href)").getall()
# pprint.pprint(items)
print(len(items))
##create all data array and add data
ITEMS=[]
ITEMS.extend(items)
##define next page link for gathering next page data
next_page=response.css("ul.pagination.onFirstPage li.page-item.step-forward-item a::attr(href)").get()
pprint.pprint(next_page)
nexr_page_url = requests.get(next_page)
#extract data while total number is less than 200
while len(ITEMS)<230:
    response = TextResponse(nexr_page_url.url, body=nexr_page_url.text, encoding='utf-8')
    items1=response.css("div.item-info span.item-title h2 a::attr(href)").getall()
    # pprint.pprint(items1)
    ITEMS.extend(items1)
    ##clear data sub array
    items1=[]
    ##redefine next page
    next_page = response.css("ul.pagination li.page-item.step-forward-item a::attr(href)").get()
    print(next_page)
    nexr_page_url = requests.get(next_page)

# pprint.pprint(ITEMS)
print(len(ITEMS))
#######################################################extract from data links and define data arrays
price=[]
price_per_M=[]
area=[]
room=[]
bedroom=[]
state=[]
date=[]
for ITEM in ITEMS:
    url_for_item = requests.get("https://binebi.ge/" + ITEM)
    response_for_items = TextResponse(url_for_item.url, body=url_for_item.text, encoding='utf-8')
    item_info = response_for_items.css("div.col-md-3.col-xs-12.col-sm-6.p-0 div.d-block::text").extract()
    item_state = response_for_items.css("div.col-md-3.col-xs-12.col-sm-6.p-0 span.d-block.pr-1::text").extract()
    item_price_per = response_for_items.css("div.convert_strict span::text").extract()
    item_price = response_for_items.css("span.convert_sp div.price::text").extract()
    item_date = response_for_items.css("ul.m-b-0.bpg_rioni.d-flex.align-items-center li::text").extract()
    # print(item_date)
    # print(item_price)
    # print(item_state)
    if(len(item_info)!=0):
        # print(item_info)
        # print(item_price[0].strip())
        area.append(float(item_info[0][:-2]))
        if item_info[1][1:-1] == "სტუდიოს ტიპის":
            room.append(1)
        else:
            room.append((item_info[1][1]))
        bedroom.append(int(item_info[2]))
        price.append(int("".join(item_price[0].split())))
    if(len(item_state)!=0):
        state.append(" ".join(item_state))
    if(len(item_state)!=0):
        date.append(item_date[1][:-1].strip())
    price_per_M.append(int("".join(item_price_per[1].split())))
    # print(item_price_per[1])
# print(price_per_M)
# print(price)
# print(area)
# print(room)
# print(bedroom)
# print(state)
# print(date)
####################################################### move toward excel
data = {
    "date":date,
    "state":state,
    "area m2":area,
    "rooms":room,
    "bedrooms":bedroom,
    "price":price,
    "price_m2":price_per_M,
}
df = pd.DataFrame(data)
print(df)
df.to_excel('arb.project_data.xlsx',sheet_name='sheet -> I', index=False)