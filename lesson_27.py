import heapq
from collections import deque


graph = {}

graph['me'] = ['Oleksandr', 'Inna', 'Victor']
graph['Oleksandr'] = ['Anastasia', 'Andriy']
graph['Inna'] = ['Borys', 'Yevhen']
graph['Victor'] = ['Dmytro']
graph['Anastasia'] = []
graph['Andriy'] = []
graph['Borys'] = []
graph['Yevhen'] = []
graph['Dmytro'] = []


def search_music_fan():
    search_queue = deque()
    search_queue += graph['me']

    already_searched = set()
    while search_queue:
        person_name = search_queue.popleft()
        print('Name', person_name)
        if person_name not in already_searched:
            if person_name.startswith('B'):
                print(person_name, 'is a music fan!')
                return True
            else:
                search_queue += graph[person_name]
                already_searched.add(person_name)
    return False


# search_music_fan()

def djekstra_search(graph, start, goal):
    queue = [(0, start, [])]
    seen = set()

    while queue:
        cost, node, path = heapq.heappop(queue)
        if node in seen:
            continue

        path = path + [node]
        seen.add(node)

        if node == goal:
            return cost, path

        for neighbor, weight in graph[node].items():
            if neighbor not in seen:
                heapq.heappush(queue, (cost + weight, neighbor, path))

    return float('inf'), []


graph = {
    'A': {'B': 100, 'C': 1},
    'B': {},
    'C': {'D': 1},
    'D': {'B': 1}
}

cost, path = djekstra_search(graph, 'A', 'B')
print('Shortest path', path)
print('Total cost of path', cost)
