import wikipediaapi
from pyvis.network import Network
from graph import *
import time
import random

wiki_wiki = wikipediaapi.Wikipedia(user_agent='Wikipedia_Graph (williamso27@gfacademy.org)', language='en')

def wiki_graph(start, repetitions):
    wikipedia = Graph()
    main_node = Node(start)
    wikipedia.add_node(main_node)
    length = 0
    visited = set()  # Keep track of visited pages
    visited.add(start)  # Mark the starting page as visited
    time.sleep(0.005)  # Rate limiting

    for i in range(repetitions):
        print(f"Repetition {i + 1}/{repetitions}: Fetching links for '{start}'")
        page_py = wiki_wiki.page(start)
        time.sleep(0.005)  # Rate limiting
        link_list = list(page_py.links.keys())

        if not link_list:  # Handle empty link_list
            print(f"No links found for page: {start}")
            break

        for link in link_list:
            # Check if the node already exists
            existing_node = next((node for node in wikipedia.get_nodes() if node.get_value() == link), None)
            if existing_node:
                wikipedia.add_edge(existing_node, main_node)
            #else:
                #new_node = Node(link)
                #wikipedia.add_node(new_node)
                #wikipedia.add_edge(new_node, main_node)

        # Find the next unvisited page
        next_start = None
        while True:
            link = random.choice(link_list)
            if link not in visited:
                next_start = link
                break

        if next_start is None:  # If no unvisited links are found, stop the loop
            print("No unvisited links found. Stopping.")
            break

        last_node = main_node
        # Update the starting page and main node for the next iteration
        start = next_start
        visited.add(start)  # Mark the new page as visited
        main_node = next((node for node in wikipedia.get_nodes() if node.get_value() == start), None)
        if not main_node:  # If the new starting node doesn't exist, create it
            main_node = Node(start)
            wikipedia.add_node(main_node)
        wikipedia.add_edge(last_node, main_node)

        length += len(link_list)

    # Print statistics
    print("this is", 100 * length / 7116000, "% of wikipedia")
    print(f"Total links processed: {length}")
    wikipedia.show_graph()


page = input("Choose your starting article: ")
wiki_graph(start=page, repetitions=0)