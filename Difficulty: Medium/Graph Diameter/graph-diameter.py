from collections import deque
class Solution:
    
    def bfs(self,adj,s):
        n=len(adj)
        visited=[False]*n
        q=deque()
        q.append((s,0))
        visited[s]=True
        maxDist=0
        farNode=s
        while q:
            node,dist=q.popleft()
            if dist>maxDist:
                maxDist=dist
                farNode=node
            for v in adj[node]:
                if visited[v]==False:
                    q.append((v,dist+1))
                    visited[v]=True
        return farNode,maxDist
    
    def diameter(self, V, edges):
        adj=[[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        firstEnd,_=self.bfs(adj,0)
        _,diameter=self.bfs(adj,firstEnd)
        return diameter