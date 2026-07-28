import defaultdict
"""
A server network is represented as a tree of g_nodes servers indexed from 1 to g_nodes and g_nodes -1 
edges where the ith edges connect the servers g_from[i] to g_to[i]. The transfer tume between any two 
connected servers is 1 unit. Given the graph g, find the max time taken 
to transfer the data between any two servers in the system. 
"""

#3 nodes, [1,2] to [2,3]
#input: g_nodes, g_from, g_to
#output: int 

#5, [1,2,3,4], [2,3,4,5]
# this is a tree (type of graph)
# longest path in tree -> diameter

def server_network(g_nodes, g_from, g_to):
    #make adj list
    # run dfs on every node and count edges /run dfs on the starting node and count the edges

    d = defaultdict()
    for i in range(len(g_from)):
        d[g_from[i]].append(g_to[i])
    
    visited = set()
    
    def dfs(node, count):
        m = 0 
        visited.add(node)
        node = None
        
        for nei in d[node]:
            if nei not in visited:
                if count+1 > m:
                    m = count+1
                    node = nei
                dfs(nei, count+1)
        
        return count

    return dfs(g_from[0], 0)




