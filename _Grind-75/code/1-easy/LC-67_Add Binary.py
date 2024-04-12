# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0

        a, b = list(a), list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result.append(str(carry % 2))
            carry //= 2

        return "".join(result)[::-1]


###### review ######
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0

        a, b = list(a), list(b)

        while a or b or carry:
            # a와 b에 아직 남아있으면 carry에 더해나가기
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            # res 업데이트
            res.append(str(carry % 2))

            # carry 업데이트
            carry //= 2

        return "".join(res)[::-1]

    def addBinary1(self, a: str, b: str) -> str:
        res = ""

        # 뒤집고, 길이 맞추기
        max_len = max(len(a), len(b))
        a = a[::-1] + "0" * (max_len - len(a))
        b = b[::-1] + "0" * (max_len - len(b))

        # carry의 초기값은 0부터 시작
        carry = 0

        # a와 b 뒤집은 것에서 같은 자리수끼리 & carry까지 함께 연산
        for _a, _b in zip(a, b):
            _a, _b = int(_a), int(_b)

            # 현재 보고 있는 자리의 값들과 carry 더하기
            _sum = _a + _b + carry

            # carry 업데이트
            carry = _sum // 2

            # res에 결과 기록
            res += str(_sum % 2)

        # carry가 1이면 res에 반영
        if carry:
            res += str(carry)

        # 뒤집어서 반환
        return res[::-1]
