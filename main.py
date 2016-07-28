# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 16:59:38 2016

"""

# Dot matrix font for reference:
# https://www.colourbox.com/image/3d-dot-matrix-font-49-characters-with-real-reflection-symbol-size-500x500pt-image-2340783

# This is helpful here:
# http://stackoverflow.com/questions/36380033/invalidschema-when-attempting-to-create-file-with-github3-py

import os
os.chdir('/Users/bryanshepherd/Projects/GitHubTyper/')

from github3 import login # docs here: http://github3py.readthedocs.io/en/latest/examples/github.html
import csv
import os
import letters
import numpy as np
import time
# import importlib
# importlib.reload(letters)

def reorg_letters(org_letter_array):
    rows = 7
    cols = len(org_letter_array)/rows
    
    temp_array = np.array(org_letter_array)
    temp_array.shape = (int(rows), int(cols))
    return (temp_array)

def github_login:
    with open('auth/auth.csv', newline='') as f:
        text = csv.reader(f)
    
        for row in text:
            user_name, password = row
    
    session = login(user_name, password)
    
    return(session)

def do_typing(num_of_commits=20):
    
    me = github_login()

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
                     
    time.sleep(300)

phrase = 'Hi mom!'    
for char in list(phrase):
    char = char.upper()
    char_array = letters.letters_dict[char]
    char_mat = reorg_letters(char_array)
    
    dims = char_mat.shape
    
    for col in range(0,dims[1]):
        for row in range(0,dims[0]):
            print(char_mat[row,col])
            if char_mat[row, col] == 1:
                do_typing()
    
# TODO: Figure out how to test
# TODO: Figure out whether it is better to prebuild the matrices or 
# do it letter by letter.
    

