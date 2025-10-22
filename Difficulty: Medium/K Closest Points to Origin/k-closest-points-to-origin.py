from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x, y = point[0], point[1]
            dis = (x - 0) ** 2 + (y - 0) ** 2  
            heapq.heappush(heap, (dis, point))  
        res = []
        for _ in range(k):
            if heap:
                res.append(heapq.heappop(heap)[1]) 
        return res

