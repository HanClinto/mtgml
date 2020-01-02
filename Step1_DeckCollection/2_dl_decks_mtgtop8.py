# Download decks from mtgtop8 ala: https://www.mtgtop8.com/mtgo?d=368698

import urllib.request
import os.path

max_deck = 368698 # For now, get this from the first page on: https://www.mtgtop8.com/search
starting_deck = 204998 # Found through experimentation on which decks appeared empty and which appeared to have content.

for i in range(starting_deck, max_deck):
    filename = "./mtgtop8_decks/" + str(i) + ".txt"
    if not os.path.exists(filename):
        print ("Downloading", i, "...")
        url = 'https://www.mtgtop8.com/mtgo?d=' + str(i)
        urllib.request.urlretrieve(url, "./mtgtop8_decks/" + str(i) + ".txt")

