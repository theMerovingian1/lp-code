import heapq


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def prim_mst(self):
        visited = [False] * self.V
        min_heap = []
        mst_cost = 0

        # Start with the vertex 0
        heapq.heappush(min_heap, (0, 0))

        while min_heap:
            weight, vertex = heapq.heappop(min_heap)

            if not visited[vertex]:
                mst_cost += weight
                visited[vertex] = True

                for neighbor, neighbor_weight in self.graph[vertex]:
                    if not visited[neighbor]:
                        heapq.heappush(min_heap, (neighbor_weight, neighbor))

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

    mst_cost = g.prim_mst()
    print("Minimum Spanning Tree Cost:", mst_cost)


if __name__ == "__main__":
    main()
