#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 23:29:50 2019

@author: piyush.krishna
"""
import requests, bs4, pandas as pd, openpyxl
def scraping(**arg):
    req = requests.get(arg['Website'])
    soup = bs4.BeautifulSoup(req.content,'html.parser')
    try:
        soup_artist = soup.select(arg['css_select_artist'])
        soup_day = soup.select(arg['css_select_day'])
    except:
        soup_day = []
    artist_l = []
    day_l = []
    festival_l = []
    for l in range(len(soup_artist) - 1):
        
        if not arg['artist_attr'] == 'n/a':
            artist = soup_artist[l].get(arg['artist_attr'])
        else:
            artist = soup_artist[l].text
        artist_l.append(artist)
        
        
        if len(soup_day) != 0:
            if not arg['day_attr'] == 'n/a':
                    day = soup_day[l].get(arg['day_attr'])
            else:
                    day = soup_day[l].text
        else:
            day = 'N/A'    
        day_l.append(day)
        festival_l.append(arg['festival_name'])
        
    df= pd.DataFrame({'Festival Name':festival_l, 'Artists':artist_l, 'Performance Days':day_l })
    return (df)

