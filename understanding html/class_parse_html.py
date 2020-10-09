import re  # import should come first

from bs4 import BeautifulSoup
from locators.class_parse_locators import ParsedItemLocators as ItemLocators

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


class ParsedItem:
    """
    takes a HTML page/part of it, and find properties of an item in it
    """

    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    def name(self):
        """
        :return: the name of the title from the a tag
        """
        locator = ItemLocators.NAME_LOCATOR
        item_link = self.soup.select_one(locator)
        item_title = item_link.attrs['title']
        return item_title

    def link(self):
        """
        :return: the href
        """
        locator = ItemLocators.LINK_LOCATOR
        item_href = self.soup.select_one(locator).attrs['href']
        return item_href

    """
    def price_his(self):
        locator = 'article.product_pod div.product_price p.price_color'
        item_price = self.soup.select_one(locator).string  # outputs -> £51.77

        pattern = '£([0-9]+\.[0-9]+)' # to match £51.77
        matcher = re.search(pattern, item_price)
        # print(matcher.group(0))  # outputs the entire pattern
        return matcher.group(1)  # outputs the first pattern within the ()
    """

    def price(self):
        locator = ItemLocators.PRICE_LOCATOR
        search_item_price = self.soup.select_one(locator).string

        pattern = re.compile(r'[^£]+')
        item_price_list = (pattern.findall(search_item_price))

        # convert list to string and convert to float
        item_price = float("".join(item_price_list))
        return item_price * 0.8

    def rating(self):
        locator = ItemLocators.RATING_LOCATOR
        star_rating_tag = self.soup.select_one(locator)

        classes = star_rating_tag.attrs['class']  # ['star-rating', 'Three'] or ['Three', 'star-rating']
        # rating_classes = [c for c in classes if c != 'star-rating']
        rating_classes = list(filter(lambda r: r != 'star-rating', classes))
        # print(type(rating_classes[0]))
        return rating_classes[0]  # gets the item as a string


item = ParsedItem(ITEM_HTML)
print(item.name())

# star_rating_tag = soup.find('p', {'class': 'star-rating'})
