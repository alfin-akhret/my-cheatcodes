#!/usr/bin/env python
# scafolder for my flask project
# @author alfin.akhret@gmail.com

def create_folders(project_name=''):
    '''
    create a project folders
    if project name is empty then
    create the project in current CWD
    '''
    import os
    
    print 'Creating project folders and files'

    project_files = [
        project_name + '__init__.py',
        project_name + 'run.py',
        project_name + 'config.py',
        project_name + 'app/__init__.py',
        project_name + 'static/js/app.js',
        project_name + 'static/css/style.css',
        project_name + 'static/images/none.txt'
        ]
    
    for f in project_files:
        if not os.path.exists(os.path.dirname(f)):
            try:
                os.makedirs(os.path.dirname(f))
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
        open(f, 'a+').close() 

    print 'Done!'

def write_files(project_name=''):
    '''
    create all base files
    '''
    pass


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        project_name = sys.argv[1] + '/'
    else:
        project_name = '' 
    create_folders(project_name)