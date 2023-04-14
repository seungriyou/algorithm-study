# https://school.programmers.co.kr/learn/courses/30/lessons/60058

p = "()))((()"

# 균형잡힌 괄호 문자열의 끝 인덱스 반환
def balanced_index(p):
    cnt = 0 # "("의 개수
    for i in range(len(p)):
        if p[i] == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return i

# 올바른 괄호 문자열인지 판단
def is_proper(p):
    cnt = 0 # "("의 개수
    for i in p:
        if i == "(":
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
    return True

def solution(p):
    answer = ""

    if not p:
        return answer

    i = balanced_index(p)
    u = p[:i + 1]
    v = p[i + 1:]

    if is_proper(u):
        answer = u + solution(v) # v에 대해 1단계부터 다시 수행한 후, u에 이어 붙이기
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        u = list(u[1:-1])
        for i in u:
            if i == "(":
                answer += ")"
            else:
                answer += "("

    return answer

print(solution(p))
