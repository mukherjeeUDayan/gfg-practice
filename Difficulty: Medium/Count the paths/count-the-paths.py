class Solution:
    def solve(self, adj, curr, dest):
        if curr == dest:
            return 1
            
        if self.cache[curr] != None:
            return self.cache[curr]
        
        cnt = 0
        for v in adj[curr]:
            cnt += self.solve(adj, v, dest)
            
        self.cache[curr] = cnt
        
        return cnt
    
    def countPaths(self, edges, V, src, dest):
        adj = [[] for _ in range(V)]
        
        for u, v in edges:
            adj[u].append(v)
        
        self.cache = [None] * V
            
        return self.solve(adj, src, dest)
        #Code here