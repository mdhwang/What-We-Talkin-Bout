import copy
import pandas as pd
import time

# Requests sends and recieves HTTP requests.
import requests

# Beautiful Soup parses HTML documents in python.
from bs4 import BeautifulSoup



#WEBPAGE TO LETTER LINKS
def get_letter_links(website_url):
    soup = BeautifulSoup(requests.get(website_url).content, 'html.parser') #get that shit
    links = []
    home_url = "https:"
    for each in soup.find_all('a'):
        links.append(home_url + each.get("href")) #store that shit
    return links[1:28] #gets only nav links, return that shit


#LETTER LINKS TO ARTIST LINKS
def get_artist_links(letter_url):
    soup = BeautifulSoup(requests.get(letter_url).content, 'html.parser') #get that shit
    links = []
    home_url = "https://www.azlyrics.com/"
    for each in soup.find_all('a'):
        links.append(home_url + each.get("href")) #store that shit
    return links[28:-8] #takes out nav links and footer links, return that shit


#ARTIST LINKS TO TRACK LINKS
def get_track_links(artist_home_url):
    name = artist_home_url.split('/')[4].split('.html')[0]
    soup = BeautifulSoup(requests.get(artist_home_url).content, 'html.parser') #get that shit
    links = []
    home_url = "https://www.azlyrics.com"
    for each in soup.find_all('a'):
        links.append(each.get("href").replace("..",home_url)) #store that shit
    return {name:links[30:-8]} #takes out nav links and footer links, return that shit as a dict for JSON reasons

#TRACK LINKS TO LYRICS
def get_lyrics(track_url):
    artist = track_url.split('/')[4].split('.html')[0]
    track = track_url.split('/')[5].split('.html')[0]
    soup = BeautifulSoup(requests.get(track_url).content, 'html.parser').prettify() #get that shit
    lyrics = soup.split("<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->")[1].split("<!-- MxM banner -->")[0]
    #return {"artist":artist,"track":track,"lyrics":lyrics}
    return lyrics