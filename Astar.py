# Graph definition (example)
graph = {
    'S': [['A', 1], ['G', 10]],
    'A': [['B', 2], ['C', 1]],
    'B': [['D', 5]],
    'C': [['D', 3], ['G', 4]],
    'D': [['G', 2]],
    'G': []
}

# Heuristic function (example)
hf = {
    'S': 5,
    'A': 3,
    'B': 4,
    'C': 2,
    'D': 6,
    'G': 0
}

opened = ['S', 'A', 'B', 'C', 'D', 'G']
closed = []

def path_cost(lis):
    cost = 0
    prev = lis[0]
    for i in range(0, (len(lis) - 1)):
        for item in graph[lis[i]]:
            if item[0] == lis[i + 1]:
                cost += item[1]
    cost += hf[lis[-1]]
    return cost

def Astar(graph, hf, goal):
    goal_reached = False
    counter = 1
    s = opened.pop(0)
    closed.append(s)
    print(f"iteration {counter}: {opened}, {closed}")
    
    while not goal_reached:
        di = {}
        for item in graph[s]:
            if item[0] not in closed:
                li = closed + [item[0]]
                cost = path_cost(li)
                di[item[0]] = cost

        smallest, cst = '', 9999
        for item in di:
            if di[item] <= cst:
                smallest, cst = item, di[item]

        closed.append(smallest)
        opened.remove(smallest)
        counter += 1
        s = smallest
        print(f"iteration {counter}: {opened}, {closed}")
        
        if smallest == goal:
            goal_reached = True
            break

    return closed

# Running the A* algorithm
path = Astar(graph, hf, 'G')
print("Final path:", " -> ".join(path))
