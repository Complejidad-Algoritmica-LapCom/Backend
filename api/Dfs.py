import json
def dfs(graph:dict, start:str) -> list:
    visited = []
    stack = [start]
    limit = 15
    while stack:
        node = stack.pop()
        if len(visited) == limit:
            break
        if node not in visited:
            visited.append(node)
            vecinos = []
            if node in graph:
                vecinos = list(map(str,graph[node]))
            stack.extend(vecinos)
    response = visited[1:]
    return response

def ApplyDFS(nodoInicial:str, listAdj:{}) -> list:
    return dfs(listAdj, nodoInicial)