class Solution:
    def totalElements(self, arr):
        # Code here
        n = len(arr)
        s = 0
        e = 0
        max_len = 0
        unique = set()

        while e < n:
            unique.add(arr[e])
            if len(unique) <= 2:
                max_len = max(max_len, e - s + 1)
                e += 1
            else:
                # Reset the window
                s += 1
                e = s
                unique.clear()
        
        return max_len

