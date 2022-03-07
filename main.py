#!/usr/bin/python
# -*- coding: Utf-8 -*-

import json
import platform
from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)
app.secret_key = "ahcestcontulaspas"
app.debug = True


@app.route('/')
def home():
    return render_template("index.html")



if __name__ == '__main__':
    if platform.system() != "Windows":


        website_url = 'thomas.lemartinel.com:80'
        app.config['SERVER_NAME'] = website_url

    app.config['SESSION_COOKIE_SECURE'] = False
    app.config['SESSION_COOKIE_NAME'] = "BonsCookies"
    app.run()
