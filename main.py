# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 16:59:38 2016

"""

import github3 # docs here: http://github3py.readthedocs.io/en/latest/examples/github.html
import csv
import os

os.chdir('/Users/bryanshepherd/Projects/GitHubTyper/')

with open('auth/auth.csv', newline='') as f:
    text = csv.reader(f)

    for row in text:
        user_name, password = row

g = github3.login(user_name, password)

for repo in g.get_user().get_repos():
    print(repo.name)

help(Github)

g.get_rate_limit().rate.remaining

help(github)


g_com = g.Commit()

help(github.GitObject)