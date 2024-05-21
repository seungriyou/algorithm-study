# https://leetcode.com/problems/distant-barcodes/

from typing import List


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        """sorting (먼저 칸을 만들고 채워나가기)"""
        from collections import Counter

        cnts = Counter(barcodes)  # - O(n)

        sorted_nums = sorted(cnts.keys(), key=lambda x: -cnts[x])  # - O(klogk)

        i = 0
        res = [0] * len(barcodes)

        # - O(n)
        # most frequent number 부터
        for num in sorted_nums:
            # 해당 number의 등장 횟수만큼 2칸씩 건너뛰며 기록
            for _ in range(cnts[num]):
                # 1-pass 완료되면 index 1부터 2-pass 시작
                if i >= len(barcodes):
                    i = 1

                res[i] = num
                i += 2

        return res

    def rearrangeBarcodes1(self, barcodes: List[int]) -> List[int]:
        """max heap (빈 곳에서부터 채워나가기)"""
        import heapq
        from collections import Counter

        cnts = Counter(barcodes)  # - O(n)

        pq = [(-cnt, num) for num, cnt in cnts.items()]  # - O(k)
        heapq.heapify(pq)  # - O(k)

        res = []

        while len(pq) > 1:
            # 연달아 2개 뽑기
            cnt1, num1 = heapq.heappop(pq)  # - O(logk)
            cnt2, num2 = heapq.heappop(pq)

            res.append(num1)
            res.append(num2)

            if cnt1 < -1:
                heapq.heappush(pq, (cnt1 + 1, num1))
            if cnt2 < -1:
                heapq.heappush(pq, (cnt2 + 1, num2))

        # pq에 원소가 남아있다면
        if pq:
            res.append(pq[0][1])

        return res
