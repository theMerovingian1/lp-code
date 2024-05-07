class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        self.graph.setdefault(u, []).append(v)
        self.graph.setdefault(v, []).append(u)

    def dfs_util(self, v, visited):
        visited.add(v)
        print(v, end=' ')

        for neighbor in self.graph.get(v, []):
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = set()
        self.dfs_util(start, visited)


def main():
    graph = Graph()
    while True:
        print("\n1. Add Edge")
        print("2. Depth First Search (DFS)")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            u = int(input("Enter vertex u: "))
            v = int(input("Enter vertex v: "))
            graph.add_edge(u, v)
        elif choice == 2:
            start_vertex = int(input("Enter the starting vertex for DFS: "))
            print("DFS Traversal:")
            graph.dfs(start_vertex)
            print()
        elif choice == 3:
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
