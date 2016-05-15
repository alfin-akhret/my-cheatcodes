#!/usr/bin/env python
# scafolder for my flask project
# @author alfin.akhret@gmail.com
import os
import sys

def create_folders(project_name=''):
    '''
    create a project folders
    if project name is empty then
    create the project in current CWD
    @param pf (project folder, default='')
    '''
    
    project_name = project_name + '/'

    print 'Creating project folders and files'

    project_files = [
        '__init__.py',
        'run.py',
        'config.py',
        'app/__init__.py',
        'app/views/__init__.py',
        'app/views/views.py',
        'static/js/app.js',
        'static/css/style.css',
        'static/images/none.txt'
        ]
    
    for f in project_files:
        f = project_name + f
        if not os.path.exists(os.path.dirname(f)):
            try:
                print 'create... %s' %f
                os.makedirs(os.path.dirname(f))
            except OSError as e:
                print e
                sys.exit(1)
                # if e.errno != errno.EEXIST:
                #     raise
        open(f, 'a+').close()

    print 'Done!'

def write_files(project_name=''):
    '''
    write all base files
    '''

    project_name = project_name + '/'

    # create application config file
    print 'writing configuration ...'
    f = open(project_name + 'config.py', 'w')
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
    f = open(project_name + 'run.py', 'w')
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
    f = open(project_name + 'app/views/views.py', 'w')
    text = """# Basic Views
from flask import Blueprint

default = Blueprint('default', __name__)

@default.route('/')
def home():
    return 'Welcome to Markweb'
    """
    f.write(text)
    f.close()

    print 'Done!'

if __name__ == '__main__':

    if len(sys.argv) > 1:
        project_name = sys.argv[1]
    else:
        project_name = '' 
    create_folders(project_name)
    write_files(project_name)
