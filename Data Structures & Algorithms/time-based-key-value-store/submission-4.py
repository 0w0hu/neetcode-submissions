class TimeMap:

    def __init__(self):
        self.store = {} # {key: [val:time]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        val = self.store.get(key, [])
        ans = ""
        l, r = 0, len(val)-1
        while l <= r:
            m = (l + r) // 2
            if val[m][1] <= timestamp:
                ans = val[m][0]
                l = m + 1
            else:
                r = m - 1
        return ans
