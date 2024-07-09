# https://school.programmers.co.kr/learn/courses/30/lessons/68936

def solution(arr):
    answer = [0, 0]  # [0의 개수, 1의 개수]

    def compress(r, c, length):
        # base condition: 내부가 모두 같은 수이거나 변의 길이가 1이면 압축 (cnt 업데이트)
        if length == 1 or is_same(r, c, length):
            answer[arr[r][c]] += 1
            return

        # recur: 아니라면 또 쪼개기
        half = length // 2
        compress(r, c, half)
        compress(r + half, c, half)
        compress(r, c + half, half)
        compress(r + half, c + half, half)

    def is_same(r, c, length):
        num = arr[r][c]
        for dr in range(length):
            for dc in range(length):
                if num != arr[r + dr][c + dc]:
                    return False
        return True

    compress(0, 0, len(arr))

    return answer
