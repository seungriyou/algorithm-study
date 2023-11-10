# https://www.acmicpc.net/problem/15659
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_value = -int(1e9)
min_value = int(1e9)

# 연산자 우선순위 고려 -> stack을 사용한다!
stack = [nums[0]]

def backtrack(idx, add, sub, mul, div):
    global min_value, max_value

    # base condition
    if idx == N:
        result = sum(stack)
        min_value = min(min_value, result)
        max_value = max(max_value, result)

    # recur
    """
    - add & sub: stack에 곧바로 append (단, sub의 경우, negative로 변환)
    - mul & div: stack의 top을 pop 한 후, 그 값과 현재 값을 연산하여 stack에 append
                (단, backtrack 후 stack의 top을 다시 pop 했던 값으로 바꿔줘야 함)
    => 이렇게 하면 base condition에서 stack에 들어있는 값을 단순히 sum 하여 구할 수 있다!
    """
    if add > 0:
        stack.append(nums[idx])
        backtrack(idx + 1, add - 1, sub, mul, div)
        stack.pop()
    if sub > 0:
        stack.append(-nums[idx])
        backtrack(idx + 1, add, sub - 1, mul, div)
        stack.pop()
    if mul > 0:
        prev = stack.pop()
        stack.append(prev * nums[idx])
        backtrack(idx + 1, add, sub, mul - 1, div)
        stack[-1] = prev
    if div > 0:
        prev = stack.pop()
        stack.append(int(prev / nums[idx]))
        backtrack(idx + 1, add, sub, mul, div - 1)
        stack[-1] = prev

backtrack(1, add, sub, mul, div)

print(max_value)
print(min_value)
