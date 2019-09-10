from nltk.corpus import stopwords 
import urllib.request
import nltk
from json import dumps, loads
import json
from re import sub
import time
from requests import get
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from selenium import webdriver
from nltk.tokenize import RegexpTokenizer
driver = webdriver.Firefox()
stop_words = set(stopwords.words('english'))
tokenizer = RegexpTokenizer(r'\w+')
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
    results[search_choice - 1].click()
    
    time.sleep(3)
    
    url = str(driver.current_url)
    
    asin_index = url.index('dp')
    asin_index += 3
    
    asin = url[asin_index: asin_index + 10]
    
    return asin

def parse_reviews(asin):
    
    reviews = []
    review_elements = []
    clean_reviews = []
    
    for i in range(3):#get 3 pages worth of reviews or 30 reviews
        
        page_num = str(i + 1)
        
        driver.get('https://www.amazon.com/product-reviews/'+ asin +'/ref=cm_cr_getr_d_show_all?ie=UTF8&reviewerType=all_reviews&pageNumber='+(page_num)+'&sortBy=recent')#gets each page and sorts by most recent
        review_elements = driver.find_elements_by_xpath("//*[@class = 'a-size-base review-text review-text-content']/span")
        
        reviews += [review.text for review in review_elements]#puts each review in a list
        
        time.sleep(5)#gives the page time to load

    for review in reviews:#iterates through each item in list
        print(review + 'END OF REVIEW\n')


search_input = input('please enter what you would like to search: ')

parse_reviews(search(search_input))

