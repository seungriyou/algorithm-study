# https://leetcode.com/problems/implement-stack-using-queues/

from collections import deque


class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()  # pop 시에 이용하는 queue
        self._top = None

    def push(self, x: int) -> None:
        self.q1.append(x)
        self._top = x

    def pop(self) -> int:
        while len(self.q1) > 1:
            self._top = self.q1.popleft()
            self.q2.append(self._top)

        res = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return res

    def top(self) -> int:
        return self._top

    def empty(self) -> bool:
        return len(self.q1) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
