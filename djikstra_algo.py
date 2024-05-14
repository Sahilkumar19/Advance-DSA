"""
Name : Sahil Kumar
Date : 26/04/2024

Algorithms : Dijkstra (Single Source shortest path algorithm)

I this python script I have implemented the dijkstra algorithm which is a single source shortest path algorithm means using 
this algorithm we find the shortest distance from a source vertex to all the vertex in the graph.

I have given the specifications of the functions written in this script for better understanding about the arguments and return type of the functions.
"""

def calculate_shortest_distances(graph, source):
    """
    Applies Dijkstra's algorithm to find the shortest paths from a source vertex to all other vertices in a weighted graph.
    
    Args:
        graph (dict): A dictionary representing the weighted graph, where keys are vertices and values are dictionaries of neighboring vertices and their weights.
        source (str): The source vertex.
    
    Returns:
        dict: A dictionary with keys as vertices and values as shortest distances from the source vertex to each vertex.
    """
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0
    unvisited = set(graph.keys())
    
    while unvisited:
        current_vertex = min(unvisited, key=lambda x: distances[x])
        unvisited.remove(current_vertex)
        
        for neighbor, weight in graph.get(current_vertex, {}).items():
            if neighbor in unvisited:
                distance = distances[current_vertex] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
    
    return distances

def main():
    """
    written just to call the the above function (calculate_shortest_distances) and print the shortest distance from source to other vertices.
    """
    graph = {
        's': {'a': 2, 'b': 1},
        'a': {'b': -2},
        'b': {}  #adding 'b' as a vertex with no outgoing edges
    }

    source = 's'
    distances = calculate_shortest_distances(graph, source)
    print(f"Shortest distances from {source}:")
    for vertex, distance in distances.items():
        print(f"{vertex}: {distance}")

if __name__ == "__main__":
    main()
