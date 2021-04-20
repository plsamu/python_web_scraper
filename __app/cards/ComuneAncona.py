import sys
sys.path.append("..")
import Card

def getCards(url, soup):
    cards = []
    titoli = soup.find_all(['article', 'h2'], class_='post-title')
    date = soup.find_all(['article', 'div', 'span'], class_='meta-date')
    
    for x in range(len(titoli)-1):
        cards.append(Card.Card(url, date[x].get_text(), titoli[x].get_text(), None))
    
    return cards