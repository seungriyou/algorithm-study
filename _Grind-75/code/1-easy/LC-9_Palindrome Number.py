# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        절반까지만 reversed_x 구하기
        """
        # 맨 오른쪽 값이 0이면 reverse 시 없어지므로, 조건 추가
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        reversed_x = 0
        tmp_x = x

        while tmp_x > reversed_x:
            reversed_x = reversed_x * 10 + tmp_x % 10
            tmp_x //= 10

        # (길이가 짝수일 때) or (길이가 홀수일 때)
        return reversed_x == tmp_x or reversed_x // 10 == tmp_x

    def isPalindrome2(self, x: int) -> bool:
        """
        - 음수: False 반환
        - 양수: 뒤집은 수 reversed_x를 구하려면, x의 오른쪽에서부터 구한 숫자가 reversed_x의 왼쪽에 오도록 더해나가기
        """

        if x < 0:
            return False

        reversed_x = 0
        tmp_x = x

        while tmp_x:
            reversed_x = reversed_x * 10 + tmp_x % 10
            tmp_x //= 10

        return reversed_x == x
