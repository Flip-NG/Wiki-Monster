#!/usr/bin/python3

import pandas as pd
import wikipedia as wp
import sys
import itertools
import time
import os


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


def more():

    article = wiki_search()
    print("\n1.summary\n2.Full Article\n3.Exit")

    choice = input("Enter your selection[1-3]:")

    if choice == '1':
        os.system('clear')
        print(article.summary)
        new_search()

    elif choice == '2':
        os.system('clear')
        print(article.content)
        new_search()

    elif choice == '3':
        os.system('clear')
        exit()

    else:
        print("Invalid Option")


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


def spinning_cursor():

    while True:
        for cursor in '|/-\\':
            yield cursor


def spin():

    spinner = spinning_cursor()

    for _ in range(10):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')


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


more()
