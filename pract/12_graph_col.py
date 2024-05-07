class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def is_safe(self, vertex, color, color_assignment):
        for i in range(self.V):
            if self.graph[vertex][i] == 1 and color_assignment[i] == color:
                return False
        return True

    def graph_coloring_util(self, colors, vertex, color_assignment):
        if vertex == self.V:
            return True

        for color in colors:
            if self.is_safe(vertex, color, color_assignment):
                color_assignment[vertex] = color
                if self.graph_coloring_util(colors, vertex + 1, color_assignment):
                    return True
                color_assignment[vertex] = -1

        return False

    def graph_coloring(self, colors):
        color_assignment = [-1] * self.V
        if not self.graph_coloring_util(colors, 0, color_assignment):
            return None
        return max(color_assignment) + 1


def main():
    num_vertices = int(input("Enter the number of vertices: "))
    num_edges = int(input("Enter the number of edges: "))

    g = Graph(num_vertices)

    print("Enter edges (vertex pairs):")
    for _ in range(num_edges):
        u, v = map(int, input().split())
        g.add_edge(u, v)

    # Determine the maximum degree of the graph
    max_degree = max(sum(g.graph[i]) for i in range(num_vertices))

    # The minimum number of colors needed will be at least the maximum degree + 1
    colors = [i for i in range(max_degree + 1)]

    min_colors = g.graph_coloring(colors)
    if min_colors is not None:
        print("Minimum number of colors needed:", min_colors)
    else:
        print("No feasible solution exists.")


if __name__ == "__main__":
    main()
