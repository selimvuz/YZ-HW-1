import queue

def a_star(start, goal, graph, h):
    open_set = queue.PriorityQueue()
    open_set.put((h[start], start))
    came_from = {start: None}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while not open_set.empty():
        current = open_set.get()[1]
        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + graph[current][neighbor]
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + h[neighbor]
                open_set.put((f_score, neighbor))

    return None

def best_first(start, goal, graph, h):
    open_set = queue.PriorityQueue()
    open_set.put((h[start], start))
    came_from = {start: None}

    while not open_set.empty():
        current = open_set.get()[1]
        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in graph[current]:
            if neighbor not in came_from:
                came_from[neighbor] = current
                open_set.put((h[neighbor], neighbor))

    return None

def reconstruct_path(came_from, current):
    path = []
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path


# Kara yolu mesafeleri
graph = {
    'Tamil Nadu': {'Maharashtra': 1222, 'Chhattisgarh': 1500, 'Odisha': 1500},
    'Maharashtra': {'Tamil Nadu': 1222, 'Gujarat': 790, 'Madhya': 747, 'Chhattisgarh': 730},
    'Madhya': {'Gujarat': 886, 'Chhattisgarh': 500, 'Rajasthan': 827, 'Bihar': 929},
    'Chhattisgarh': {'Tamil Nadu': 1500, 'Maharashtra': 730, 'Madhya': 500, 'Bihar': 822, 'Odisha': 411},
    'Odisha': {'Tamil Nadu': 1500, 'Bihar': 878, 'Chhattisgarh': 411},
    'Gujarat': {'Maharashtra': 790, 'Madhya': 886, 'Rajasthan': 652},
    'Rajasthan': {'Madhya': 827, 'Gujarat': 652, 'Ladakh': 1270, 'Bihar': 1280},
    'Bihar': {'Madhya': 929, 'Rajasthan': 1280, 'Ladakh': 2030, 'Odisha': 878, 'Chhattisgarh': 822, 'Nagaland': 1327},
    'Ladakh': {'Rajasthan': 1270, 'Bihar': 2030},
    'Nagaland': {'Bihar': 1327}
}

# Her şehir için kuş uçuşu mesafelerini içeren sözlük
h = {
    'Tamil Nadu': 1175,
    'Maharashtra': 900,
    'Madhya': 650,
    'Gujarat': 1340,
    'Rajasthan': 1270,
    'Ladakh': 1700,
    'Bihar': 645,
    'Odisha': 0,
    'Chhattisgarh': 270,
    'Nagaland': 1240
}

# Başlangıç ve bitiş noktalarımız:
start = 'Rajasthan'
goal = 'Odisha'

# A* algoritmasının sonucu
path = a_star(start, goal, graph, h)
print("A* ile bulunan yol:", path)

# Best First algoritmasının sonucu
path = best_first(start, goal, graph, h)
print("BFS ile bulunan yol:", path)
