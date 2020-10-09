class ParsedItemLocators:
    """
    Locates an item in the HTML page.

    Allows us to see what our code will be looking at as well as change it quickly if the locator changes.
    """
    NAME_LOCATOR = 'article.product_pod h3 a'
    LINK_LOCATOR = 'article.product_pod h3 a'
    PRICE_LOCATOR = 'article.product_pod div.product_price p.price_color'
    RATING_LOCATOR = 'article.product_pod p.star-rating'