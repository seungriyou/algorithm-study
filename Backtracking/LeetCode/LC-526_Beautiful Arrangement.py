# [LC] 526 - Beautiful Arrangement
# https://leetcode.com/problems/beautiful-arrangement/

class Solution:
    def countArrangement(self, n: int) -> int:
        nums = list(range(1, n + 1))
        cnt = 0

        def backtrack(elements, idx):
            nonlocal cnt

            # base condition
            if idx == n + 1:
                cnt += 1
                # return

            # recur
            for e in elements:
                # beautiful arrangement condition 만족 시에만 dfs
                if e % idx == 0 or idx % e == 0:
                    next_elements = elements[:]
                    next_elements.remove(e)
                    backtrack(next_elements, idx + 1)

        backtrack(nums, 1)

        return cnt


class Solution2:
    def countArrangement(self, n: int) -> int:
        nums = set(range(1, n + 1))
        seen = set()
        cnt = 0

        def backtrack(idx):
            nonlocal cnt

            # base condition
            if idx > n:
                cnt += 1

            # recur
            for e in nums - seen:
                # beautiful arrangement condition 만족 시에만 dfs
                if e % idx == 0 or idx % e == 0:
                    seen.add(e)
                    backtrack(idx + 1)
                    seen.remove(e)

        backtrack(1)

        return cnt


sol1 = Solution()
sol2 = Solution2()
n = 2
print(sol1.countArrangement(n))
print(sol2.countArrangement(n))
