#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 11:11:18 2019
"""

from flask import Flask, render_template
import Scraper as sc, pandas as pd, openpyxl

app = Flask(__name__)

@app.route('/')
def home():
    df = pd.DataFrame()
    scraping_wb = openpyxl.load_workbook('scraping_data.xlsx')
    for row in scraping_wb['Sheet1'].iter_rows(min_row = 2):
        df_c = sc.scraping (festival_name = row[0].value,
                       Website = row[1].value, 
                       css_select_artist = row[2].value,
                       artist_attr = row[3].value,
                       css_select_day = row[4].value,
                       day_attr = row[5].value)
        df = df.append(df_c)
    return render_template('ab.html', data = df.to_html(header="true", table_id="table"))   

if __name__ == '__main__':
    app.run(debug = 1)