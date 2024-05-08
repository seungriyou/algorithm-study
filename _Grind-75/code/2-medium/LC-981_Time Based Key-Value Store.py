# https://leetcode.com/problems/time-based-key-value-store/

from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)  # {key: [(value, timestamp)]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        lst = self.dic[key]

        # dic[key]에 기록된 timestamp 중 최솟값 > 주어진 timestamp 라면 값이 없는 것이다!
        if not lst or lst[0][1] > timestamp:
            return ""

        left, right = 0, len(lst) - 1
        while left <= right:
            mid = (left + right) // 2

            if lst[mid][1] < timestamp:
                left = mid + 1
            elif lst[mid][1] > timestamp:
                right = mid - 1
            else:
                return lst[mid][0]

        return lst[right][0]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
