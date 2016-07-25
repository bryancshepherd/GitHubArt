# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 16:59:38 2016

"""

# Dot matrix font for reference:
# https://www.colourbox.com/image/3d-dot-matrix-font-49-characters-with-real-reflection-symbol-size-500x500pt-image-2340783

from github3 import login # docs here: http://github3py.readthedocs.io/en/latest/examples/github.html
import csv
import os

os.chdir('/Users/bryanshepherd/Projects/GitHubTyper/')

with open('auth/auth.csv', newline='') as f:
    text = csv.reader(f)

    for row in text:
        user_name, password = row

me = login(user_name, password)

# This is helpful here:
# http://stackoverflow.com/questions/36380033/invalidschema-when-attempting-to-create-file-with-github3-py

repo = me.repository('bryancshepherd', 'GitHubTyper')

# Create a file
data = 'testing file 1'
repo.create_file(path = 'files/dotfile.txt',
                 message = 'Add dot file',
                 content = data.encode('utf-8'))

# Get the file reference for later use
file_sha = repo.contents(path = 'files/dotfile.txt').sha

# Delete the file
repo.delete_file(path = 'files/file1.txt',
                 message = 'Delete dot file',
                 sha = file_sha)

