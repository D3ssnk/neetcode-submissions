class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pairs = []
        ans = []
        for n in points:
            distance = math.sqrt((n[0]**2) + (n[1]**2)) 
            pairs.append([distance, n])
        
        pairs = sorted(pairs, key= lambda x: x[0])
        for i in range(k):
            ans.append(pairs[i][1])
        return ans
        