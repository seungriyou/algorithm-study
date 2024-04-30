# https://leetcode.com/problems/sort-colors/

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1-pass algorithm & O(1) space (Dutch national flag problem)

        # 1. 세 color의 pointer 초기화
        # red는 왼쪽에, blue는 오른쪽에 위치해야 하므로 양끝에서 시작한다.
        # white는 왼쪽에서부터 이동하면서, 상황에 따라 red나 blue와 swap 한다.
        red, white, blue = 0, 0, len(nums) - 1

        # 2. white를 옮겨가면서 swap 한다.
        # red / white / blue 순서로 위치해야 하므로, 상황에 맞게 white가 가리키는 원소를 red 및 blue가 가리키는 원소와 swap 하면 된다.
        while white <= blue:
            # (1) nums[white]가 red인 경우
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1        # nums[red - 1] 까지가 확실한 red가 됨
                white += 1
            # (2) nums[white]가 whit인 경우
            elif nums[white] == 1:
                white += 1
            # (3) nums[white]가 blue인 경우
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1       # nums[blue + 1] 까지가 확실한 blue가 됨


    def sortColors2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 2-pass algorithm

        # 1. 숫자의 개수 세기
        cnt = [0] * 3
        for num in nums:
            cnt[num] += 1

        # 2. 각 숫자의 개수만큼 inplace로 채우기
        i = 0
        for num, c in enumerate(cnt):
            for _ in range(c):
                nums[i] = num
                i += 1


###### review ######
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """O(1) space & one-pass"""

        # red: 확실하게 red인 원소의 다음 원소의 index
        # blue: 확실하게 blue인 원소의 이전 원소의 index
        # white: 움직이면서 red 및 blue와 swap
        red, white, blue = 0, 0, len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1  # nums[red - 1] 까지 red
                white += 1

            elif nums[white] == 1:
                white += 1

            elif nums[white] == 2:
                nums[blue], nums[white] = nums[white], nums[blue]
                blue -= 1  # nums[blue + 1] 까지 blue
                # white += 1은 X

    def sortColors2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = [0, 0, 0]
        for num in nums:
            cnt[num] += 1

        j = 0
        for i, c in enumerate(cnt):
            for _ in range(c):
                nums[j] = i
                j += 1
