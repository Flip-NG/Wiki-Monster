#!/usr/bin/python3
# WIKIT written by flip-NG
# Copyright (C) 2018

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# importing libraries

import pandas as pd
import wikipedia as wp
import sys
import itertools
import time
import os


# queries wikipedia for search string and prints summary table

def wiki_search():

    os.system('clear')
    banner()

    search = input("Search:")
    print("searching", end='')
    spin()

    html = wp.page(search).html()
    df = pd.read_html(html)[0]
    table = df.drop(df.index[[0, 1]])
    article = wp.page(search)

    spin()
    os.system('clear')
    print(article.title)
    print(table.to_string(index=False, header=False))
    return article


# creats options menu and executes chosen option

def more():

    article = wiki_search()
    print("\n1.summary\n2.Full Article\n3.Exit")

    choice = input("Enter your selection[1-3]:")

# prints summary if chosen

    if choice == '1':
        os.system('clear')
        print(article.summary)
        new_search()

# prints complete wikipedia page

    elif choice == '2':
        os.system('clear')
        print(article.content)
        new_search()

# exits script

    elif choice == '3':
        os.system('clear')
        exit()

    else:
        print("Invalid Option")
        more()


# draws banner to terminal

def banner():

    print(
       '''
##########################
#___________()________() #
#\ \ /\ / / || | |/ / || #
# \ V  V /  || |   <  || #
#__\_/\_/___||_|_|\_\_||_#
#************************#
##########################''')


# creats spinner cursor that is executed during search

def spinning_cursor():

    while True:
        for cursor in '|/-\\':
            yield cursor


# executes cursor spin

def spin():

    spinner = spinning_cursor()

    for _ in range(10):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')


# menu that asks to execute new search or exits script

def new_search():

    print("1.New Search\n2.Exit")
    x = input("Enter[1-2]")

    if x == '1':
        wiki_search()

    elif x == '2':
        os.system('clear')
        exit()

    else:
        print("Invalid Command")
        time.sleep(5)
        new_search()

# starts script

more()
