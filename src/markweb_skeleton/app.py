#!/usr/bin/python
# Basic skeleton for Markweb app
# @author alfin.akhret@gmail.com
from flask import Flask

app = Flask(__name__)

# load configuration
app.config.from_object('config.DevelopmentConfig')

if __name__ == '__main__':
    app.run()