# https://leetcode.com/problems/3sum/

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations

        result = set()

        # p: positive, z: zero, n: negative
        p, z, n = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)

        # p와 n은 set으로도 가지고 있기 (O(1) lookup table)
        p_set, n_set = set(p), set(n)

        # (1) 0이 한 개 이상 존재한다면, 합이 0인 p와 n 원소의 쌍을 찾기
        if z:
            for pn in p_set:
                if -pn in n_set:
                    result.add((-pn, 0, pn))

        # (2) 0이 세 개 이상 존재한다면, 결과에 추가
        if len(z) > 2:
            result.add((0, 0, 0))

        # (3) p 원소 2개 & n 원소 1개의 합이 0인 경우
        for p1, p2 in combinations(p, 2):
            if (nn := -(p1 + p2)) in n_set:
                result.add(tuple(sorted([nn, p1, p2])))

        # (4) p 원소 1개 & n 원소 2개의 합이 0인 경우
        for n1, n2 in combinations(n, 2):
            if (pn := -(n1 + n2)) in p_set:
                result.add(tuple(sorted([n1, n2, pn])))

        return result

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        nums.sort()

        for i in range(n - 2):
            # 이전 값과 중복되었다면 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # j, k를 양쪽에서부터 좁혀오면서 구하기
            j, k = i + 1, n - 1
            while j < k:
                _sum = nums[i] + nums[j] + nums[k]

                if _sum < 0:
                    j += 1

                elif _sum > 0:
                    k -= 1

                else:
                    result.append([nums[i], nums[j], nums[k]])

                    # 다음 값과 중복되었다면, 중복된 원소 중 가장 마지막 인덱스로 건너뛰기
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1

                    # 인덱스 업데이트
                    j += 1
                    k -= 1

        return result


###### review ######
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """two pointer (fast ver)"""

        result = []

        nums.sort()

        n = len(nums)

        for a in range(n - 2):
            # a가 가리키는 숫자가 이전과 같다면 빠르게 넘어가기
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            # b와 c를 a 오른쪽 영역에서 좁혀오며 확인
            b, c = a + 1, n - 1
            while b < c:
                _sum = nums[a] + nums[b] + nums[c]

                if _sum < 0:
                    b += 1

                elif _sum > 0:
                    c -= 1

                else:
                    result.append([nums[a], nums[b], nums[c]])

                    # 중복된 원소 건너뛰기
                    while b < c and nums[b] == nums[b + 1]:
                        b += 1
                    while b < c and nums[c] == nums[c - 1]:
                        c -= 1

                    b += 1
                    c -= 1

        return result

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        """two pointer (slow ver) (중복 건너뛰지 X)"""

        result = set()

        nums.sort()

        n = len(nums)

        for a in range(n - 2):
            b, c = a + 1, n - 1

            while b < c:
                _sum = nums[a] + nums[b] + nums[c]

                if _sum < 0:
                    b += 1

                elif _sum > 0:
                    c -= 1

                else:
                    result.add((nums[a], nums[b], nums[c]))
                    b += 1
                    c -= 1

        return list(result)
