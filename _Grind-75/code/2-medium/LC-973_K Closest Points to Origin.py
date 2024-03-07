# https://leetcode.com/problems/k-closest-points-to-origin/

from typing import List


class Solution:
    def kClosest_heap(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Heap: O(nlogk)"""

        import heapq

        heap = []
        for px, py in points:
            # 거리 기준으로 최대 힙
            heapq.heappush(heap, (-(px * px + py * py), px, py))

            # heap의 크기는 최대 k로 유지
            if len(heap) > k:
                heapq.heappop(heap)

        return [point for _, *point in heap]

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Sorting: O(nlogn)"""

        def get_powered_distance(point):
            x, y = point
            return x * x + y * y

        return sorted(points, key=lambda p: get_powered_distance(p))[:k]
