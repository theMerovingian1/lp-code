import sys


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def minKey(self, key, mstSet):
        min_val = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if key[v] < min_val and not mstSet[v]:
                min_val = key[v]
                min_index = v
        return min_index

    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1

        for _ in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] and not mstSet[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)


def get_input():
    num_vertices = int(input("Enter the number of vertices: "))
    g = Graph(num_vertices)
    print("Enter the adjacency matrix (separate values by space):")
    for i in range(num_vertices):
        row = list(map(int, input().split()))
        for j in range(num_vertices):
            g.graph[i][j] = row[j]
    return g


def main():
    print("Prim's Algorithm for Minimum Spanning Tree")
    g = get_input()
    g.primMST()


if __name__ == "__main__":
    main()
