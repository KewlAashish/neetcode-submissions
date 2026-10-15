class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        possible_ans = ""

        range = self.map[key]
        l = 0 
        r = len(range) -1
        while l <= r:
            mid = (l + r) // 2
            if range[mid][0] <= timestamp:
                possible_ans = range[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return possible_ans