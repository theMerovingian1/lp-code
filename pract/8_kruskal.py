class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, weight):
        self.graph.append((u, v, weight))

    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find_parent(parent, x)
        y_root = self.find_parent(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal_mst(self):
        result = []
        parent = [i for i in range(self.V)]
        rank = [0] * self.V

        # Sort all edges by weight
        self.graph = sorted(self.graph, key=lambda item: item[2])

        i = 0  # Index for sorted edges
        e = 0  # Index for result[]

        while e < self.V - 1 and i < len(self.graph):
            u, v, weight = self.graph[i]
            i += 1
            x = self.find_parent(parent, u)
            y = self.find_parent(parent, v)

            if x != y:
                e += 1
                result.append((u, v, weight))
                self.union(parent, rank, x, y)

        mst_cost = sum(weight for _, _, weight in result)
        return mst_cost


def add_edges(graph):
    while True:
        u = int(input("Enter vertex u (-1 to finish): "))
        if u == -1:
            break
        v = int(input("Enter vertex v: "))
        weight = int(input("Enter weight: "))
        graph.add_edge(u, v, weight)


def main():
    num_vertices = int(input("Enter the number of vertices: "))
    g = Graph(num_vertices)
    add_edges(g)

    mst_cost = g.kruskal_mst()
    print("Minimum Spanning Tree Cost:", mst_cost)


if __name__ == "__main__":
    main()
