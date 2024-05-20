# https://leetcode.com/problems/reorganize-string/

class Solution:
    # ref: https://leetcode.com/problems/reorganize-string/solutions/3947780/100-2-approaches-priority-queue-sort

    def reorganizeString1(self, s: str) -> str:
        """sorting"""

        from collections import Counter

        # create a counter
        cnts = Counter(s)

        # sort chars in most frequent order
        sorted_chars = sorted(cnts.keys(), key=lambda x: -cnts[x])

        # if most frequent char appears more than half of the total length, return ""
        if cnts[sorted_chars[0]] > (len(s) + 1) // 2:
            return ""

        res = ["-"] * len(s)
        i = 0  # first pass: start from 0-index

        for char in sorted_chars:
            for _ in range(cnts[char]):
                if i >= len(s):
                    i = 1  # second pass: start from 1-index

                res[i] = char
                i += 2  # interval = 2

        return "".join(res)

    def reorganizeString2(self, s: str) -> str:
        """max heap #2"""

        import heapq
        from collections import Counter

        # create a counter
        cnts = Counter(s)

        # create a max heap
        pq = [(-cnt, char) for char, cnt in cnts.items()]
        heapq.heapify(pq)  # -- heapify = O(n)

        res = []

        # pq의 원소가 1개 이하로 남을 때까지 연달아 2개 뽑는 동작 반복
        while len(pq) >= 2:
            # 이렇게 하면 char1 != char2
            # 또한, cnt 값 뿐만 아니라 char로도 비교하기 때문에, 이전 문자를 확인할 필요도 X
            cnt1, char1 = heapq.heappop(pq)
            cnt2, char2 = heapq.heappop(pq)

            res.append(char1)
            res.append(char2)

            if cnt1 < -1:
                heapq.heappush(pq, (cnt1 + 1, char1))
            if cnt2 < -1:
                heapq.heappush(pq, (cnt2 + 1, char2))

        # pq에 원소가 1개 남아있다면, 해당 원소의 남은 cnt 값이 1보다 큰 경우라면 불가능하므로 "" 반환
        if pq:
            cnt, char = heapq.heappop(pq)
            if cnt < -1:
                return ""
            res.append(char)

        return "".join(res)

    def reorganizeString(self, s: str) -> str:
        """max heap #1"""

        import heapq
        from collections import Counter

        # create a counter
        cnts = Counter(s)

        # create a max heap
        pq = [(-cnt, char) for char, cnt in cnts.items()]
        heapq.heapify(pq)  # -- heapify = O(n)
        # pq = []
        # for char, cnt in cnts.items():
        #     heapq.heappush(pq, (-cnt, char))    # -- O(nlogn) == sorting

        # ref: https://dev.to/fayomihorace/python-how-simple-string-concatenation-can-kill-your-code-performance-2636
        # res = []
        res = ""

        # 같은 문자끼리는 최소 1칸 떨어지도록 하기 위해 한 cycle을 2칸으로 설정
        cycle = 2

        # most frequent element 부터 하나씩 꺼내기
        while pq:
            # 만약 res의 가장 최근 문자가 이번 cycle에서 pop 될 첫 번째 char과 같다면 종료
            if res and res[-1] == pq[0][1]:
                return ""

            # 한 cycle(= 2칸) 내에서 pop 한 char들에 대해, cnt 값을 업데이트한 tuple을 임시 저장하기 위한 list
            tmp = []

            # cycle 내에서는 동일한 문자 pop 되지 X
            for _ in range(cycle):
                if pq:
                    cnt, char = heapq.heappop(pq)

                    # res.append(char)
                    res += char

                    # cnt 값 업데이트하여 다시 pq에 넣기 위해 임시 list tmp에 넣기
                    if cnt < -1:
                        tmp.append((cnt + 1, char))

            # pq에 cnt 업데이트
            for t in tmp:
                heapq.heappush(pq, t)

        return res
        # return "".join(res)
