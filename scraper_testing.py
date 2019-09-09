from bs4 import BeautifulSoup
from nltk.corpus import stopwords 
import urllib.request
import nltk
from lxml import html
from json import dumps, loads
import json
from re import sub
from dateutil import parser as dateparser
import time
from requests import get
from nltk.tokenize import sent_tokenize
from selenium import webdriver

driver = webdriver.Firefox()

def parse_reviews():
    
    reviews = []
    review_elements = []
    
    for i in range(3):#get 3 pages worth of reviews or 30 reviews
        
        page_num = str(i + 1)
        
        driver.get('https://www.amazon.com/product-reviews/B07TZKFJBX/ref=cm_cr_getr_d_show_all?ie=UTF8&reviewerType=all_reviews&pageNumber='+(page_num)+'&sortBy=recent')#gets each page
        review_elements = driver.find_elements_by_xpath("//*[@class = 'a-size-base review-text review-text-content']/span")
        
        reviews += [review.text for review in review_elements]
        
        time.sleep(5)

    for review in reviews:
        
        print(review + 'END OF REVIEW')
        
parse_reviews()
