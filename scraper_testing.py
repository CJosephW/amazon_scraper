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
from nltk.corpus import wordnet
import string
from textblob import TextBlob
import re
driver = webdriver.Firefox()
stop_words = set(stopwords.words('english'))
tokenizer = RegexpTokenizer(r'\w+')
good_synonyms = []
is_noun = lambda pos: pos[:2] == 'NN'
for syn in wordnet.synsets('quality'):
    for l in syn.lemmas():
        good_synonyms.append(l.name())
good_synonyms.append('good')
bad_syns = wordnet.synsets('bad')
bad_syns.append('bad')
nouns = {x.name().split('.', 1)[0] for x in wordnet.all_synsets('n')}
def search(search_keyword):
    
    driver.get('https://www.amazon.com/s?k='+ search_keyword + '&ref=nb_sb_noss_1')
    
    time.sleep(5)
    
    search_index = 1
    
    results = driver.find_elements_by_css_selector("span.a-size-base-plus.a-color-base.a-text-normal")
    other_results = driver.find_elements_by_css_selector("span.a-size-medium.a-color-base.a-text-normal")

    for result in other_results:
        
        results.append(result)
    
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
    clean_reviews2 = []
    clean_reviews = []
    
    for i in range(3):#get 3 pages worth of reviews or 30 reviews
        
        page_num = str(i + 1)
        
        driver.get('https://www.amazon.com/product-reviews/'+ asin +'/ref=cm_cr_getr_d_show_all?ie=UTF8&reviewerType=all_reviews&pageNumber='+(page_num)+'&sortBy=recent')#gets each page and sorts by most recent
        review_elements = driver.find_elements_by_xpath("//*[@class = 'a-size-base review-text review-text-content']/span")
        
        reviews += [review.text for review in review_elements]#puts each review in a list
        
        time.sleep(5)#gives the page time to load

    for review in reviews:#iterates through each item in list
        print(review + 'END OF REVIEW\n')
        #clean_tokens += [word.strip(string.punctuation) for word in review.split(" ")]
        
    clean_reviews2 += [review.translate(str.maketrans("","", string.punctuation)) for review in reviews]
    
    clean_reviews = ''.join(reviews)
    clean_reviews = clean_reviews.split('.')

    for i in range(len(clean_reviews)):
        text = TextBlob(clean_reviews[i])
        current_word = clean_reviews[i].split(' ')#see if words to the left and right are noun then grab if they are and put them before 
        if any(syn in clean_reviews[i] for syn in good_synonyms):
            print (clean_reviews[i] + 'good review')
                #todo use text blob to find noun and noun pharses
                #remove words like the and such
                

    
search_input = input('please enter what you would like to search: ')

parse_reviews(search(search_input))

