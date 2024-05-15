import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
import numpy as np

# Заданные точки
points = np.array([
    [-8, -8],
    [-8, 3],
    [-6, 7],
    [4, 5],
    [8, 4]
])

# Построение триангуляции Делоне
tri = Delaunay(points)

# Визуализация триангуляции
plt.triplot(points[:, 0], points[:, 1], tri.simplices)
plt.plot(points[:, 0], points[:, 1], 'o')

# Подписи для точек
for i, txt in enumerate(['A1', 'A2', 'A3', 'A4', 'A5']):
    plt.annotate(txt, (points[i, 0], points[i, 1]))

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Триангуляция Делоне')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
