# Задание №1
# На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

n = int(input('Ведите количество друзей (N): '))

graph = [[0 if i == j else 1 for j in range(n)] for i in range(n)]

handshake = 0

for i in range(n):
    for j in range(i, n):
        if graph[i][j] == 1:
            handshake += 1

print(f'Количество рукопожатий: {handshake}')
