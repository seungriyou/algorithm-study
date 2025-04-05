# https://leetcode.com/problems/find-the-duplicate-number/

from typing import List

class Solution:
    def findDuplicate1(self, nums: List[int]) -> int:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(1)

        [Approach]
            nums 내 원소의 범위를 보면 각 원소를 index로 사용할 수 있다는 것을 알 수 있다.
            또한 duplicated number란 cycle을 의미하는 것이므로, linked-list의 cycle detection에 사용할 수 있는 <Floyd's 알고리즘>을 적용할 수 있다.
            (ref: https://seungriyou.github.io/posts/floyds-cycle-detection/)
            따라서 다음과 같이 slow & fast pointer를 이동시킬 수 있다.
            1. slow와 fast가 만날 때까지, slow는 한 칸씩, fast는 두 칸씩 진행한다.
               -> slow와 fast가 만났다면 cycle이 존재하는 것!
            2. slow와 fast가 만나면 slow를 다시 초기 위치로 이동시키고, slow와 fast 모두 한 칸씩 진행한다.
               => slow와 fast가 만나는 지점이 cycle의 시작점, 즉 duplicated number이다.
        """

        slow = fast = 0

        while True:
            # 1. slow와 fast가 만날 때까지 진행
            slow = nums[slow]  # -- 1 칸씩
            fast = nums[nums[fast]]  # -- 2 칸씩

            # 2. slow와 fast가 만났다면, slow를 다시 맨 앞으로 옮기고
            #    slow와 fast가 만날 때까지 1 칸씩 진행
            if slow == fast:
                slow = 0
                while slow != fast:
                    slow = nums[slow]  # -- 1 칸씩
                    fast = nums[fast]  # -- 1 칸씩

                return slow

    def findDuplicate(self, nums: List[int]) -> int:
        """
        [Complexity]
            - TC: O(nlogn)
            - SC: O(1)

        [Approach]
            원소의 범위가 [1, n]이므로, 비둘기집의 원리를 이용해 다음의 값을 mid로 트래킹하는 binary search로 풀 수 있다.
                (1) 현재 보고 있는 원소 값
                (2) (1)값의 이하 값을 원소들의 개수
        """

        def get_lte(val):
            return sum(num <= val for num in nums)

        n = len(nums)
        lo, hi = 1, n - 1  # -- 원소의 범위

        while lo < hi:  # -- O(logn)
            mid = lo + (hi - lo) // 2

            # 현재 보고 있는 원소 값 이하인 값들을 가지는 원소들의 개수 구하기
            cnt = get_lte(mid)  # -- O(n)

            # range가 [1, n]이므로 cnt > mid인 경우에 비둘기집 원리 적용 가능
            if cnt > mid:
                hi = mid  # 비둘기집의 원리에 의해, duplicated number는 [lo, mid]에 존재
            else:
                lo = mid + 1  # 아니라면 duplicated number는 [mid + 1, hi]에 존재

        return lo
