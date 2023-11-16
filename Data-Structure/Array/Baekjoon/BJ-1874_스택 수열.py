# https://www.acmicpc.net/problem/1874
import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
curr = 0    # nums의 원소 중 현재 비교 중인 원소를 가리키는 index
i = 1       # stack에 넣고 빼려는 숫자 (1~n 까지의 수로 오름차순)
stack = []  # 숫자를 넣고 빼려는 stack
result = [] # result를 저장

while i < N + 1 and curr < N:
    if stack and stack[-1] == nums[curr]:
        stack.pop()
        result.append("-")
        curr += 1
        continue
    stack.append(i)
    result.append("+")
    i += 1

"""
stack에 아직 pop 되지 않은 원소가 남아있다면,
stack을 뒤집은 것과 아직 보지 못한 nums의 부분리스트를 비교하면 된다.
- 같으면 stack에 남아있는 모든 원소를 pop 하면 nums를 만들 수 있는 것이고,
- 다르면 stack에 남아있는 원소로 nums를 완성할 수 없는 것이다.
"""
stack.reverse()
if nums[curr:] == stack:
    for r in result:
        print(r)
    for _ in range(len(stack)):
        print("-")
else:
    print("NO")
