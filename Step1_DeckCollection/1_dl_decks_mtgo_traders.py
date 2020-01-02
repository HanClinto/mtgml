# Download decks from mtgotraders ala: https://www.mtgotraders.com/deck/data/download.php?d=503&t=t&g=m

import urllib.request

max_deck = 4191 # For now, get this from the top entry on "Top 10 recent" from this page: https://www.mtgotraders.com/deck/#/

for i in range(185, max_deck):
    print ("Downloading", i, "...")
    url = 'https://www.mtgotraders.com/deck/data/download.php?t=t&g=m&d=' + str(i)
    urllib.request.urlretrieve(url, "./mtgotraders_decks/" + str(i) + ".txt")

