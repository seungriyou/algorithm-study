# https://leetcode.com/problems/find-k-th-smallest-pair-distance/

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        """
        enough(distance): 거리가 distance 이하인 pair의 개수가 k개 이상인지 반환하는 함수
            -> 이를 만족하는 smallest distance 구하기

        pair -> 최적화를 위해 sort

        -------------
        TC: O(nlogn)
        SC: O(1)
        """

        nums.sort()
        n = len(nums)

        def enough(distance):
            cnt, i, j = 0, 0, 0

            # slow / fast pointer (i뿐만 아니라 j도 계속해서 증가하기만 한다!!!) ***
            while i < n or j < n:
                while j < n and nums[j] - nums[i] <= distance:
                    j += 1
                cnt += j - i - 1  # count pairs
                i += 1

            return cnt >= k

        lo, hi = 0, nums[-1] - nums[0]

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if enough(mid):
                hi = mid  # look for left
            else:
                lo = mid + 1  # exclude mid

        return lo
