# https://leetcode.com/problems/find-k-closest-elements/

from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        sorted array -> binary search

        길이 k의 subarray arr[i:i + k]의 모든 원소를 살펴볼 필요가 없다.
        길이 k인 범위의 lower bound를 찾기 위해 binary search를 수행하며, arr[mid]와 arr[mid + k]만 가지고 비교하면 된다.
        (lo와 hi 사이의 값들은 lower bound의 후보가 된다)

        [ four cases ]
        <1> ---x---arr[mid]-----arr[mid+k]---- => left
        <2> --arr[mid]--x-------arr[mid+k]---- => left
        <3> --arr[mid]-------x--arr[mid+k]---- => right
        <4> --arr[mid]------arr[mid+k]---x---- => right

        위와 같은 네 가지 케이스를 모두 커버하면서 arr[mid]와 arr[mid + k] 중에 x에 더 가까운 값을 찾기 위해 x - arr[mid]와 arr[mid + k] - x를 비교한다.

        - 만약 arr[mid]가 x에 더 가깝다면, arr[mid + k]는 길이 k 안에 포함될 수 없다.
          => 따라서 arr[mid + 1], arr[mid + 2], ...를 후보에서 제외한다.
          => left를 살펴보는 경우에 해당하므로, |a - x| == |b - x| and a < b 조건을 만족시키기 위해 다음과 같이 로직을 작성할 수 있다.
          => if x - arr[mid] <= arr[mid + k] - x: hi = mid
        - 만약 arr[mid + k]가 x에 더 가깝다면, arr[mid]는 길이 k 안에 포함될 수 없다.
          => 따라서 ..., arr[mid - 1], arr[mid]를 후보에서 제외한다.
          => right를 살펴보는 경우에 해당한다.
          => if x - arr[mid] > arr[mid + k] - x: lo = mid + 1
        """

        # candidates of lower bound of length k subarray
        lo, hi = 0, len(arr) - k

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if x - arr[mid] > arr[mid + k] - x:
                lo = mid + 1
            else:
                hi = mid

        return arr[lo:lo + k]
