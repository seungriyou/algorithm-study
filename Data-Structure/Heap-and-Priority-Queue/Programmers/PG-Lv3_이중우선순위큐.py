# https://school.programmers.co.kr/learn/courses/30/lessons/42628
import heapq

# list.remove()가 정말 최선인가...? (O(N)이다!!)

def solution(operations):
    asc = []
    desc = []

    for operation in operations:
        op, num = operation.split()
        num = int(num)

        if op == "I":
            heapq.heappush(asc, num)
            heapq.heappush(desc, -num)

        elif asc and desc:
            if num == 1:
                asc.remove(-heapq.heappop(desc))

            elif num == -1:
                desc.remove(-heapq.heappop(asc))

    return [-desc[0], asc[0]] if asc and desc else [0, 0]

operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))     # should print [333, -45]
