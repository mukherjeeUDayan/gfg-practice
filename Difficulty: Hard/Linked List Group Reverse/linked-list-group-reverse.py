"""
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""

class Solution:
    def reverseKGroup(self, head, k):
        # Code here
        def reverse(sta,sto):
            prv=None
            cur=sta
            while cur!=sto:
                nxt=cur.next
                cur.next=prv
                prv=cur
                cur=nxt
            return prv
        dummy=Node(-1)
        dummy.next=head
        tail=dummy
        sta=head
        sto=sta
        while sto:
            for _ in range(k):
                sto=sto.next
                if not sto:
                    break
            ntail=reverse(sta,sto)
            tail.next=ntail
            tail=sta
            sta.next=sto
            sta=sto
        return dummy.next