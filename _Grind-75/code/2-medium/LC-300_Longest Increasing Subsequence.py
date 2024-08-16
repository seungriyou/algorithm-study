# https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        greedy + binary search (오..) (TC: O(n log(n)))
        (ref: https://leetcode.com/problems/longest-increasing-subsequence/solutions/1326308/c-python-dp-binary-search-bit-segment-tree-solutions-picture-explain-o-nlogn)
            - 앞에서부터 LIS를 모은다.
            - 현재 원소 num이 LIS의 마지막 원소보다 크지 않다면, 현재 원소 num을 LIS에 덮어쓴다.
                - LIS에 덮어쓸 위치를 구하려면, LIS에서 num 이상인 값 중에서 가장 작은 값의 위치를 찾으면 된다.
                - LIS는 increasing 순서로 구성되어 있으므로 binary search를 사용할 수 있다.
            - 이렇게 구성한 LIS는 가장 긴 길이를 가지는 LIS이다.
        """

        def find_left(lis, num):
            lo, hi = 0, len(lis) - 1

            while lo < hi:
                mid = lo + (hi - lo) // 2
                if lis[mid] < num:
                    lo = mid + 1
                else:
                    hi = mid

            return lo

        lis = []
        for num in nums:
            # (1) lis가 비어있거나 (2) lis의 마지막 값보다 현재 원소가 큰 경우에는 append
            if not lis or lis[-1] < num:
                lis.append(num)
            # 아니라면 lis에서 num이 들어갈 위치(= num보다 크거나 같은 첫번째 원소) 구하고 덮어쓰기
            else:
                idx = find_left(lis, num)
                lis[idx] = num

        return len(lis)

    def lengthOfLIS1(self, nums: List[int]) -> int:
        """
        DP (TC: O(n^2))
            - i 번째 원소를 볼 때, 0 ~ i - 1 번째의 값을 보면서, 가장 큰 값에 + 1
            - dp[i] = nums[i]가 포함되는 LIS의 길이
        """
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1

        return max(dp)
