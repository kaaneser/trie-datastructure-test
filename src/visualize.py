import networkx as nx
import matplotlib.pyplot as plt

def visualize_trie(trie):
    G = nx.DiGraph()

    def add_edges(node, prefix=""):
        for char, child_node in node.children.items():
            G.add_edge(prefix, prefix + char)
            add_edges(child_node, prefix + char)

    add_edges(trie.root)
    pos = nx.spring_layout(G, seed=100)
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, node_size=3000, node_color="skyblue", with_labels=True)
    plt.title("Trie Visualization")
    plt.show()