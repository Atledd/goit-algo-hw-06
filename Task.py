import networkx as nx
import matplotlib.pyplot as plt

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
# DFS
print("\nDFS шлях від Дарницького:")
path_dfs = list(nx.dfs_edges(city_graph, source="Дарницький"))
print(path_dfs)

# BFS
print("\nBFS шлях від Дарницького:")
path_bfs = list(nx.bfs_edges(city_graph, source="Дарницький"))
print(path_bfs)

# Завдання 3: Алгоритм Дейкстри
print("\nНайкоротші шляхи від Данрницього району:")
dijkstra_paths = nx.single_source_dijkstra_path(city_graph, source="Дарницький")
dijkstra_lengths = nx.single_source_dijkstra_path_length(city_graph, source="Дарницький")

for target, path in dijkstra_paths.items():
    print(f"Шлях до {target}: {path}, Довжина: {dijkstra_lengths[target]} км")