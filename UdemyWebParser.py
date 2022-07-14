from bs4 import BeautifulSoup

SIMPLE_HTML = """<html>
<head>HEADER</head>
<body>
<h1>Title</h1>
<p class="subtitle">Lorem ipsum dolor</p>
<p>This is a paragraph with no class... wah wah</p>
<ul>
    <li>Thai</li>
    <li>Jenna</li>
    <li>Brittany</li>
    <li>McKay</li>
</ul>
</body>
</html>"""

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')


def find_title():
    h1_tag = simple_soup.find('h1')
    print(h1_tag.string)


def find_list_items():
    list_items = simple_soup.find_all('li')
    list_contents = [e.string for e in list_items]
    print(list_contents)


def find_subtitle():
    paragraph_contents = simple_soup.find('p', attrs={"class": "subtitle"})
    print(paragraph_contents.string)


def find_other_paragraph():
    paragraph_all = simple_soup.find_all('p')
    second_paragraph = [p for p in paragraph_all if 'subtitle' not in p.attrs.get('class', [])]
    print(second_paragraph[0].string)


find_title()
find_list_items()
find_subtitle()
find_other_paragraph()
