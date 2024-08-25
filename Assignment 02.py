#Scenario 1

from bs4 import BeautifulSoup
import requests

url = "https://realpython.github.io/fake-jobs/"
request = requests.get(url)
request

info = BeautifulSoup(request.content,"html5lib")
info

title = info.find(class_="title is-1")
title.text.strip()

div = info.find(id="resultcontainer")
div.text
    
