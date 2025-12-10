from Queues import *
class Node:
    def __init__(self, val):
        self.value = val
        self.edges = []

    def set_value(self, val):
        self.value = val

    def get_value(self):
        return self.value

    def get_edges(self):
        return self.edges

    def __str__(self):
        return "Node with value " + str(self.value)


class Graph:
    def __init__(self):
        self.nodes = []

    def get_nodes(self):
        return self.nodes

    def add_node(self, n):
        if n in self.get_nodes():
            raise ValueError("node already exists")
        self.nodes.append(n)

    def add_edge(self, n1, n2):
        if self.edge_exists(n1, n2) == True:
            raise ValueError("node already exists")
        else:
            n1.edges.append(n2)
            n2.edges.append(n1)

    def __str__(self):
        s = "Graph with the following nodes:"
        for n in self.get_nodes():
            s += "\n\t" + str(n)
        return s

    def edge_exists(self, n1, n2):
        return n2 in n1.get_edges()

    def find_node(self, v):
        # Given a value v, this method returns the node in the graph that has value v.
        # This method is useful for building the hyperlanes from the provided list.
        for n in self.get_nodes():
            if n.get_value() == v:
                return n
        raise ValueError("Node not found.")

    def shortest_path(self, s1_name, s2_name):
        s1_node = self.find_node(s1_name)
        s2_node = self.find_node(s2_name)

        visited = []
        to_visit = Queue()
        to_visit.enqueue([s1_node])
        visited.append(s1_node)

        while to_visit.size() != 0:
            temp = to_visit.dequeue()
            current_system = temp[-1]
            current_system_edges = current_system.get_edges()
            if current_system == s2_node:
                return [node.get_value() for node in temp]
            for i in current_system_edges:
                if i not in visited:
                    new_path = temp + [i]
                    to_visit.enqueue(new_path)
                    visited.append(i)

        return "No path found- hyperlink between these galaxies does not exist."

    def shortest_path_length(self, s1_name, s2_name):
        return (len(self.shortest_path(s1_name, s2_name)) -1)