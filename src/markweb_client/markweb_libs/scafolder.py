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

    def install(self):
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

        self.__write_files()
        self.__create_virtual_environment()

    def __write_files(self):
        '''
        write base files
        '''
        print 'writing base files ...'
        files_to_write = ['run.py', 'config.py', 'requirements.txt', 'app/views/views.py', 'templates/base.html', 'templates/index.html']

        for item in files_to_write:
            
            src_file, _ = os.path.splitext(item)

            # read from source files
            f = open('base_contents/' + os.path.basename(src_file) + '.txt', 'r')
            content = f.read()
            f.close()

            # write to target files
            f = open(self.project_name + item, 'w')
            f.write(content)
            f.close()
        
        print 'Done!'

    def __create_virtual_environment(self):
        '''
        create project virtual environment
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
    scafolder.install()