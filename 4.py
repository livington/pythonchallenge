import requests
from bs4 import BeautifulSoup, Comment
import re
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
big_characters = [c.upper() for c in characters]

characters += big_characters
reg = r'[a-z][A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z][a-z]'
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

if __name__ == '__main__':
    num = '12345'
    res = []
    new_res = []
    fl_to_divide = 0

    for i in range(400):
        r = requests.get(url + num)
        print('iteration={0}, res={1}'.format(i+1, r.text))
        s = r.text.split()

        if fl_to_divide == 1:
            num = str(int(r.text.split()[-1]) // 2)
        else:
            num = s[-1]

        if s[1] == 'Yes.':
            fl_to_divide = 1
            num = str(int(r.text.split()[-1]) // 2)

        if r.text.find('and the next nothing') != 0:
            new_res.append((i, r.text))

    print(new_res)
