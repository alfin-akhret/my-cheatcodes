#!/usr/bin/env python
# CLI client for markweb app
# @author: alfin akhret
# features:
# 1. fetch the markweb skeleton

"""Naval Fate.

Usage:
  markweb install [--target=PROJECT_FOLDER]
  markweb --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""
from docopt import docopt
from markweb_libs.scafolder import create_folders, write_files, create_virtual_environment

def install(target):
    if target is None:
        target = '.'
    create_folders(target)
    write_files(target)
    create_virtual_environment(target)

if __name__ == '__main__':
    args = docopt(__doc__, version='Markweb 0.0.1')
    # print args
    if args['install']:
        install(args['--target'])
