class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def is_safe(self, v, pos, path):
        # Check if this vertex is adjacent to the previous vertex
        if self.graph[path[pos - 1]][v] == 0:
            return False
        
        # Check if the vertex has been visited already
        if v in path:
            return False

        return True

    def hamiltonian_circuit_util(self, path, pos):
        if pos == self.vertices:
            # Check if there's an edge from the last vertex to the first vertex
            if self.graph[path[pos - 1]][path[0]] == 1:
                return True
            else:
                return False

        for v in range(1, self.vertices):
            if self.is_safe(v, pos, path):
                path[pos] = v
                if self.hamiltonian_circuit_util(path, pos + 1):
                    return True
                # Backtrack if a Hamiltonian circuit is not found with this vertex
                path[pos] = -1

        return False

    def hamiltonian_circuit(self):
        path = [-1] * self.vertices
        path[0] = 0  # Start from the first vertex

        if not self.hamiltonian_circuit_util(path, 1):
            print("No Hamiltonian circuit exists")
            return False

        print("Hamiltonian circuit found:")
        for vertex in path:
            print(vertex, end=" ")
        print(path[0])  # Complete the cycle
        return True

# Example usage
g = Graph(5)
g.graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]
g.hamiltonian_circuit()
