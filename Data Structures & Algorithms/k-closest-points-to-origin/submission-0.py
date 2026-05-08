class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = [[(x ** 2 + y ** 2), x, y] for x, y in points]
        heapq.heapify(dists)

        res = []
        for _ in range(k): 
            dist = heapq.heappop(dists)
            res.append([dist[1], dist[2]])
        
        return res