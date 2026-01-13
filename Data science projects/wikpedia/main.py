import wikipediaapi
from pyvis.network import Network
from graph import *

wiki_wiki = wikipediaapi.Wikipedia(user_agent='Wikipedia_Graph (williamso27@gfacademy.org)', language='en')

while True:
    print("format your article request properly capitalized, with underscores between words, and specifiers in parenthesis. ")
    print("example formats: USA, Wikipedia, New_York_City, Orange_(color)")
    page = wiki_wiki.page(input("choose your starting article: "))
    print("Page - Exists: %s" % page.exists())