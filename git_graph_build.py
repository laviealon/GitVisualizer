import networkx as nx
import git
from matplotlib import pyplot as plt

repo = git.Repo(search_parent_directories=True)


def build_graph():
    G = nx.Graph()
    pos = {}
    for branch in repo.branches:
        print(f'Branch: {branch.name}')
        commits = list(repo.iter_commits(branch))
        for commit in commits:
            print(f'  Commit: {commit.hexsha} - {commit.message.strip()}')
            G.add_node(commit.hexsha[:2])  # TODO: replace with node ID so can store more info
            if commit.parents:
                for parent in commit.parents:
                    G.add_edge(parent.hexsha[:2], commit.hexsha[:2])
            else:
                pos[commit.hexsha[:2]] = [2, 10]
    return G


def visualize_graph(G):
    nx.draw_networkx(G)
    plt.savefig("graph.png")


if __name__ == '__main__':
    G = build_graph()
    visualize_graph(G)









