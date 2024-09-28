Adj_dict = dict()
adj_str = '''0: 1
1: 2 3
2: 0
3: 4
4: 1'''

adj_list = adj_str.split("\n")
for item in adj_list:
    keys, *values = item.split(":")
    keys = int(keys.strip())
    values = [int(vals.strip()) for vals in values[0].split()]
    Adj_dict[keys] = values

def find_eulerian_cycle(graph):
    def dfs(vertex):
        while adj_list[vertex]:
            neighbor = adj_list[vertex].pop(0)
            dfs(neighbor)
        cycle.append(vertex)

    adj_list = {vertex: neighbors[:] for vertex, neighbors in graph.items()}  # Make a copy of the graph
    cycle = []

    # Choose any vertex as the starting point
    start_vertex = next(iter(adj_list.keys()))

    dfs(start_vertex)

    return cycle[::-1]

eulerian_cycle = find_eulerian_cycle(Adj_dict)
result = ' '.join(str(item) for item in eulerian_cycle)
print(result)