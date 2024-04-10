from graphviz import Digraph

class AfdView:
    def __init__(self):
        self.graph = Digraph()

    def add_node(self, node):
        self.graph.node(node)

    def add_edge(self, start, end, label):
        self.graph.edge(start, end, label=label)

    def render(self, filename):
        self.graph.render(filename, format='png', cleanup=True)