import networkx as nx
import matplotlib.pyplot as plt


class GraphVisualization:
    def __init__(self):
        self.visual = []

    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        pos = {1: [2, 5], 2: [2, 4], 3: [2, 3], 4: [2, 2], 5: [2, 1]}
        nx.draw_networkx(G, pos)
        plt.savefig("graph.png")


if __name__ == '__main__':
    G = GraphVisualization()
    G.addEdge(1, 2)
    G.addEdge(2, 3)
    G.addEdge(3, 4)
    G.addEdge(4, 5)
    G.visualize()






