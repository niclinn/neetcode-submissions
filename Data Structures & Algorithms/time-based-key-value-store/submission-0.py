class TimeMap:

    def __init__(self):
        self.keyStore = defaultdict(list) # key: list of [value, timestamp] 

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        left, right = 0, len(self.keyStore[key]) - 1
        res = ""
        
        while left <= right: 
            mid = (left + right) // 2
            
            # timestamp is larger than target (timestamp in parameter)
            if self.keyStore[key][mid][1] > timestamp: 
                right = mid - 1

            # timestamp is smaller than target (timestamp in parameter)
            else: 
                res = self.keyStore[key][mid][0]
                left = mid + 1
            
        return res



