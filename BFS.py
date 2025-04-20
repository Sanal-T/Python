from collections import deque  # <- Add this import

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

def bfs(graph, start):
    visited = set()
    queue = deque([start])  # now deque is properly imported
    key = input('Key: ')

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node, end=' ')
            if node == key:
                break
            visited.add(node)
            queue.extend(graph[node])

print('BFS')
graph = read_graph()
bfs(graph, 'A')
4
