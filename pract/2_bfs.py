from collections import deque


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        self.graph.setdefault(u, []).append(v)
        self.graph.setdefault(v, []).append(u)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')

            for neighbor in self.graph.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


def main():
    graph = Graph()
    while True:
        print("\n1. Add Edge")
        print("2. Breadth First Search (BFS)")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            u = int(input("Enter vertex u: "))
            v = int(input("Enter vertex v: "))
            graph.add_edge(u, v)
        elif choice == 2:
            start_vertex = int(input("Enter the starting vertex for BFS: "))
            print("BFS Traversal:")
            graph.bfs(start_vertex)
            print()
        elif choice == 3:
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
