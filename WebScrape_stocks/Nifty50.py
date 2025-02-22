import pandas as pd
#to work on data 

import sys
import os

import requests
#to connect to the web

from bs4 import BeautifulSoup
#to scrape data from websites

import re
#regualar expressions to work with text(finding, searching and manipulating)

#stock_code eg: SBI -> SBIN
def fetch_NSE_stock_price(stock_code):
    
    stock_url  = 'https://www.nseindia.com/get-quotes/equity?symbol='+str(stock_code)
    print(stock_url)
    response = requests.get(stock_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data_array = soup.find(id='responseDiv').getText().strip().split(":")

fetch_NSE_stock_price("SBIN")