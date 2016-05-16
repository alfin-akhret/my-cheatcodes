#!/usr/bin/env python
# scafolder for my flask project
# @author alfin.akhret@gmail.com
import os
import sys

class Scafolder():
    '''
    Scafold basic flash directory structures
    and files
    '''
    def __init__(self, project_name):
        self.project_name = project_name + '/'
        self.project_files = [
            '__init__.py',
            'run.py',
            'config.py',
            'requirements.txt',
            'templates/base.html',
            'templates/index.html',
            'app/__init__.py',
            'app/views/__init__.py',
            'app/views/views.py',
            'static/js/app.js',
            'static/css/style.css',
            'static/images/none.txt'
            ]

    def create_folders(self):
        '''
        create a project folders
        if project name is empty then
        create the project in current CWD
        @param pf (project folder, default='')
        ''' 

        print 'Creating project folders and files'
        
        for f in self.project_files:
            f = self.project_name + f
            if not os.path.exists(os.path.dirname(f)):
                try:
                    print 'create... %s' %f
                    os.makedirs(os.path.dirname(f))
                except OSError as e:
                    print e
                    sys.exit(1)
            open(f, 'a+').close()

        print 'Done!'

    def write_files(self):
        '''
        write to all base files
        '''
        # create application config file
        print 'writing configuration ...'
        f = open(self.project_name + 'config.py', 'w')
        text = """# application configuration
class BaseConfig(object):
    'Base config class'
    SECRET_KEY = 'A random secret key'
    DEBUG = True
    TESTING = False
    NEW_CONFIG_VARIABLE = 'my value'

class ProductionConfig(BaseConfig):
    'production spesific config'
    DEBUG = False
    #SECRET_KEY = open('/path/to/secret/key/file').read()

class StagingConfig(BaseConfig):
    'Staging specific config'
    DEBUG = True

class DevelopmentConfig(BaseConfig):
    'Development environment spesific config'
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'Another random secret key'
    """
        f.write(text)
        f.close()
        
        # create main application server file
        print 'writing application server ...'
        f = open(self.project_name + 'run.py', 'w')
        text = """from flask import Flask
from app.views.views import default

# create the app
# set the static folder and instance folder
app = Flask(__name__, static_folder='/static',
    instance_path='/instance',
    instance_relative_config=True)

# register the blueprint
app.register_blueprint(default)

# load app configuration, default=DevelopmentConfig
app.config.from_object('config.DevelopmentConfig')

if __name__ == '__main__':
    app.run()
        """
        f.write(text)
        f.close()

        # create default views
        print 'writing base view ...'
        f = open(self.project_name + 'app/views/views.py', 'w')
        text = """# Basic Views
from flask import Blueprint
from flask import render_template, request

default = Blueprint('default', __name__)

@default.route('/')
def home():
    return render_template('index.html')
    """
        f.write(text)
        f.close()

        f = open(self.project_name + 'templates/base.html', 'w')
        text = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>App name</title>
</head>
<body>

    <div class="container">
        {% block container %}{% endblock %}
    </div>
    
</body>
</html>"""
        f.write(text)
        f.close()

        f = open(self.project_name + 'templates/index.html', 'w')
        text = """{% extends 'base.html' %}

{% block container %}
    <p>Flask server is running</p>
{% endblock %}

</body>
</html>"""
        f.write(text)
        f.close()

        # create requirements.txt
        f = open(self.project_name + 'requirements.txt', 'w')
        text = 'Flask==0.10.1'
        f.write(text)
        f.close()

        print 'Done!'

    def create_virtual_environment(self):
        '''
        - create project virtual environment
        - activate it
        - intall flask
        '''
        os.chdir(self.project_name)
        
        print 'Setting up virtual environment ...'
        os.system('virtualenv venv')
        
        print 'Done!'


if __name__ == '__main__':

    if len(sys.argv) > 1:
        project_name = sys.argv[1]
    else:
        project_name = '.'
    scafolder = Scafolder(project_name)
    scafolder.create_folders()
    scafolder.write_files()
    scafolder.create_virtual_environment()