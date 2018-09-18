import requests
from bs4 import BeautifulSoup, Comment
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']

characters += [c.upper() for c in characters]


if __name__ == '__main__':
    r = requests.get('http://www.pythonchallenge.com/pc/def/ocr.html')
    soup = BeautifulSoup(r.text, "html.parser")
    res = ''

    comments = soup.findAll(text=lambda text: isinstance(text, Comment))

    for c in comments[1]:
        if c in characters:
            res += c

    print(res)