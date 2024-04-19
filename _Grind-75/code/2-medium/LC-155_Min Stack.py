# https://leetcode.com/problems/min-stack/

class MinStack:
    """1-stack version"""

    def __init__(self):
        self.stack = []     # [(val, min_val)]

    def push(self, val: int) -> None:
        if not self.stack or self.stack[-1][1] > val:
            self.stack.append((val, val))
        else:
            self.stack.append((val, self.stack[-1][1]))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


class MinStack2:
    """2-stack version"""

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # stack에 append
        self.stack.append(val)
        # min_stack 업데이트 (min_stack[-1] >= val이면 append)
        if not self.min_stack or self.min_stack[-1] >= val:
            self.min_stack.append(val)

    def pop(self) -> None:
        # stack에서 pop
        top = self.stack.pop()
        # min_stack top과 같으면 min_stack도 pop
        if self.min_stack and self.min_stack[-1] == top:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else self.stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


###### review ######
class MinStack:
    """1-stack"""

    def __init__(self):
        self.stack = []  # [(val, min_val)]

    def push(self, val: int) -> None:
        if not self.stack or self.stack[-1][1] > val:
            self.stack.append((val, val))
        else:
            self.stack.append((val, self.stack[-1][1]))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


class MinStack2:
    """2-stack"""

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # stack에 넣기
        self.stack.append(val)

        # min_stack에 현재까지의 최솟값 넣기
        if not self.min_stack or self.min_stack[-1] > val:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        # stack에서 빼기
        self.stack.pop()

        # min_stack에 담긴 최솟값도 빼기
        self.min_stack.pop()

    def top(self) -> int:
        # stack의 top 반환
        return self.stack[-1]

    def getMin(self) -> int:
        # min_stack의 top 반환
        return self.min_stack[-1]
