# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 21:34:23 2019

@author: pikrishna
"""

from flask import Flask, render_template, request,make_response, redirect
from flask_bootstrap import Bootstrap
app = Flask(__name__)

a = '1'
class sum1:
    def sum123(self):
        return 12345

@app.route('/')
def home():
    return render_template('home.html',data = a)


@app.route('/ab')
def ab():
    a = make_response('<h1>ahahahaha.</h1>')
    #return render_template('ab.html',data = dir(request))
    x= sum1()
    return render_template('home.html',d = x)
#import flask_new



if __name__ == '__main__':

   app.run(debug = 1)
   bootstrap = Bootstrap(app)
  
