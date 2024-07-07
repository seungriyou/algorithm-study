# https://school.programmers.co.kr/learn/courses/30/lessons/12979

def solution(n, stations, w):
    answer = 0
    ran = (2 * w) + 1
    start = 1

    for station in stations:
        s, e = station - w, station + w

        if start < s:
            q, r = divmod(s - start, ran)
            answer += (q + (1 if r else 0))

        start = e + 1

    if start <= n:
        q, r = divmod(n - start + 1, ran)
        answer += (q + (1 if r else 0))

    return answer
