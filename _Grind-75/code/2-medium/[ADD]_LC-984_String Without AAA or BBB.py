# https://leetcode.com/problems/string-without-aaa-or-bbb/

# https://leetcode.com/problems/string-without-aaa-or-bbb/solutions/226740/clean-c-python-solution

class Solution:
    def strWithout3a3b2(self, a: int, b: int) -> str:
        """recur (w/o string concat)"""

        res = []

        def recur(a, b):
            if a == 0:
                res.extend(["b"] * b)
            elif b == 0:
                res.extend(["a"] * a)
            elif a > b:
                res.extend(list("aab"))
                recur(a - 2, b - 1)
            elif a < b:
                res.extend(list("bba"))
                recur(a - 1, b - 2)
            else:
                res.extend(list("ab"))
                recur(a - 1, b - 1)

        recur(a, b)
        # res.reverse()

        return "".join(res)

    def strWithout3a3b(self, a: int, b: int) -> str:
        import heapq

        pq = [(cnt, ch) for cnt, ch in [(-a, "a"), (-b, "b")] if cnt != 0]
        heapq.heapify(pq)

        res = ""

        while pq:
            # 가장 개수가 많은 문자 ch1 pop
            cnt1, ch1 = heapq.heappop(pq)

            # 같은 문자가 연달아서 세 번 나오게 될 경우
            if len(res) > 1 and res[-2] == res[-1] == ch1:
                # if not pq:  #  (constraints: it is guaranteed that `s` exists)
                #     return res

                # 두 번째로 개수가 많은 문자 ch2 pop
                cnt2, ch2 = heapq.heappop(pq)
                res += ch2
                if (new_cnt2 := cnt2 + 1) != 0:
                    heapq.heappush(pq, (new_cnt2, ch2))

                # ch1은 그대로 다시 넣기
                heapq.heappush(pq, (cnt1, ch1))

            # 같은 문자가 연달아서 세 번 나오지 않는 경우, res에 ch1 넣기
            else:
                res += ch1
                if (new_cnt1 := cnt1 + 1) != 0:
                    heapq.heappush(pq, (new_cnt1, ch1))

        return res

    def strWithout3a3b_recur(self, a: int, b: int) -> str:
        """recur"""

        if a == 0:
            return "b" * b
        if b == 0:
            return "a" * a

        if a > b:
            return "aab" + self.strWithout3a3b(a - 2, b - 1)
        elif a < b:
            return "bba" + self.strWithout3a3b(a - 1, b - 2)
        else:
            return "ab" + self.strWithout3a3b(a - 1, b - 1)

    def strWithout3a3b2(self, a: int, b: int) -> str:
        """iter"""

        res = ""

        while a and b:
            if a > b:
                res += "aab"
                a -= 2
                b -= 1
            elif a < b:
                res += "bba"
                a -= 1
                b -= 2
            else:
                res += "ab"
                a -= 1
                b -= 1

        if a:
            res += a * "a"
        if b:
            res += b * "b"

        return res
