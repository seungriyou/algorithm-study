# https://school.programmers.co.kr/learn/courses/30/lessons/131130

def solution(cards):
    graph = {i: cards for i, cards in enumerate(cards, start=1)}
    cnt = []  # 각 그룹 내에 속하는 상자의 개수
    n = len(cards)
    visited = [False] * (n + 1)

    def count_boxes_per_group(box):
        """BFS"""
        bcnt = 0

        while not visited[box]:
            bcnt += 1
            visited[box] = True
            box = graph[box]

        return bcnt

    for box in range(1, n + 1):
        if not visited[box]:
            cnt.append(count_boxes_per_group(box))

    if len(cnt) < 2:
        return 0

    cnt.sort(reverse=True)

    return cnt[0] * cnt[1]
