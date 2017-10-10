import requests
from bs4 import BeautifulSoup

#url='https://www.anekdot.ru/release/story/month/'
#url = 'http://bash.im'
url = 'http://forumua.org/forum/%D0%BE%D0%B1%D1%89%D0%B5%D1%81%D1%82%D0%B2%D0%BE-%D0%BA%D1%83%D0%BB%D1%8C%D1%82%D1%83%D1%80%D0%B0-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F/%D1%87%D0%B5%D1%80%D0%BA%D0%B0%D1%81%D1%81%D1%8B-%D0%B8-%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C/68304-%D1%81%D1%83%D0%B1%D1%81%D0%B8%D0%B4%D0%B8%D1%8F'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html,'html.parser')
for tag in soup.find_all('div', 'js-post__content-text OLD__post-content-text restore h-wordwrap'):
	print(tag.get_text().replace("\n", " ").strip())


#<div class="js-post__content-text OLD__post-content-text restore h-wordwrap" itemprop="text">
							