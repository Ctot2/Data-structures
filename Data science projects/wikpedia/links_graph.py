import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia(user_agent='Wikipedia_Graph (williamso27@gfacademy.org)', language='en')
page_py = wiki_wiki.page("2025_in_women's_road_cycling")
print(len(list(page_py.links.keys())))