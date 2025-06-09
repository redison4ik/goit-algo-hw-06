import heapq
import networkx as nx
from HW6_1 import kyiv_metro  

def dijkstra_metro(graph: nx.Graph, start: str) -> dict:
    # Початкові відстані — нескінченність, крім стартової
    distances = {node: float('inf') for node in graph.nodes()}
    distances[start] = 0

    # Пріоритетна черга: (відстань, вузол)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor].get("weight", 1)
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

G_metro = kyiv_metro()

for u, v in G_metro.edges():
    G_metro[u][v]["weight"] = 1

shortest_paths = dijkstra_metro(G_metro, "Академмістечко")

print("Найкоротші шляхи (кількість станцій):")
print(f"Академмістечко → Теремки: {shortest_paths['Теремки']} станцій")
print(f"Сирець → Позняки: {shortest_paths['Позняки']} станцій")
print(f"Героїв Дніпра → Арсенальна: {shortest_paths['Арсенальна']} станцій")