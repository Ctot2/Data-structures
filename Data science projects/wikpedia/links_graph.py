import wikipediaapi
from pyvis.network import Network
from graph import *
import time
import random
from Stacks import *


wiki_wiki = wikipediaapi.Wikipedia(user_agent='Wikipedia_Graph (williamso27@gfacademy.org)', language='en')


history = Stack()
page_cache = {}


well_shit_counter = 0

def get_page(title): #got this off the internet b/c i couldn't figure out why i was being rate-limited
    if title not in page_cache:
        page_cache[title] = wiki_wiki.page(title)
    return page_cache[title]


def safe_links(page): #also got this off the internet for the same reason
    for i in range(5):
        try:
            return list(page.links.keys())
        except Exception:
            (time.sleep(0.5 + random.random())) # backoff
    return [] # give up

def wiki_graph(start, repetitions, well_shit_counter=0):
    wikipedia = Graph()
    main_node = Node(start)
    wikipedia.add_node(main_node)

    visited = set()
    visited.add(start)

    time.sleep(0.1 + random.random() * 0.2)
    current_page = start

    for i in range(repetitions):
        print(f"repetition {i} out of {repetitions}: {current_page}")
        page_py = get_page(current_page)
        history.push(page_py)

        print("1Fetching links for:", current_page)
        link_list = safe_links(page_py)

        if len(link_list) == 0:
            history.pop()
            if history.size() == 0:
                continue

            page2_obj = history.pop()
            link_list = safe_links(page2_obj)
            current_page = page2_obj.title

            print("2Fetching links for:", current_page)
            well_shit_counter += 1

            bonus_node = Node(current_page)
            wikipedia.add_node(bonus_node)
            visited.add(current_page)

        for existing_node in wikipedia.get_nodes():
            if existing_node.get_value() != current_page and existing_node.get_value() in link_list:
                wikipedia.add_edge(Node(current_page), existing_node)

        x = 0
        next_page = random.choice(link_list)
        while next_page in visited:
            next_page = random.choice(link_list)
            x += 1
            if x == len(link_list):
                history.pop()
                next_page = history.pop()

                x = 0
                link_list = safe_links(next_page)
                next_page = random.choice(link_list)


        new_node = Node(next_page)
        current_page_node = Node(current_page)
        wikipedia.add_node(new_node)
        wikipedia.add_edge(current_page_node, new_node)

        visited.add(next_page)
        current_page = next_page

    print(well_shit_counter)
    wikipedia.show_graph()

wiki_graph(start="Wikipedia", repetitions=5000)