import requests
from bs4 import BeautifulSoup

url= "https://www.google.com"

response= requests.get(url)

if response.status_code==200:
    html_response=response.text
    print(html_response)
else:
    print("error getting the website")
    exit()

soup= BeautifulSoup(html_response,"html.parser")
print(soup.find("google"))
