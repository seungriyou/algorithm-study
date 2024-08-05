# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        """
        - 모두 확인하는 것은 O(mn)
        - binary search 적용
            - lo: 1
            - hi: m * n
        - enough(num): num 이하인 값이 k개 이상 있는지 여부 반환
            -> 이를 만족하는 minimum num 값을 찾아야 함

        --------------
        어떻게 lo가 table에 존재하는 것을 보장할 수 있나?
        (ref: https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/solutions/1580357/c-python-clean-simple-solution-w-detailed-explanation-binary-search-with-proof)
            lo와 hi이 하나의 숫자로 수렴하게 되며, 그 값이 enough를 만족시키는(= num 이하인 값의 개수가 k개 이상) 가장 작은 값이므로
            해당 숫자는 table에 존재하게 된다.

        --------------
        TC: O(m * log(m * n))
            - [1, m * n]에서 binary search
            - binary search의 각 iteration -> O(m)
        SC: O(1)
        """

        def enough(num):
            """
            cnt = 0
            # row 별로 확인
            for r in range(1, m + 1):
                # 현재 row의 모든 원소가 num 이하인 값이라면 최대 개수인 n(= row 내 모든 원소 개수),
                # 현재 row의 원소 중 일부가 num 이하인 값이라면 num // r 까지만!
                le = min(n, num // r)

                # le == 0이라면 early stop
                if le == 0:
                    break

                # 현재 row에서 찾은 num 이하인 값 개수 업데이트
                cnt += le

            return cnt >= k
            """
            # simpler
            return sum(min(n, num // r) for r in range(1, m + 1)) >= k

        lo, hi = 1, m * n

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if enough(mid):
                hi = mid  # look for left
            else:
                lo = mid + 1  # exclude mid

        return lo
