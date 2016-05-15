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
    
    print 'Creating project folders'
    
    os.makedirs(project_name + 'app', )

    open(project_name + '__init__.py', 'a+').close()
    open(project_name + 'app/__init__.py', 'a+').close()

    static_folder = ['js', 'css', 'images']
    for f in static_folder:
        os.makedirs(project_name + 'static/' + f)
        if f == 'js':
            open(project_name + 'static/js/app.js', 'a+').close()
        if f == 'css':
            open(project_name + 'static/css/style.css', 'a+').close()

    print 'Done!'

  

def create_files(project_name=''):
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