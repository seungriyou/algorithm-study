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


###### review ######
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        quick select
        - TC: O(n)
        - SC: O(1)
        """
        from random import randint

        def get_distance(point):
            x, y = point
            return x * x + y * y

        def partition(left, right):
            p = left

            # pivot를 random하게 선택하고, right와 swap (이렇게 해야 시간 오래 안 걸림..?)
            random = randint(left, right)
            points[random], points[right] = points[right], points[random]

            # pivot의 distance 구하기
            pivot_distance = get_distance(points[right])

            for i in range(left, right):
                # 현재 보고 있는 point의 distance가 pivot distance 이하이면 p와 swap
                if get_distance(points[i]) <= pivot_distance:
                    points[i], points[p] = points[p], points[i]
                    p += 1

            # 마지막으로 p와 right swap
            # - p를 기준으로, points[p]의 distance보다 작은 distance인 point는 왼쪽에,
            # - points[p]의 distance보다 큰 distance인 point은 오른쪽에 위치
            points[p], points[right] = points[right], points[p]

            return p

        # iterative 형식
        left, right, pivot_index = 0, len(points) - 1, len(points)
        while pivot_index != k:
            pivot_index = partition(left, right)
            if pivot_index < k:
                left = pivot_index + 1
            else:
                right = pivot_index - 1

        return points[:k]

    def kClosest_heapq(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        heapq
        - TC: O(nlogk)
        - SC: O(k)
        """
        import heapq

        def get_distance(point):
            x, y = point
            return x * x + y * y

        q = []
        for point in points:
            heapq.heappush(q, (-get_distance(point), point))

            if len(q) > k:
                heapq.heappop(q)

        return [point for _, point in q]
