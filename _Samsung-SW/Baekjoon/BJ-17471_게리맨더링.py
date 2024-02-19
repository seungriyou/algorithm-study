# https://www.acmicpc.net/problem/17471
import sys; input = sys.stdin.readline
from collections import deque

N = int(input())
population = [-1] + list(map(int, input().split()))
graph = [[]] + [list(map(int, input().split()))[1:] for _ in range(N)]


def is_connected(subset):
    """
    subset에 포함된 노드들이 서로 연결되어 있는지 여부를 반환하는 함수 (w/ bfs)
    """
    # subset이 비어있다면 False 리턴
    if not subset:
        return False

    _subset = set(subset)           # subset에서 remove, pop 등의 연산을 수행할 것이므로 set 복사
    q = deque([_subset.pop()])

    while q:
        pos = q.popleft()

        for npos in graph[pos]:
            if npos in _subset:
                q.append(npos)
                _subset.remove(npos)

    # 연결되어 있는 노드는 모두 _subset에서 remove 되었을 것이기 때문에,
    # _subset에 남아있는 노드가 없어야 모두 연결된 것이다!
    return len(_subset) == 0


def get_subsets(target_num):
    """
    전체 노드 중 target_num 개의 노드를 고르는 조합을 반환하는 함수 (w/ backtracking)
    """
    result = []         # 모든 조합을 담을 리스트
    elements = set()

    def backtrack(idx, target_num):
        # base condition
        if len(elements) == target_num:
            result.append(set(elements))    # 현재 조합을 복제해서 result에 담기
            return

        # recur
        for i in range(idx, N + 1):
            elements.add(i)
            backtrack(i + 1, target_num)
            elements.remove(i)

    # 1번 노드부터 시작
    backtrack(1, target_num)

    return result


def get_population(subset):
    """
    주어진 subset에 포함된 모든 노드에서의 총 인구수의 합을 반환하는 함수
    """
    return sum(population[i] for i in subset)


def solution():
    min_diff = 1_000
    total_set = set(range(1, N + 1))

    # 1개 ~ N // 2개의 노드를 선택하는 조합들을 모두 구하기
    # 어차피 subset과 other_subset에 대해 모두 검사할 것이므로, N // 2개까지만 고르는 조합을 구해도 된다!
    for target_num in range(1, N // 2 + 1):
        subsets = get_subsets(target_num)

        # target_num 개의 노드를 선택한 조합들을 순회하면서
        for subset in subsets:
            other_subset = total_set - subset
            # subset과 other_subset에 대해 각각이 모두 서로 연결되어 있다면, min_diff 업데이트
            if is_connected(subset) and is_connected(other_subset):
                min_diff = min(min_diff, abs(get_population(subset) - get_population(other_subset)))

    # min_diff가 초기값과 동일하다면 선거구를 나눌 수 없는 것이므로 -1 반환
    return -1 if min_diff == 1_000 else min_diff


print(solution())
