import networkx as nx
from matplotlib import pyplot as plt

main = ['be', '60', '9e']
bugFix = ['44', 'ac', '06', '4e', 'dd', 'be', '60', '9e']
branches = [main, bugFix]

G = nx.Graph()

for branch in branches:
    for i in range(len(branch)):
        commit_hexsha = branch[i]
        G.add_node(commit_hexsha[:2])
        if i + 1 < len(branch):
            parent_hexsha = branch[i + 1]
            G.add_edge(parent_hexsha[:2], commit_hexsha[:2])

vertical_positions = {node: (0, index) for index, node in enumerate(G.nodes)}
pos = nx.spring_layout(G, pos=vertical_positions, fixed=vertical_positions.keys())
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightblue', font_size=12, font_weight='bold')

if __name__ == '__main__':
    plt.show()


