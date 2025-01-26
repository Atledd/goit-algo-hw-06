import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import heapq

#Задання 1
# Створимо граф, який представляє транспортну мережу міста
city_graph = nx.Graph()

# Додамо вершини (наприклад, райони міста)
nodes = [
    "Дарницький", "Дніпровський", "Деснянський", "Оболонський", "Святошинський",
    "Шевченківський", "Солом'янський", "Голосіївський", "Поділ", "Печерськ"
]
city_graph.add_nodes_from(nodes)

# Додамо ребра (дороги між районами) з вагами (відстань у км)
edges = [
    ("Дарницький", "Дніпровський", 3), ("Дарницький", "Голосіївський", 5), ("Дарницький", "Печерськ", 2), 
    ("Голосіївський", "Печерськ", 2), ("Голосіївський", "Солом'янський", 1), ("Солом'янський", "Святошинський", 3),
    ("Солом'янський", "Шевченківський", 3), ("Святошинський", "Шевченківський", 6), ("Святошинський", "Поділ", 3), 
    ("Святошинський", "Оболонський", 5), ("Печерськ", "Шевченківський", 2), ("Печерськ", "Дніпровський", 2),
    ("Поділ", "Шевченківський", 1), ("Поділ", "Оболонський", 3), ("Поділ", "Дніпровський", 4),
    ("Деснянський", "Дніпровський", 2), ("Деснянський", "Оболонський", 5),
]
city_graph.add_weighted_edges_from(edges)

# Візуалізуємо граф
pos = nx.spring_layout(city_graph, seed=42)
plt.figure(figsize=(8, 6))
nx.draw(city_graph, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10)
edge_labels = nx.get_edge_attributes(city_graph, 'weight')
nx.draw_networkx_edge_labels(city_graph, pos, edge_labels=edge_labels)
plt.title("Transport Network")
plt.show()

# Аналіз характеристик графа
num_nodes = city_graph.number_of_nodes()
num_edges = city_graph.number_of_edges()
degree_of_nodes = dict(city_graph.degree())

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступені вершин:")
for node, degree in degree_of_nodes.items():
    print(f"  {node}: {degree}")

# Завдання 2: Реалізація DFS і BFS
graph_dict = nx.to_dict_of_lists(city_graph)  # Перетворюємо граф NetworkX у словник для ручних алгоритмів

# DFS
def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
        path = []
    else:
        path = []

    visited.add(vertex)
    path.append(vertex) # Додаємо вершину до шляху

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            path.extend(dfs_recursive(graph, neighbor, visited))
    
    return path

print("\nDFS шлях від Дарницького:")
path_dfs = dfs_recursive(graph_dict, "Дарницький")
print(path_dfs)

# BFS
def bfs_recursive(graph, queue, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    if not queue:
        return path
    vertex = queue.popleft()
    if vertex not in visited:
        visited.add(vertex)
        path.append(vertex)
        queue.extend(set(graph[vertex]) - visited)
    return bfs_recursive(graph, queue, visited, path)

print("\nBFS шлях від Дарницького:")
queue = deque(["Дарницький"])
path_bfs = bfs_recursive(graph_dict, queue)
print(path_bfs)

# Завдання 3: Алгоритм Дейкстри
def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph.nodes}
    distances[start] = 0
    priority_queue = [(0, start)] # Черга: (відстань, вершина)
    visited = set()

    while priority_queue:
        # Отримуємо вершину з найменшою відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Пропускаємо вже відвідані вершини
        if current_vertex in visited:
            continue
        visited.add(current_vertex)

        # Оновлюємо відстані до сусідів
        for neighbor, attributes in graph[current_vertex].items():
            weight = attributes['weight']
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

print("\nНайкоротший шлях від Данрницього району:")
city_graph.add_nodes_from(nodes)
city_graph.add_weighted_edges_from(edges)
distances = dijkstra(city_graph, "Дарницький")

for vertex, distance in distances.items():
    print(f"Відстань від Дарницького району до {vertex}: {distance} км")