# https://school.programmers.co.kr/learn/courses/30/lessons/134239

def solution(k, ranges):
    answer = []

    def get_numbers(k):
        ans = [k]

        while k > 1:
            if k & 1:
                k = (k * 3) + 1
            else:
                k //= 2
            ans.append(k)

        return ans

    def get_area_per_range(nums):
        res = [0]

        for i in range(len(nums) - 1):
            r_height, t_height = min(nums[i], nums[i + 1]), abs(nums[i] - nums[i + 1])

            # 이전까지의 넓이 + (직사각형 부분 + 삼각형 부분)
            res.append(res[-1] + (r_height + 0.5 * t_height))

        return res

    # prefix sum 응용 (areas[i]: x=i 까지 정적분)
    areas = get_area_per_range(get_numbers(k))
    n = len(areas) - 1

    for a, b in ranges:
        if a > n + b:
            answer.append(-1)
        else:
            answer.append(areas[n + b] - areas[a])

    return answer
