import json
def dfs(graph:dict, start:str, limit:int) -> list:
    limite = limit
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if len(visited) == limite:
            break
        if node not in visited:
            visited.append(node)
            vecinos = list(map(str,graph[node]))
            stack.extend(vecinos)
    return visited



listAdj = {}
with open("api\lista-adyacencia-no-ponderada.json", "r") as archivo:
    listAdj = json.load(archivo)

def ApplyDFS(nodoInicial:str, limite:int) -> list:
    return dfs(listAdj, nodoInicial, limite)