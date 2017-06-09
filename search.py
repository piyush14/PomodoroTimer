import bs4
import requests

_author_ = "Rk"
_pyversion_ = "2.7 or lower"


def search(query):
    url = 'http://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias' \
          '%3Daps&field-keywords={}'.format(query.replace(' ', '+'))

    return scrape(url)
    print (url)


def scrape(url):
    response = requests.get(url,
                            headers={'User-agent': 'Mozilla/5.0 (Windows NT '
                                                   '6.2; WOW64) AppleWebKit/'
                                                   '537.36 (KHTML, like '
                                                   'Gecko) Chrome/37.0.2062.'
                                                   '120 Safari/537.36'})
    soup = bs4.BeautifulSoup(response.content, "html.parser")
    # print response.content
    prod_list = []
    prods = {}
    asins_dict = {}
    asins_sponsored_dict = {}
    for tag in soup.find_all('li', {'class': 's-result-item'}):
        asins_dict[tag.get('data-asin')] = tag.get('id')
        prods['Product'] = tag.find('h2').text.encode('ascii', 'ignore')
        by_list = tag.find_all('span',
                               {'class': 'a-size-small '
                                         'a-color-secondary'})

        # print by_list
        if len(by_list) > 0:
            if 'by ' in by_list[0].string:
                prods['by'] = by_list[1].string.encode('utf-8')
            else:
                prods['by'] = ' '

        try:
            price_list = tag.find('span',
                                  {'class': 'a-size-base '
                                            'a-color-price '
                                            's-price a-text-bold'}).text
        except AttributeError:
            price_list = 'Price Not Found'
        # print price_list
        if len(price_list) > 0:
            prods['price'] = price_list.encode('ascii', 'ignore')

        try:
            stars_list = tag.find('span',
                                  {'class': 'a-icon-alt'}).text
        except AttributeError:
            stars_list = 'No ratings Found'
        # print stars_list
        if len(stars_list) > 0:
            if stars_list[0] == 'Prime':
                if len(stars_list) > 1:
                    prods['star'] = stars_list
            else:
                prods['star'] = stars_list.encode('ascii', 'ignore')
        prod_url_list = 'http://www.amazon.in/gp/product/' + tag.get('data-asin')
        prods['url'] = prod_url_list.encode('ascii', 'ignore')
        img_url_list = tag.find_all('img',
                                    {'class': 's-access-image '
                                              'cfMarker'})
        if len(img_url_list) > 0:
            prods['imgurl'] = img_url_list[0]['src'].encode('utf-8')

        prod_list.append(prods.copy())
        # start here
        # you can print less info my directly calling the tag:ex  print prods['star'], prods['price']
    ##    print prod_list
    for i, entry in enumerate(prod_list):
        print 'result:' + str(i)
        print entry;

        # print type(prods)


if __name__ == "__main__":
    search_string = input("what would you like to search for?  eg: 'men watch' ")
    product_list = search(search_string)