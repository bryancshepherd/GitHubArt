# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 16:59:38 2016

"""

import sys

# Dot matrix font for reference:
# https://www.colourbox.com/image/3d-dot-matrix-font-49-characters-with-real-reflection-symbol-size-500x500pt-image-2340783

# This is helpful here:
# http://stackoverflow.com/questions/36380033/invalidschema-when-attempting-to-create-file-with-github3-py

import os
os.chdir('/Users/bryanshepherd/Projects/GitHubTyper/')

# GitHub3.py docs are here:
# http://github3py.readthedocs.io/en/latest/examples/github.html
from github3 import login 
import csv
import os
import letters
import numpy as np
import time
import datetime

# The letter arrays are manually added to letters.py.
# It's easier to create them if they are laid out as 
# 7 x N 'matrices' (that are actually arrays), 
# but they then need to be converted to real
# matrices and reshaped to fill in the correct days. 
# This function does the conversion to a matrix and reshaping. 
# This process could be done a number of ways - this is how
# I did it.
def reorg_letters(org_letter_array):
    rows = 7
    cols = len(org_letter_array)/rows
    
    temp_array = np.array(org_letter_array)
    temp_array.shape = (int(rows), int(cols))
    return (temp_array)

# Login helper
# Comma separated redentials are stored 
# in the first row of auth.csv. 
def github_login():
    with open('auth/auth.csv', newline='') as f:
        text = csv.reader(f)
    
        for row in text:
            user_name, password = row
    
    session = login(user_name, password)
    
    return(session)

# The function that submits the commits
# The number of commits should be set to 
# something quite a bit higher than your
# normal number of daily commits. This 
# may also require changing the sleep_time
# so that things still complete in a reasonable
# amount of time
def do_typing(num_of_commits=20, sleep_time=300):
    
    me = github_login()

    repo = me.repository('bryancshepherd', 'GitHubTyper')

    # Create a file
    data = 'typing file'
    repo.create_file(path = 'files/dotfile.txt',
                     message = 'Add dot file',
                     content = data.encode('utf-8'))
    
    # Get the file reference for later use
    file_sha = repo.contents(path = 'files/dotfile.txt').sha
    
    # Delete the file
    repo.delete_file(path = 'files/file1.txt',
                     message = 'Delete dot file',
                     sha = file_sha)
                     
    time.sleep(sleep_time)

# Matrixify the characters in the
# passed phrase
def matrixify_phrase(phrase_to_convert):
    for i in range(len(phrase_to_convert)):
        char = phrase_to_convert[i]
        char = char.upper()
        char_array = letters.letters_dict[char]
        temp_char_mat = reorg_letters(char_array)
        
        if i == 0:
            char_mat = temp_char_mat
        else:
            char_mat = np.hstack((char_mat, temp_char_mat))
        
    return(char_mat)
    

def typing_controller(args = sys.argv): 
    
# Get the command line arguments
    phrase = args[1]
    start_date = args[2]
    
    # Work with start and current date to
    # figure out the pointer/typer position
    split_start_date = [int(num) for num in start_date.split('-')]
    start_date_dt = datetime.date(split_start_date[0], 
                                  split_start_date[1], 
                                  split_start_date[2])
                                  
    # Check that the start date is a Sunday, since
    # that's our [0,0] day on GitHub
    if start_date_dt.isoweekday() != 7:
        print('The start date should be a Sunday.')
        return()
        
    curr_date = datetime.date.today()
    
    date_diff = curr_date - start_date_dt
    date_diff_int = date_diff.days
    
    # Use floor division to get the row
    # and modulus to get the column
    row = date_diff_int % 7
    col = date_diff_int//7

    mat_phrase = matrixify_phrase(phrase_to_convert=phrase) 
    
    dims = mat_phrase.shape
    
    if (date_diff_int >= (dims[0]*dims[1])):
        return()
    
    if mat_phrase[row, col] == 1:
        # do_typing()
        
        print('1') # Just for testing
    else: # Just for testing
        print('0') # Just for testing
        
typing_controller()

    

