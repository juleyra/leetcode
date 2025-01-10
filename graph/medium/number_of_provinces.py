def find(parent, x):
    while parent[x] != x:  # Поки не знайдемо корінь
        x = parent[x]
    return x


def union(parent, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    if rootX != rootY:
        parent[rootY] = rootX  # Просто з'єднуємо rootY до rootX


def countProvinces(isConnected):
    n = len(isConnected)
    parent = list(range(n))  # Кожне місто саме собі батько

    # Об'єднуємо міста, які безпосередньо з'єднані
    for i in range(n):
        for j in range(i + 1, n):
            if isConnected[i][j] == 1:
                union(parent, i, j)
    print(parent)
    # Підраховуємо кількість унікальних коренів (провінцій)
    provinces = set(parent)
    return len(provinces)


# Приклад виклику
isConnected = [
    [1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1]
]
print(countProvinces(isConnected))  # Виведе 3
