import networkx as nx
from HW6_1 import kyiv_metro

def weighted_kyiv_metro():
    G = kyiv_metro()
    for u, v in G.edges():
        G[u][v]["weight"] = 1
    return G
G_weighted = weighted_kyiv_metro()

# найкоротші шляхи (кількість станцій як вага = 1)
shortest_paths = dict(nx.all_pairs_dijkstra_path_length(G_weighted, weight="weight"))

print("Найкоротші шляхи (кількість станцій):")
print(f"Академмістечко → Теремки: {shortest_paths['Академмістечко']['Теремки']} станцій")
print(f"Сирець → Позняки: {shortest_paths['Сирець']['Позняки']} станцій")
print(f"Героїв Дніпра → Арсенальна: {shortest_paths['Героїв Дніпра']['Арсенальна']} станцій")