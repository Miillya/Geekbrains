# Задание №3
# Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны, по
# алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.


import random


def graph_gen(number_vertices):
    graph = []
    for i in range(number_vertices):
        number_edges = random.randint(1, number_vertices - 1)
        graph.append([])
        l = 0
        while l < number_edges:
            vertex = random.randint(0, number_vertices - 1)
            if vertex != i and vertex not in graph[i]:
                graph[i].append(vertex)
                l += 1

    return graph


def dfs(graph, start, visited=[]):
    if len(visited) == 0:
        visited = []
    visited.append(start)
    for i in graph[start]:
        if i not in visited:
            dfs(graph, i, visited)
    return visited


n = int(input('Введите количество вершин: '))
input_point = int(input("Введите точку входа: "))


graph = graph_gen(n)
print('Граф', *graph, sep='\n')
print('Обход графа: ', dfs(graph, input_point))
