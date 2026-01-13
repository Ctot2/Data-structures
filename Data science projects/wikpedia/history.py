import wikipediaapi
from graph import *

# Initialize Wikipedia API
wiki_wiki = wikipediaapi.Wikipedia(user_agent='Wikipedia_Graph (williamso27@gfacademy.org)', language='en')
page_py = wiki_wiki.page('Wikipedia')
print("Page - Exists: %s" % page_py.exists())

# Initialize the graph
wikipedia = Graph()

# Add the main page as a node
main_node = Node("Wikipedia")
wikipedia.add_node(main_node)

# Get links from the main page
link_list = list(page_py.links.keys())

# Add links from the main page as nodes
for link in link_list:
    if not any(node.get_value() == link for node in wikipedia.get_nodes()):
        wikipedia.add_node(Node(link))

# Get links from the first linked page
page2 = wiki_wiki.page(link_list[0])
link_list2 = list(page2.links.keys())

# Add links from the second page as nodes
for link in link_list2:
    if not any(node.get_value() == link for node in wikipedia.get_nodes()):
        wikipedia.add_node(Node(link))

# Add edges between the main page and the second page's links
for link in link_list2:
    try:
        n1 = wikipedia.find_node(link)
        n2 = wikipedia.find_node("Wikipedia")
        wikipedia.add_edge(n1, n2)
    except ValueError:
        print(f"Node not found for link: {link}")

# Check if an edge exists between "Wikipedia" and one of the second page's links
try:
    n1 = wikipedia.find_node("Wikipedia")
    n2 = wikipedia.find_node(link_list2[5])
    print(wikipedia.edge_exists(n1, n2))
except ValueError:
    print(f"Node not found for link: {link_list2[5]}")

