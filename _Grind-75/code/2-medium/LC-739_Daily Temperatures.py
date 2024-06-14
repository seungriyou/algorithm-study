# https://leetcode.com/problems/daily-temperatures/

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        monotonic stack

        ex) temperatures = [73,74,75,71,69,72,76,73]

        stack           현재 보고있는 값과 그 다음 값
        -------------- -------------------------
        (73)            73  <   74
        0               0       1

        (74)            74  <   75
        1               1       2

        (75)            75  >   71
        2               2       3

        (75  71)        71  >   69
        2   3           3       4

        (75  71  69)    69  <   72
        2   3   4       4       5
        => 72가 들어갈 수 있도록, top에서부터 2개 pop

        (75  72)        76  >   73
        2   5           6       7
        ...
        """

        # stack: temperatures[i]가 감소하는 순서대로 들어가도록 함
        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)

        return res
