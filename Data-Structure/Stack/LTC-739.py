# [LTC] 739 - Daily Temperatures

from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    answer = [0] * len(temperatures)
    stack = []  # index
    for i, cur in enumerate(temperatures):
        # 현재 온도가 스택 값보다 높다면 정답 처리
        while stack and cur > temperatures[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)

    return answer

temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures((temperatures)))
