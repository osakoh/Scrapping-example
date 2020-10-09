from bs4 import BeautifulSoup


SIMPLE_HTML = '''
<html lang="en">
<head></head> 

<body>
    <h1>Title H1</h1>
    <p class="subtitle">This is a paragraph</p>
    <p>Another paragraph without a class</p>
    <ul>
        <li>Ann</li>
        <li>Sue</li>
        <li>Pau</li>
        <li>Sam</li>
    </ul>
</body>
</html>
'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')


def find_title():
    h1_tag = simple_soup.find('h1')  # find(): to get a single elements
    print(h1_tag.string)  # '.string': used to get the text within the HTML element


def find_list_items():
    list_items = simple_soup.find_all('li')  # find_all(): to get many elements
    list_items = [items.string for items in list_items]
    print(list_items)


def find_subtitle():
    paragraph = simple_soup.find('p', {'class': 'subtitle'})
    print(paragraph.string)


def find_other_paragraph():
    paragraphs = simple_soup.find_all('p')
    print(paragraphs)
    # p.attrs: is a dictionary. Elements can be accessed using '.get()' or p.attrs['class'].
    # '.get()' is better because it doesn't output a keyError if the element isn't in the dict but returns None
    # other_paragraph = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]
    other_paragraph = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]
    print(other_paragraph[0].string)


find_title()
find_list_items()
find_subtitle()
find_other_paragraph()