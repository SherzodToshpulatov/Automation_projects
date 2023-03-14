import bs4, requests
def getprice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('body > section.Catalog-information.container > div.Catalog-information-right-start > div.Catalog-information-right > div.Catalog-information-right-block-right > div.Catalog-information-right-block-right-main > h1 > span')
    return elems[0].text.strip()

price = getprice('https://www.mediapark.uz/products/view/16498')
print('The Price Is ' + price)


