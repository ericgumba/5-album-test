# -*- coding: utf-8 -*- 
import requests
from bs4 import BeautifulSoup
import sys

    
def formatted_text(t):
    if "[" in t:
        return "" 
    if "&" in t:  
        t=t.replace('&','and')
    chars_to_replace = ['.','\'',',','!','?']
    for c in chars_to_replace:
        t =  t.replace(c,'').lower() 
    return t.replace(' ','-')

class WikipediaScraper:
    def other(url):

        response = requests.get(
            url=url,
        )
        soup = BeautifulSoup(response.content, 'html.parser')
        res = [] 
        title = soup.find(id="firstHeading") 
        results = soup.find(id="mw-content-text")

        col_elements = results.find_all("ul")
        
        brk = False   
        for col_element in col_elements:
            if brk:
                break
            title_elements = col_element.find_all("a")  
            for title_element in title_elements: 
                if title_element.text == 'List of pop punk albums':
                    brk = True
                    break

                ft = formatted_text(title_element.text)

                if ft:
                    res.append(ft)  

        return res 

    def get_artist_list( url):

        if url == "https://en.wikipedia.org/wiki/List_of_pop-punk_bands":
            return WikipediaScraper.other(url)

        response = requests.get(
            url=url,
        )
        soup = BeautifulSoup(response.content, 'html.parser')
        res = [] 
        title = soup.find(id="firstHeading") 
        results = soup.find(id="mw-content-text")

        col_elements = results.find_all("div", class_="div-col")
        
        for col_element in col_elements:
            title_elements = col_element.find_all("a")  
            for title_element in title_elements: 
                if title_element.text == 'List of alternative metal artists':
                    break
                
                ft = formatted_text(title_element.text)

                if ft:
                    res.append(ft)  

        return res 