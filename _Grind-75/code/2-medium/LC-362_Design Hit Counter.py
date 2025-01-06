# https://leetcode.com/problems/design-hit-counter/

class HitCounter1:

    def __init__(self):
        from collections import deque
        self.q = deque([])

    def hit(self, timestamp: int) -> None:
        self.q.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # timestamp - q[0] < 300 이 될 때까지 q.popleft()
        while self.q and timestamp - self.q[0] >= 300:
            self.q.popleft()
        return len(self.q)


class HitCounter:

    def __init__(self):
        self.hits = [(0, 0)] * 300  # (timestamp, hit cnt)

    def hit(self, timestamp: int) -> None:
        i = (timestamp - 1) % 300  # circular
        t, c = self.hits[i]

        if timestamp - t < 300:
            self.hits[i] = (timestamp, c + 1)  # 해당 인덱스의 timestamp가 300초 이내라면 ++ (monotonically increasing)
        else:
            self.hits[i] = (timestamp, 1)  # 300초 이내가 아니라면 0으로 초기화 후 ++

    def getHits(self, timestamp: int) -> int:
        cnt = 0
        for t, c in self.hits:
            if timestamp - t < 300:
                cnt += c
        return cnt

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
