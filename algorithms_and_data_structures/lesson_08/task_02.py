# Задание №2
# Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин, которые
# необходимо обойти.

from collections import deque


g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra(graph, start):
    length = len(graph)
    s = start
    is_visited = [False] * length  # посещена ли вершина
    cost = [float('inf')] * length  # вес пути

    parent = [-1] * length

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]

                    parent[i] = start

        min_cost = float('inf')

        for i in range(length):

            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    parent[s] = s

    way = {}
    for i in range(length):
        way[i] = deque([i])

    for i in way:
        if parent[i] != (-1):
            if i == s:
                continue
            spam = i

            while spam != s:
                way[i].appendleft(parent[spam])
                spam = parent[spam]
        else:
            way[i] = ['нет пути']

    return cost, way


s = int(input('От какой вершины идти (от 0 до 7): '))

if 0 <= s <= 7:

    cost, way = dijkstra(g, s)

    print(f'\n Кратчайшие пути от вершины {s}:\n {cost}\n')

    print('Вершины, которые надо обойти')
    for k in way:
        print(k, ':', *way[k])

else:
    print('Некорректный ввод, начните сначала')
