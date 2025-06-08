import networkx as nx
from collections import deque
from HW6_1 import kyiv_metro

def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in graph.neighbors(vertex):
                stack.append((neighbor, path + [neighbor]))
    return None

def bfs_path(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        (vertex, path) = queue.popleft()
        if vertex == goal:
            return path
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph.neighbors(vertex):
                queue.append((neighbor, path + [neighbor]))
    return None

if __name__ == "__main__":
    G = kyiv_metro()
    start_station = "Академмістечко"
    end_station = "Теремки"

    dfs = dfs_path(G, start_station, end_station)
    bfs = bfs_path(G, start_station, end_station)

    print(f"🔎 DFS шлях ({len(dfs)} станцій):\n{' → '.join(dfs)}")
    print(f"\n🔎 BFS шлях ({len(bfs)} станцій):\n{' → '.join(bfs)}")
