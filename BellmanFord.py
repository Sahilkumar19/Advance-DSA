class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight
def bellman_ford(edges, V, src):
    distance = [float('inf')] * V
    distance[src] = 0

    for _ in range(V - 1):
        for edge in edges:
            if distance[edge.src] != float('inf') and distance[edge.src] + edge.weight < distance[edge.dest]:
                distance[edge.dest] = distance[edge.src] + edge.weight

    for edge in edges:
        if distance[edge.src] != float('inf') and distance[edge.src] + edge.weight < distance[edge.dest]:
            print("Graph contains negative weight cycle")
            return

    for i in range(V):
        print(f"Distance from vertex {src} to vertex {i} is {distance[i]}")

V = 5  
edges = []
edges.append(Edge(0, 1, -1))
edges.append(Edge(0, 2, 4))
edges.append(Edge(1, 2, 3))
edges.append(Edge(1, 3, 2))
edges.append(Edge(1, 4, 2))
edges.append(Edge(3, 2, 5))
# edges.append(Edge(3, 1, 1))
edges.append(Edge(4, 3, -3))

bellman_ford(edges, V, 0)