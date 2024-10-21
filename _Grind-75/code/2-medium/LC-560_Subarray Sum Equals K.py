# https://leetcode.com/problems/subarray-sum-equals-k/

from typing import List


class Solution:
    def subarraySum0(self, nums: List[int], k: int) -> int:
        """O(n^2) -> 당연히 TLE"""

        res = 0
        n = len(nums)

        for i in range(n):
            _sum = 0
            for j in range(i, n):
                _sum += nums[j]
                if _sum == k:
                    res += 1

        return res

    def subarraySum1(self, nums: List[int], k: int) -> int:
        """
        subarray = a contiguous non-empty sequence
        - prefix sum 활용
            ps => nums[i] ~ num[j] 합 = ps[j + 1] - ps[i]
        - hash table: sum이 k가 되기 위해 필요한 ps 값을 O(1)에 찾기 위함
            idx_cnts => {ps 값: prefix sum이 해당 값인 idx의 개수}

        subarray를 확인하므로 ps를 구성함과 동시에 확인할 수 있음
            ps[j + 1] - ps[i] = k
            => ps[i] = ps[j + 1] - k = ps[-1] - k
        """

        from collections import defaultdict

        idx_cnts = defaultdict(int)  # {ps 값: prefix sum이 해당 값인 idx의 개수}
        ps, res = [0], 0  # ps = prefix sum

        for n in nums:
            # prefix sum 기록
            ps.append(ps[-1] + n)

            # [**주의**] ps 값이 k인 경우에는 1 추가
            if ps[-1] == k:
                res += 1

            # ps[i] = ps[j + 1] - k = ps[-1] - k 에 해당하는 idx_cnts 값을 res에 더하여 count
            res += idx_cnts[ps[-1] - k]

            # 현재 ps 값의 개수 증가
            idx_cnts[ps[-1]] += 1

        return res

    def subarraySum2(self, nums: List[int], k: int) -> int:
        """
        prefix sum -> 어차피 ps[-1]만 보는데 O(n) space가 필요하지 않음!
        """

        from collections import defaultdict

        idx_cnts = defaultdict(int)  # {ps 값: prefix sum이 해당 값인 idx의 개수}
        ps = res = 0  # ps = last prefix sum

        for n in nums:
            # prefix sum 기록
            ps += n

            # [**주의**] ps 값이 k인 경우에는 1 추가
            if ps == k:
                res += 1

            # ps[i] = ps[j + 1] - k = ps[-1] - k 에 해당하는 idx_cnts 값을 res에 더하여 count
            res += idx_cnts[ps - k]

            # 현재 ps 값의 개수 증가
            idx_cnts[ps] += 1

        return res

    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        prefix sum -> O(1) space & ps == k인 경우 미리 handling
        & defaultdict 사용하지 않음!
        """

        idx_cnts = {0: 1}  # {ps 값: prefix sum이 해당 값인 idx의 개수} w/ corner case handling
        ps = res = 0  # ps = last prefix sum

        for n in nums:
            # prefix sum 기록
            ps += n

            # ps[i] = ps[j + 1] - k = ps[-1] - k 에 해당하는 idx_cnts 값을 res에 더하여 count
            if ps - k in idx_cnts:
                res += idx_cnts[ps - k]

            # 현재 ps 값의 개수 증가
            idx_cnts[ps] = idx_cnts.get(ps, 0) + 1

        return res
