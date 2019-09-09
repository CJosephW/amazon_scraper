from nltk.corpus import stopwords 
import urllib.request
import nltk
from json import dumps, loads
import json
from re import sub
import time
from requests import get
from nltk.tokenize import sent_tokenize
from selenium import webdriver

driver = webdriver.Firefox()
def search(search_keyword):
    
    driver.get('https://www.amazon.com/s?k='+ search_keyword + '&ref=nb_sb_noss_1')
    time.sleep(5)
    search_index = 1
    results = driver.find_elements_by_css_selector("span.a-size-base-plus.a-color-base.a-text-normal")

    for result in results:
        print(str(search_index)+ ' ' + result.text)
        search_index += 1

    search_choice = input('please select search result by the number provided')
    search_choice = int(search_choice)
    results[search_choice].click()
    time.sleep(3)
    product_details = driver.find_elements_by_tag_name('li')
    for item in product_details:
        if len(item.text) == 10:
            asin = item.text
                
    print(asin)

def parse_reviews():
    
    reviews = []
    review_elements = []
    
    for i in range(3):#get 3 pages worth of reviews or 30 reviews
        
        page_num = str(i + 1)
        
        driver.get('https://www.amazon.com/product-reviews/B07TZKFJBX/ref=cm_cr_getr_d_show_all?ie=UTF8&reviewerType=all_reviews&pageNumber='+(page_num)+'&sortBy=recent')#gets each page and sorts by most recent
        review_elements = driver.find_elements_by_xpath("//*[@class = 'a-size-base review-text review-text-content']/span")
        
        reviews += [review.text for review in review_elements]#puts each review in a list
        
        time.sleep(5)#gives the page time to load

    for review in reviews:#iterates through each item in list
        
        print(review + 'END OF REVIEW')

search_input = input('please enter what you would like to search: ')
search(search_input)

