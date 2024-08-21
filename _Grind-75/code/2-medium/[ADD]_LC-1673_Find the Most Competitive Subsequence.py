# https://leetcode.com/problems/find-the-most-competitive-subsequence/

from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        """
        길이가 k인 most competitive subsequence(=> lexiographical order)를 만들기 위해서,
        왼쪽부터 살펴보며 non-decreasing monotonic stack을 구성하듯이 접근할 수 있다.
        이때, stack에서 pop 하는 동작은 최대 len(nums) - k 번 가능하다는 점에 유의한다.

        이렇게 구성된 stack의 길이는 k보다 길 수 있는데, more competitive == differ 되는 지점의 수가 작은 것이므로 stack[:k]로 잘라준다!
        """

        can_pop = len(nums) - k
        stack = []

        for num in nums:
            while stack and stack[-1] > num and can_pop:
                stack.pop()
                can_pop -= 1
            stack.append(num)

        return stack[:k]
