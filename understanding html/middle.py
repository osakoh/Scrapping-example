import re  # import should come first

from bs4 import BeautifulSoup

ITEM_HTML = ''' <html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">

    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html">
                    <img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" 
                    alt="A Light in the Attic" class="thumbnail">
                    </a>  
            </div>
            <p class="star-rating Three">
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
            </p>
            <h3>
                <a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...
                </a>
            </h3>
            
            <div class="product_price">            
                 <p class="price_color">£51.77</p>
                 <p class="instock availability">
                    <i class="icon-ok"></i>  
                        In stock 
                 </p>
                 <form>
                    <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
                 </form>
            </div>
    </article>
</li>

</body></html>
'''

# first get the BeautifulSoap object
soup = BeautifulSoup(ITEM_HTML, 'html.parser')


# print(soup)


def find_item_name():
    """
    :return: the name of the title from the a tag
    """
    locator = 'article.product_pod h3 a'
    item_link = soup.select_one(locator)
    item_title = item_link.attrs['title']
    print(item_title)


def find_item_link():
    """
    :return: the href
    """
    locator = 'article.product_pod h3 a'
    item_href = soup.select_one(locator).attrs['href']
    print(item_href)


"""
def find_price_his():
    locator = 'article.product_pod div.product_price p.price_color'
    item_price = soup.select_one(locator).string  # outputs -> £51.77

    pattern = '£([0-9]+\.[0-9]+)' # to match £51.77
    matcher = re.search(pattern, item_price)
    # print(matcher.group(0))  # outputs the entire pattern
    print(matcher.group(1))  # outputs the first pattern within the ()
"""


def find_price():
    locator = 'article.product_pod div.product_price p.price_color'
    search_item_price = soup.select_one(locator).string

    pattern = re.compile(r'[^£]+')
    item_price_list = (pattern.findall(search_item_price))

    # convert list to string and convert to float
    item_price = float("".join(item_price_list))
    print(item_price * 0.8)


def find_rating():
    locator = 'article.product_pod p.star-rating'
    star_rating_tag = soup.select_one(locator)

    classes = star_rating_tag.attrs['class']  # ['star-rating', 'Three'] or ['Three', 'star-rating']
    # rating_classes = [c for c in classes if c != 'star-rating']
    rating_classes = list(filter(lambda c: c != 'star-rating', classes))
    print(rating_classes[0])


find_item_name()
find_item_link()
find_price()
find_rating()

# star_rating_tag = soup.find('p', {'class': 'star-rating'})
