import requests
from bs4 import BeautifulSoup, Comment
import re
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
big_characters = [c.upper() for c in characters]

characters += big_characters
reg = r'[a-z][A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z][a-z]'
url = 'http://www.pythonchallenge.com/pc/def/equality.html'

if __name__ == '__main__':
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    res = ''

    comments = soup.findAll(text=lambda text: isinstance(text, Comment))

    print(comments[0])

    first_word = ''.join(re.findall(reg, comments[0]))
    print(first_word)