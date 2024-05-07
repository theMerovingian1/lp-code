import heapq


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def dijkstra_mst(self, src):
        # Priority queue to store (distance, vertex) pairs
        min_heap = [(0, src)]
        mst_cost = 0
        visited = set()

        while min_heap:
            dist, vertex = heapq.heappop(min_heap)

            if vertex not in visited:
                mst_cost += dist
                visited.add(vertex)

                for neighbor, weight in self.graph[vertex]:
                    if neighbor not in visited:
                        heapq.heappush(min_heap, (weight, neighbor))

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

    src_vertex = int(input("Enter the source vertex: "))

    mst_cost = g.dijkstra_mst(src_vertex)
    print("Minimum Spanning Tree Cost:", mst_cost)


if __name__ == "__main__":
    main()
