#!/usr/bin/python
# Basic skeleton for Markweb app
# @author alfin.akhret@gmail.com
from flask import Flask

# create the app
# set the static folder and instance folder
app = Flask(__name__, static_folder='/static',
    instance_path='/instance',
    instance_relative_config=True)

# load app configuration, default=DevelopmentConfig
app.config.from_object('config.DevelopmentConfig')

if __name__ == '__main__':
    app.run()