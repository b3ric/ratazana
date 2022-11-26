import re
import requests
from bs4 import BeautifulSoup

HTML_TAGS = re.compile(r'<.*?>')
URL_MATCH = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'

def fetch_content(url: str):

    if not _valid_url(url):
        return None

    content = {}
    paragraphs = []

    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser')

    # Parse title and clean HTML tags
    title = re.sub(HTML_TAGS, '', str(soup.find('title')))

    for p in soup.find_all("p"):
        # Parse each paragrath and clean HTML tags
        p = re.sub(HTML_TAGS, '', str(p))
        paragraphs.append(p)

    content = {
        'title': title,
        'body': paragraphs
    }

    return content

def _valid_url(url:str):
    regxp = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'
    return re.fullmatch(regxp, url)
