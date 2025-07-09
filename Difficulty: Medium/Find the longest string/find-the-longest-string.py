class Solution():
    def longestString(self, arr):
        # code here
        class Trie:
            def __init__(self):
                self.root={}
            def insert(self,w):
                node=self.root
                for c in w:
                    if c not in node:
                        node[c]={}
                    node=node[c]
                node['.']={}
            def find(self,w):
                node=self.root
                for c in w:
                    if c not in node:
                        return False
                    node=node[c]
                return '.' in node
        trie=Trie()
        for w in arr:
            trie.insert(w)
        ret=[]
        for w in sorted(arr,key=lambda x:-len(x)):
            if len(w)<len(ret):
                continue
            ok=True
            for l in range(len(w)-1):
                if not trie.find(w[:l+1]):
                    ok=False
                    break
            if not ok:
                continue
            ret=min([ret,list(w)],key=lambda x:(-len(x),x,))
        return ''.join(ret)