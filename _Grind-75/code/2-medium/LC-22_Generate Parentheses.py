# https://leetcode.com/problems/generate-parentheses/

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        tmp = []

        def dfs(left, right):
            """
            left: 사용 가능한 ( 개수
            right: 사용 가능한 ) 개수

            => 구성할 때마다 사용한 ) 개수 <= ( 개수 여야 한다!
            """
            # base condition
            if not right:
                res.append("".join(tmp))
                return

            # recur
            if left:
                tmp.append("(")
                dfs(left - 1, right)
                tmp.pop()
            if right > left:
                tmp.append(")")
                dfs(left, right - 1)
                tmp.pop()

        dfs(n, n)

        return res
