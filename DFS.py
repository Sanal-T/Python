def read_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))
    print("First node should be A")
    for _ in range(num_nodes):
        node = input("Enter the node: ")
        neighbors = input(f"Enter the neighbors of {node} separated by space: ").split()
        graph[node] = neighbors
    print(graph)
    return graph

def dfs(graph, node, visited, key):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        if node == key:
            return True  # stop DFS if key is found
        for neighbor in graph.get(node, []):
            if dfs(graph, neighbor, visited, key):
                return True
    return False

print('DFS')
graph = read_graph()
start = 'A'
key = input('Key: ')
visited = set()
dfs(graph, start, visited, key)
