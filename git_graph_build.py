import networkx as nx
import git
from matplotlib import pyplot as plt

repo = git.Repo(search_parent_directories=True)


def build_graph():
    G = nx.Graph()
    for branch in repo.branches:
        print(f'Branch: {branch.name}')
        commits = list(repo.iter_commits(branch))
        for commit in commits:
            print(f'  Commit: {commit.hexsha} - {commit.message.strip()}')
            G.add_node(commit.hexsha[:2])  # TODO: replace with node ID so can store more info
            if commit.parents:
                for parent in commit.parents:
                    G.add_edge(parent.hexsha[:2], commit.hexsha[:2])
    return G


def visualize_graph(G):
    vertical_positions = {node: (0, index) for index, node in enumerate(G.nodes)}
    pos = nx.spring_layout(G, pos=vertical_positions, fixed=vertical_positions.keys())
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightblue', font_size=12, font_weight='bold')
    plt.savefig("graph.png")
    plt.show()


if __name__ == '__main__':
    G = build_graph()
    visualize_graph(G)









