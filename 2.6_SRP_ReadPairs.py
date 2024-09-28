import networkx as nx
k = 3
d = 1
array_list = 'ACC|ATA ACT|ATT ATA|TGA ATT|TGA CAC|GAT CCG|TAC CGA|ACT CTG|AGC CTG|TTC GAA|CTT GAT|CTG GAT|CTG TAC|GAT TCT|AAG TGA|GCT TGA|TCT TTC|GAA'
array = array_list.split()

def Graph(array, k):
    graph = {}
    for string in array:
        prefix = string[0:k - 1] + string[k] + string[k + 1 : 2 * k]
        suffix = string[1:k] + string[k] + string[k + 2 :]
        graph[prefix] = [suffix]
    return graph

l = len(Graph(array, k))
G = nx.DiGraph(Graph(array, k))

def EulerPath(G):
    nodes = list(G.nodes())
    for node in nodes:
        if G.in_degree(node) < G.out_degree(node):
            print(node, G.in_degree(node), G.out_degree(node))
            path = list(nx.dfs_edges(G, node))
            break
    string = path[0][0][:k - 1]
    for i in range(0, len(path)):
        string += path[i][1][k - 2]
    for j in range(l - k - d, len(path)):
        string += path[j][1][-1]
    print(string)

EulerPath(G)