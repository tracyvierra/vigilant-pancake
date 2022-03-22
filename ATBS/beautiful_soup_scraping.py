# Author: Tracy Vierra
# Date Created: 3/22/2022
# Date Modified: 3/22/2022

# Description:

# Usage:

import bs4
import requests

res = requests.get('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/')
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# soup.select('<span id="newBuyBoxPrice" class="a-size-base a-color-price header-price a-text-normal">$34.94</span>')

elems = soup.select('#newBuyBoxPrice.a-size-base.a-color-price.header-price.a-text-normal')
print(elems)

def getAmazonPrice(url):
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#newBuyBoxPrice')
    return elems[0].text.strip()


print(getAmazonPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/'))



