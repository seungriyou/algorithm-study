# https://school.programmers.co.kr/learn/courses/30/lessons/12936

def solution(n, k):
    # backtracking 이용하면 TLE

    answer = []

    people = list(range(1, n + 1))  # 사전 순으로 나열해야하므로, 1 ~ n까지 오름차순으로 list 유지
    k -= 1  # people list에서 index로 접근하기 위함

    def factorial(num):
        val = 1
        for n in range(1, num + 1):
            val *= n
        return val

    while people:
        """
        _ / _ ... _
        n * (n - 1)!

        맨 왼쪽 원소가 정해진다면, 그 왼쪽에 올 수 있는 순열의 경우의 수는 (n - 1)! 개이다.
        따라서 people 내 원소에서 맨 왼쪽 원소가 될 수 있는 값의 인덱스는 k // (n - 1)!로 찾을 수 있다.
        이렇게 왼쪽부터 answer list를 채워가면 된다.
        """
        idx, k = divmod(k, factorial(len(people) - 1))
        answer.append(people.pop(idx))

    return answer
