from bs4 import BeautifulSoup
from nltk.corpus import stopwords 
import urllib.request
import nltk
from lxml import html
from json import dumps, loads
import json
from re import sub
from dateutil import parser as dateparser
from time import sleep
from requests import get
from nltk.tokenize import sent_tokenize
from selenium import webdriver




def ParseReviews(asin):
    driver.get

def FindAsin():
    asins = []
    review_data = []

    for asin in asins:
        print('extracting data from amazon.com/dp/' + asin)
