# https://www.acmicpc.net/problem/1406
import sys
input = sys.stdin.readline

string = list(input().rstrip())
M = int(input())

# ===== TLE =====
"""
# 커서 위치
c = len(string)

for _ in range(M):
    command = input().rstrip()
    if command == "L":
        # 커서를 왼쪽으로 한 칸 옮기기 (맨 앞이면 무시)
        if c > 0:
            c -= 1
    elif command == "D":
        # 커서를 오른쪽으로 한 칸 옮기기 (맨 뒤면 무시)
        if c < len(string):
            c += 1
    elif command == "B":
        # 커서 왼쪽의 문자 삭제 (맨 앞이면 무시) / 커서 위치 -1
        if c > 0:
            # string = string[:c - 1] + string[c:]
            string.remove(string[c - 1])
            c -= 1
    else:
        # 커서 왼쪽에 문자 추가 / 커서 위치 +1
        new_char = command[-1]
        # string = string[:c] + new_char + string[c:]
        string.insert(c, new_char)
        c += 1

print("".join(string))
"""

# ===== w/ stack =====
stack1 = [*string]  # 커서 왼쪽
stack2 = []         # 커서 오른쪽

for _ in range(M):
    command = input().rstrip()
    if command == "L":
        # 커서를 왼쪽으로 한 칸 옮기기 (맨 앞이면 무시)
        if stack1:
            stack2.append(stack1.pop())
    elif command == "D":
        # 커서를 오른쪽으로 한 칸 옮기기 (맨 뒤면 무시)
        if stack2:
            stack1.append(stack2.pop())
    elif command == "B":
        # 커서 왼쪽의 문자 삭제 (맨 앞이면 무시) / 커서 위치 -1
        if stack1:
            stack1.pop()
    else:
        # 커서 왼쪽에 문자 추가 / 커서 위치 +1
        stack1.append(command[-1])

stack2.reverse()
print("".join(stack1)+"".join(stack2))
