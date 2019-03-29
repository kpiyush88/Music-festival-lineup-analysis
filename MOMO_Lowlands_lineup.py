# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 07:11:37 2019

@author: pikrishna
"""
import requests, bs4, pandas as pd, json

def scrape_momo():
    req = requests.get('https://motelmozaique.nl/en/festival/lineup/')
    soup_momo = bs4.BeautifulSoup(req.content,'html.parser')
    tag_momo_artists = soup_momo.select('#programma a div .programma-inner .content')
    tag_momo_category = soup_momo.select('#programma a div .programma-inner .meta-category')
    tag_momo_artist_links = soup_momo.select('#programma a')
    momo_artists = []
    momo_category = []
    momo_artist_links = []
    momo_days = []
    for l in range(len(tag_momo_artists)-1):
        momo_artists.append(tag_momo_artists[l].text)
        momo_category.append(tag_momo_category[l].text)
        momo_artist_links.append(tag_momo_artist_links[l].get('href'))
        req = requests.get(tag_momo_artist_links[l].get('href'))
        soup_momo = bs4.BeautifulSoup(req.content,'html.parser')
        tag_momo_days = soup_momo.select_one('h2')
        momo_days.append(tag_momo_days.text)
    momo_df = pd.DataFrame({'Artists':momo_artists,'category':momo_category,'performance days':momo_days, 
                                'MOMO link': momo_artist_links})
    return (momo_df)

def scrape_lowlands():
    req = requests.get('https://lowlands.nl/programma/')
    soup_low = bs4.BeautifulSoup(req.content,'html.parser')
    tag_low_artists = soup_low.select('#main section .program__inner div.block-hover')
    tag_low_category = soup_low.select('#main section .program__inner div.block-hover a') 
    low_artists = []
    low_category = []
    for l in range(len(tag_low_artists) - 1):
        low_artists.append(tag_low_artists[l].get('data-sort-title'))
        low_category.append(tag_low_category[l].get('data-act-category'))
    low_df = pd.DataFrame({'Artists': low_artists,'Category':low_category})
    return(low_df)

def scrape_pukkelpop():
    req =  requests.get ('https://www.pukkelpop.be/en/line-up/abc/')
    soup_puk = bs4.BeautifulSoup(req.content,'html.parser')
    tag_puk_artists = soup_puk.select('main .lineup-bands .band-lineup__info .band-lineup__name')
    tag_puk_day = soup_puk.select('main .lineup-bands .band-lineup__info .band-lineup__act')
    puk_artists =  list()
    puk_day =  list()
    l = 0
    for t in tag_puk_artists:
        puk_artists.append(t.text)
        puk_day.append(tag_puk_day[l].text) 
        l += 1
    puk_df = pd.DataFrame({'Artists':puk_artists,'performance days':puk_day})
    return (puk_df)

def scrape_pinkpop():
    req = requests.get('https://www.pinkpop.nl/2019/en/programme/')
    soup_pink = bs4.BeautifulSoup(req.content,'html.parser')
    tag_pink_artists = soup_pink.select('.post-type-archive-programma #line-up a .bg-dark-grey h3')
    tag_pink_day = soup_pink.select('.post-type-archive-programma #line-up a .bg-dark-grey h5')
    pink_artists =  list()
    pink_day =  list()
    l = 0
    for t in tag_pink_artists:
        pink_artists.append(t.text)
        pink_day.append(tag_pink_day[l].text) 
        l += 1
    pink_df = pd.DataFrame({'Artists':pink_artists,'performance days':pink_day})
    return (pink_df)
    
df = scrape_lowlands()                
               
                    
'''
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html',data = df)

if __name__ == '__main__':
    app.run(debug = 1)
'''






