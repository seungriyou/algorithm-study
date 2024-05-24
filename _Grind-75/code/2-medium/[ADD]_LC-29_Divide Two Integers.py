class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        resolved TLE (O(logn * logn))
        - ref:
            - https://leetcode.com/problems/divide-two-integers/solutions/13407/c-bit-manipulations/comments/240434
            https://leetcode.com/problems/divide-two-integers/solutions/1327339/java-0ms-100-faster-obeys-all-conditions
        """

        # result 값
        cnt = 0

        # early stop & handle corner cases
        # note: python에서는 1 << 31이 -2147483648이 아닌 2147483648(long 타입)이므로 직접 숫자를 기입하자!
        MIN_INT, MAX_INT = -2147483648, 2147483647  # (1 << 31) -1

        # if divisor == 1 or dividend == 0:
        #     return dividend

        if dividend == MIN_INT:
            if divisor == MIN_INT:
                return 1
            elif divisor == -1:  # -- only corner case
                return MAX_INT
            else:
                """
                divisor != MIN_INT이므로 abs(divisor)는 overflow가 발생하지 X
                -> dividend에 abs(divisor)를 한 번 더해서 dividend != MIN_INT가 되도록하고, 미리 cnt 값을 1개 세기
                """
                dividend += abs(divisor)
                cnt += 1
        elif divisor == MIN_INT:
            return 0

        # convert to positive
        is_neg = (dividend < 0) ^ (divisor < 0)
        dvd, div = abs(dividend), abs(divisor)

        while dvd >= div:
            # divisor로 빼는 것을 더 효율적으로 변경!
            # divisor만큼 한 번씩 빼는 것이 아닌, divisor의 2배, divisor의 4배, divisor의 8배... 등 divisor의 2^n배로 크게 늘려가면서
            # 뺄셈을 log time으로 수행할 수 있다!
            # https://leetcode.com/problems/divide-two-integers/solutions/13403/clear-python-code/comments/148769

            n = 0  # div를 1개씩 빼지 X, 2^n개씩 빼기! -> log time으로 가능!
            while dvd >= (div << (n + 1)):
                n += 1

            cnt += 1 << n
            dvd -= div << n

        return -cnt if is_neg else cnt

    def divide_tle(self, dividend: int, divisor: int) -> int:
        """
        TLE ver (dividend = 2147483647, divisor = 1) O()

        왜 corner case가 dividend = -2^31, divisor = -1 일 때 뿐인지?
            - abs(dividend) -> overflow 발생하기 때문일텐데, 왜 divisor가 -1일 때 뿐이지..? 이해가 안가,,,

        풀이 과정 전체에서도 python이라고 해서 예외 없이, 32-bit int 자료형을 사용한다는 가정하에 풀어야 하는 것 같다.

        ref:
            - https://leetcode.com/problems/divide-two-integers/solutions/13403/clear-python-code
            - https://leetcode.com/problems/divide-two-integers/solutions/142849/c-java-python-should-not-use-long-int
        """

        # result 값
        cnt = 0

        # early stop & handle corner cases
        # note: python에서는 1 << 31이 -2147483648이 아닌 2147483648이므로 직접 숫자를 기입하자!
        MIN_INT, MAX_INT = -2147483648, 2147483647  # (1 << 31) -1

        if divisor == 1 or dividend == 0:
            return dividend

        if dividend == MIN_INT:
            if divisor == MIN_INT:
                return 1
            elif divisor == -1:  # -- only corner case
                return MAX_INT
            else:
                """
                divisor != MIN_INT이므로 abs(divisor)는 overflow가 발생하지 X
                -> dividend에 abs(divisor)를 한 번 더해서 dividend != MIN_INT가 되도록하고, 미리 cnt 값을 1개 세기
                """
                dividend += abs(divisor)
                cnt += 1
        elif divisor == MIN_INT:
            return 0

        # convert to positive
        is_neg = (dividend < 0) ^ (divisor < 0)
        dvd, div = abs(dividend), abs(divisor)

        # TLE 발생!!! 더 효율적으로 cnt 값을 세어보자!
        while dvd >= div:
            # dvd < div 인 순간, 현재의 cnt 값에 부호 붙여서 반환
            dvd -= div
            cnt += 1

        return -cnt if is_neg else cnt
