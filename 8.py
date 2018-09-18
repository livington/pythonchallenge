import requests
from bs4 import BeautifulSoup, Comment
import bz2

url = 'http://www.pythonchallenge.com/pc/def/integrity.html'


if __name__ == '__main__':
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")
    comments = soup.findAll(text=lambda text: isinstance(text, Comment))
    comments = comments[0].split('\n')
    fc = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    sc = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
    print(fc, sc)
    print(''.join([str(bz2.decompress(fc))[2:-1], str(bz2.decompress(sc))[2:-1]]))