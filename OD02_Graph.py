class Graph:
    def __init__(self, directed=False):
        self.adj_list = {}
        self.directed = directed

    def add_vertex(self, v):
        """Добавить вершину"""
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, u, v):
        """Добавить ребро u -> v (или u <-> v, если неориентированный)"""
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj_list[u].append(v)
        if not self.directed:
            self.adj_list[v].append(u)

    def display(self):
        """Вывести граф"""
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex}: {neighbors}")

    def dfs(self, start, visited=None):
        """Обход в глубину"""
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")
        for neighbor in self.adj_list.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start):
        """Обход в ширину"""
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")
            for neighbor in self.adj_list.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

# Пример использования
g = Graph(directed=False)
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")
g.display()

print("DFS:")
g.dfs("A")  # A B D C

print("\nBFS:")
g.bfs("A")  # A B C D