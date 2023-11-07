import json
def dijkstra(Grafo, salida):
    dist, prev = {}, {}
    result = []

    for vertice in Grafo:
        dist[vertice] = float("inf")
        prev[vertice] = None
    dist[salida] = 0

    Q = [vertice for vertice in Grafo]

    while Q:
        u = min(Q, key=dist.get)
        Q.remove(u)
        result.append(u)

        for vecino in Grafo[u]:
            if vecino in Q and dist[vecino] > dist[u] + Grafo[u][vecino]:
                dist[vecino] = dist[u] + Grafo[u][vecino]
                prev[vecino] = u

    return result, dist, prev

with open("lista-adyacencia.json", "r") as archivo:
    grafo = json.load(archivo)
    
nodoInicio = "PcCom Revolt One 3070 Intel Core i7-11800H/16GB/1TB SSD/RTX 3070/17.3\""

s, distancia, previos = dijkstra(grafo, nodoInicio)
print(f"{s=}")
print(f"{distancia=}")
print(f"{previos=}")