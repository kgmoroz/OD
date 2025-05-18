# Реализация графа на основе списка смежности.
# Можно задать, будет ли граф ориентированным (направленным) или нет.

class Graph:
    def __init__(self, directed=False):
        # Словарь для хранения списка смежности: вершина -> список соседей
        self.adj_list = {}

        # Флаг, определяющий направленность графа
        self.directed = directed

    def add_vertex(self, v):
        """
        Добавить вершину в граф.
        Если такая вершина уже существует — ничего не делаем.
        """
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, u, v):
        """
        Добавить ребро между вершинами u и v.
        Если граф направленный — добавляется только u -> v.
        Если не направленный — добавляется и v -> u.
        """
        # Убедимся, что обе вершины существуют
        self.add_vertex(u)
        self.add_vertex(v)

        # Добавляем вершину v в список смежности u
        self.adj_list[u].append(v)

        # Если граф не направленный, добавляем обратное ребро
        if not self.directed:
            self.adj_list[v].append(u)

    def display(self):
        """
        Напечатать список смежности для всех вершин графа.
        Удобно для визуальной проверки структуры графа.
        """
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex}: {neighbors}")

    def dfs(self, start, visited=None):
        """
        Обход в глубину (DFS, Depth-First Search).
        Рекурсивно посещает вершины, начиная с указанной.
        """
        if visited is None:
            visited = set()  # Множество посещённых вершин создаётся один раз

        visited.add(start)   # Помечаем текущую вершину как посещённую
        print(start, end=" ")  # Выводим текущую вершину

        # Рекурсивно обходим все непосещённые соседние вершины
        for neighbor in self.adj_list.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start):
        """
        Обход в ширину (BFS, Breadth-First Search).
        Используется очередь для последовательного посещения соседей.
        """
        visited = set()     # Множество уже посещённых вершин
        queue = [start]     # Очередь начинается с вершины старта
        visited.add(start)  # Помечаем стартовую вершину как посещённую

        while queue:
            vertex = queue.pop(0)  # Извлекаем первый элемент из очереди
            print(vertex, end=" ") # Печатаем его

            # Добавляем в очередь всех непосещённых соседей
            for neighbor in self.adj_list.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

# -------------------------------
# Пример использования графа:
# -------------------------------

g = Graph(directed=False)      # Создаём неориентированный граф

# Добавляем рёбра между вершинами
g.add_edge("A", "B")           # A <-> B
g.add_edge("A", "C")           # A <-> C
g.add_edge("B", "D")           # B <-> D
g.add_edge("C", "D")           # C <-> D

# Выводим список смежности
g.display()
# Ожидаемый вывод:
# A: ['B', 'C']
# B: ['A', 'D']
# C: ['A', 'D']
# D: ['B', 'C']

print("DFS:")
g.dfs("A")  # Обход в глубину от A, например: A B D C

print("\nBFS:")
g.bfs("A")  # Обход в ширину от A: A B C D