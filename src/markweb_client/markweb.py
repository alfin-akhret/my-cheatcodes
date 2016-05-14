#!/usr/bin/env python
# CLI client for markweb app
# @author: alfin akhret
# features:
# 1. fetch the markweb skeleton

"""Naval Fate.

Usage:
  markweb install
  markweb --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Markweb 0.0.1')
    print arguments