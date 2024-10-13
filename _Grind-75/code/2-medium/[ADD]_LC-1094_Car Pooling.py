# https://leetcode.com/problems/car-pooling/

from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0] * 1001
        for n, s, e in trips:
            diff[s] += n
            diff[e] -= n

        num = 0
        for d in diff:
            num += d
            if num > capacity:
                return False

        return True
