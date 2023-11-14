import sys

def dijkstra(graph, start, end):
    # Inicializar distancias y nodos visitados
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = {}
    
    while distances:
        # Obtener el nodo con la distancia mínima
        current_node = min(distances, key=distances.get)
        
        # Si el nodo actual es el nodo final, hemos encontrado el camino más corto
        if current_node == end:
            path = []
            while current_node in visited:
                path.insert(0, current_node)
                current_node = visited[current_node]
            path.insert(0, start)
            return path, distances[end]
    

        # Actualizar las distancias a los nodos vecinos
        for neighbor, weight in graph[current_node]:
            if neighbor in visited:
                continue
            new_distance = distances[current_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                visited[neighbor] = current_node
        
        del distances[current_node]
    
    return [], float('inf')

# Ejemplo de uso
graph = {
    'A': [{'B': 2}, {'C': 5}],
    'B': [{'C': 1}, {'D': 7}],
    'C': [{'D': 3}],
    'D': []
}
start_node = 'A'
end_node = 'D'

shortest_path, shortest_distance = dijkstra(graph, start_node, end_node)

if shortest_path:
    print(f"El camino más corto desde {start_node} a {end_node} es: {shortest_path}")
    print(f"La distancia total es: {shortest_distance}")
else:
    print(f"No se encontró un camino desde {start_node} a {end_node}")
