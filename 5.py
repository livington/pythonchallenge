import requests
import pickle
from bs4 import BeautifulSoup, Comment
import re
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
big_characters = [c.upper() for c in characters]

characters += big_characters
reg = r'[a-z][A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z][a-z]'
url = 'http://www.pythonchallenge.com/pc/def/banner.p'

if __name__ == '__main__':
    r = requests.get(url)
    print(r.content)
    uniq_res = []

    with open('banner.p', 'wb') as f:
        f.write(r.content)

    with open('banner.p', 'rb') as f:
        res = pickle.load(f)

    for r in res:
        print(''.join([elem[1]*elem[0] for elem in r]))