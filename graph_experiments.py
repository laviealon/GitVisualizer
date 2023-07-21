import networkx as nx

if __name__ == '__main__':
    G = nx.DiGraph()
    G.add_edge('a', 'b', weight=0.6)
    nx.draw(G, pos=nx.circular_layout(G), node_color='r', edge_color='b')
    print(G.nodes())