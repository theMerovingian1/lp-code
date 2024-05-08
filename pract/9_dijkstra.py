class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def printSolution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])

    def minDistance(self, dist, sptSet):
        min_dist = float('inf')
        min_index = -1
        for v in range(self.V):
            if dist[v] < min_dist and not sptSet[v]:
                min_dist = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for _ in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if (self.graph[u][v] > 0 and not sptSet[v] and
                        dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)


def get_input():
    num_vertices = int(input("Enter the number of vertices: "))
    g = Graph(num_vertices)
    print("Enter the adjacency matrix (separate values by space):")
    for i in range(num_vertices):
        g.graph[i] = list(map(int, input().split()))
    return g


def main():
    print("Dijkstra's Algorithm for Single Source Shortest Path")
    g = get_input()
    src = int(input("Enter the source vertex: "))
    g.dijkstra(src)


if __name__ == "__main__":
    main()
