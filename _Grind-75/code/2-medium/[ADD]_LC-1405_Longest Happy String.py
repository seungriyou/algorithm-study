# https://leetcode.com/problems/longest-happy-string/

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        import heapq

        pq = [(cnt, ch) for cnt, ch in [(-a, "a"), (-b, "b"), (-c, "c")] if cnt != 0]
        heapq.heapify(pq)

        res = ""

        while pq:
            # limit이 가장 높은 char ch1 pop
            cnt1, ch1 = heapq.heappop(pq)

            # ch1이 최근 res에 추가된 두 개의 문자와 동일하다면, 두 번째로 limit이 높은 char ch2 pop
            if len(res) > 1 and res[-2] == res[-1] == ch1:
                # pq에 남은 문자가 없다면 종료
                if not pq:
                    return res

                # ch2 res에 추가 & 관련 값 업데이트
                cnt2, ch2 = heapq.heappop(pq)
                res += ch2
                if (new_cnt2 := cnt2 + 1) != 0:
                    heapq.heappush(pq, (new_cnt2, ch2))

                # ch1은 다시 그대로 넣기
                heapq.heappush(pq, (cnt1, ch1))

            # ch1을 res에 추가할 수 있다면, ch1 res에 추가 & 관련 값 업데이트
            else:
                res += ch1
                if (new_cnt1 := cnt1 + 1) != 0:
                    heapq.heappush(pq, (new_cnt1, ch1))

        return res
    