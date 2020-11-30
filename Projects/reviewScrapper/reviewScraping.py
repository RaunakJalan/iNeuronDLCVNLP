from bs4 import BeautifulSoup
import pymongo
import scrapy
import requests

url = "https://www.flipkart.com/realme-narzo-20-glory-silver-64-gb/p/itm4ac58d879006d?pid=MOBFVEATBBRGJBKH&lid=LSTMOBFVEATBBRGJBKH4OKPVI&marketplace=FLIPKART&srno=s_1_3&otracker=search&otracker1=search&fm=SEARCH&iid=fd57f73e-72f3-4e01-a8f6-11932d452473.MOBFVEATBBRGJBKH.SEARCH&ppt=sp&ppn=sp&ssid=29j5rntx0mp8c1s01606757338074&qH=bcdc2513ea0bb0e5"

req_data = requests.get(url)
review_soup = BeautifulSoup(req_data.content, 'html.parser')
# print(review_soup)

all_reviews = review_soup.find_all('div', {'class':'col JOpGWq'})
# print(all_reviews)

rating_list = []
review_header_list = []
detailed_review_list = []
user_list = []
likes_dislikes_list = []

# pages_total = review_soup.find_all('div',{'class':'_2MImiq _1Qnn1K'})

# print(review_soup)

for review in all_reviews:
    rating = review.find_all('div', {'class':'_3LWZlK _1BLPMq'})
    rating = [e.get_text() for e in rating]
    review_header = review.find_all('p', {'class':'_2-N8zT'})
    review_header = [e.get_text() for e in review_header]
    detailed_review = review.find_all('div', {'class':'t-ZTKy'})
    detailed_review = [e.get_text() for e in detailed_review]
    user = review.find_all('p', {'class':'_2sc7ZR _2V5EHH'})
    user = [e.get_text() for e in user]
    likes_dislikes = review.find_all('span', {'class': '_3c3Px5'})
    likes_dislikes = [e.get_text() for e in likes_dislikes]

    rating_list.append(rating)
    review_header_list.append(review_header)
    detailed_review_list.append(detailed_review)
    user_list.append(user)
    likes_dislikes_list.append(likes_dislikes)

# print(rating_list)
# print('*'*50)
# print(review_header_list)
# print('*'*50)
# print(detailed_review_list)
# print('*'*50)
# print(user_list)
# print('*'*50)
# print(likes_dislikes_list)
# print('*'*50)
