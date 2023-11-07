import json
def dfs(graph:dict, start:str) -> list:
    limite = 10
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if len(visited) == limite:
            break
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    return visited

listAdj = {}
nodoInicial = "ASUS ExpertBook B1 B1502CBA-EJ0436X Intel Core i5-1235U/8GB/512GB SSD/15.6\""
with open("lista-adyacencia-no-ponderada.json", "r") as archivo:
    listAdj = json.load(archivo)

with open("Resultadosdfs.json", "w") as archivo:
    json.dump(dfs(listAdj, nodoInicial), archivo)