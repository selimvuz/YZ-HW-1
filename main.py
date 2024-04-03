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
    'Madhya': {'Gujarat': 886, 'Chhattisgarh': 500, 'Rajasthan': 827, 'Bihar': 1441},
    'Chhattisgarh': {'Tamil Nadu': 1500, 'Maharashtra': 730, 'Madhya': 500, 'Bihar': 822, 'Odisha': 411},
    'Odisha': {'Tamil Nadu': 1500, 'Bihar': 878, 'Chhattisgarh': 411},
    'Gujarat': {'Maharashtra': 790, 'Madhya': 886, 'Rajasthan': 652},
    'Rajasthan': {'Madhya': 827, 'Gujarat': 652, 'Ladakh': 1270, 'Bihar': 1280},
    'Bihar': {'Madhya': 929, 'Rajasthan': 1280, 'Ladakh': 2030, 'Odisha': 878, 'Chhattisgarh': 822, 'Nagaland': 1327},
    'Ladakh': {'Rajasthan': 1270, 'Bihar': 2030},
    'Nagaland': {'Bihar': 1327}
}

"""
graph = {
    'Tamil Nadu': {'Maharashtra': 1222, 'Madhya': 1713, 'Gujarat': 1961, 'Rajasthan': 2233, 'Ladakh': 3452, 'Bihar': 2407, 'Odisha': 1500, 'Chhattisgarh': 1500, 'Nagaland': 3456},
    'Maharashtra': {'Tamil Nadu': 1222, 'Madhya': 747, 'Gujarat': 790, 'Rajasthan': 1048, 'Ladakh': 2267, 'Bihar': 1441, 'Odisha': 1131, 'Chhattisgarh': 730, 'Nagaland': 2752},
    'Madhya': {'Tamil Nadu': 1713, 'Maharashtra': 747, 'Gujarat': 886, 'Rajasthan': 827, 'Ladakh': 1743, 'Bihar': 929, 'Odisha': 902, 'Chhattisgarh': 500, 'Nagaland': 2240},
    'Gujarat': {'Tamil Nadu': 1961, 'Maharashtra': 790, 'Madhya': 886, 'Rajasthan': 652, 'Ladakh': 1871, 'Bihar': 1940, 'Odisha': 1671, 'Chhattisgarh': 1460, 'Nagaland': 3163},
    'Rajasthan': {'Tamil Nadu': 2233, 'Maharashtra': 1048, 'Madhya': 827, 'Gujarat': 652, 'Ladakh': 1270, 'Bihar': 1280, 'Odisha': 1694, 'Chhattisgarh': 1310, 'Nagaland': 2627},
    'Ladakh': {'Tamil Nadu': 3452, 'Maharashtra': 2267, 'Madhya': 1743, 'Gujarat': 1871, 'Rajasthan': 1270, 'Bihar': 2030, 'Odisha': 2519, 'Chhattisgarh': 2225, 'Nagaland': 3341},
    'Bihar': {'Tamil Nadu': 2407, 'Maharashtra': 1441, 'Madhya': 929, 'Gujarat': 1940, 'Rajasthan': 1280, 'Ladakh': 2030, 'Odisha': 878, 'Chhattisgarh': 822, 'Nagaland': 1327},
    'Odisha': {'Tamil Nadu': 1500, 'Maharashtra': 1131, 'Madhya': 902, 'Gujarat': 1671, 'Rajasthan': 1694, 'Ladakh': 2519, 'Bihar': 878, 'Chhattisgarh': 411, 'Nagaland': 2154},
    'Chhattisgarh': {'Tamil Nadu': 1500, 'Maharashtra': 730, 'Madhya': 500, 'Gujarat': 1460, 'Rajasthan': 1310, 'Ladakh': 2225, 'Bihar': 822, 'Odisha': 411, 'Nagaland': 2170},
    'Nagaland': {'Tamil Nadu': 3456, 'Maharashtra': 2752, 'Madhya': 2240, 'Gujarat': 3163, 'Rajasthan': 2627, 'Ladakh': 3341, 'Bihar': 1327, 'Odisha': 2154, 'Chhattisgarh': 2170}
}
"""

# h, her şehir için kuş uçuşu mesafelerini içeren sözlüktür.
h = {
    'Tamil Nadu': 0,
    'Maharashtra': 1008,
    'Madhya': 1320,
    'Gujarat': 1490,
    'Rajasthan': 1830,
    'Ladakh': 2570,
    'Bihar': 1790,
    'Odisha': 1175,
    'Chhattisgarh': 1180,
    'Nagaland': 2360
}

# Başlangıç ve bitiş noktalarınız:
start = 'Rajasthan'
goal = 'Odisha'

# A* Algoritmasını kullanarak yolu bulun
path = a_star(start, goal, graph, h)
print("A* ile bulunan yol:", path)

# Best First Algoritmasını kullanarak yolu bulun
path = best_first(start, goal, graph, h)
print("Best First ile bulunan yol:", path)
