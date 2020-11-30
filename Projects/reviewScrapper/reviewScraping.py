from bs4 import BeautifulSoup
import requests

url = "https://www.flipkart.com/realme-narzo-20-glory-silver-64-gb/p/itm4ac58d879006d?pid=MOBFVEATBBRGJBKH&lid=LSTMOBFVEATBBRGJBKH4OKPVI&marketplace=FLIPKART&srno=s_1_3&otracker=search&otracker1=search&fm=SEARCH&iid=fd57f73e-72f3-4e01-a8f6-11932d452473.MOBFVEATBBRGJBKH.SEARCH&ppt=sp&ppn=sp&ssid=29j5rntx0mp8c1s01606757338074&qH=bcdc2513ea0bb0e5"

req_data = requests.get(url)
review_soup = BeautifulSoup(req_data.content, 'html.parser')

# print(review_soup)


rating_list = []
review_header_list = []
detailed_review_list = []
user_list = []
likes_dislikes_list = []

baseUrl = 'https://www.flipkart.com'

pages_total = review_soup.find('div',{'class':'_3UAT2v _16PBlm'})

review_link = str(pages_total.find_parent().get('href'))
url = baseUrl + review_link
c=0
while True:
    c+=1
    print(url)
    print('*'*100)
    req_data = requests.get(url)
    review_soup = BeautifulSoup(req_data.content, 'html.parser')

    all_reviews = review_soup.find_all('div', {'class':'col _2wzgFH K0kLPL'})
    #print(all_reviews)
    page_rating = []
    page_review = []
    page_detailed = []
    page_user = []
    page_like_dis = []
    for review in all_reviews:
        rating = review.find('div', {'class':'_3LWZlK _1BLPMq'})
        if rating == None:
            rating  = review.find('div',{'class':'_3LWZlK _1rdVr6 _1BLPMq'})
        if rating == None:
            rating  = review.find('div',{'class':'_3LWZlK _32lA32 _1BLPMq'})
        rating = rating.text
        review_header = review.find('p', {'class':'_2-N8zT'}).text
        detailed_review = review.find('div', {'class':'t-ZTKy'}).text
        user = review.find('p', {'class':'_2sc7ZR _2V5EHH'}).text
        likes_dislikes = review.find_all('span', {'class': '_3c3Px5'})
        likes_dislikes = [e.get_text() for e in likes_dislikes]

        page_rating.append(rating)
        page_review.append(review_header)
        page_detailed.append(detailed_review)
        page_user.append(user)
        page_like_dis.append(likes_dislikes)


    rating_list.append(page_rating)
    review_header_list.append(page_review)
    detailed_review_list.append(page_detailed)
    user_list.append(page_user)
    likes_dislikes_list.append(page_like_dis)

    review_links = review_soup.find_all('a',{'class':'_1LKTO3'})
    if len(review_links)==1:
        if review_links[0].get_text()=="Previous":
            break
        else:
            url = baseUrl + str(review_links[0].get('href'))
    elif len(review_links)>1:
        url = baseUrl + str(review_links[1].get('href'))
    else:
        break
    if c==10:
        break

print(rating_list)
print('*'*50)
print(review_header_list)
print('*'*50)
print(detailed_review_list)
print('*'*50)
print(user_list)
print('*'*50)
print(likes_dislikes_list)
print('*'*50)
