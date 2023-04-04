# 주의: len(s) == 16인 경우, s[12:18]를 출력해도 오류가 발생하지 않는다.

s = "ababcdcdababcdcd"

def solution(s):
    answer = len(s)

    # 1개부터 len(s) // 2까지 step을 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        cnt = 1
        prev = s[:step]

        for i in range(step, len(s), step):
            if prev == s[i:i + step]:
                cnt += 1
            else:
                compressed += str(cnt) + prev if cnt > 1 else prev
                # 상태 초기화
                prev = s[i:i + step]
                cnt = 1

        # 남아있는 문자열 처리
        compressed += str(cnt) + prev if cnt > 1 else prev
        answer = min(answer, len(compressed))

    return answer

print(solution(s))
