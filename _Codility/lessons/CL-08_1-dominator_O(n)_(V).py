# https://app.codility.com/programmers/lessons/8-leader/dominator/
# https://app.codility.com/demo/results/trainingF5W3KA-89F/

def solution(A):
    # O(n)
    """
    top이 stack의 top이라고 가정하면, 모든 원소를 순회하며
    - top과 값이 다르면 top을 pop & not append
    - 값이 같다면 append
    stack의 top 이하는 모두 같은 값을 가지게 될 것 이므로
    stack의 top과 그 size만 트래킹하면 되기 때문에 전체 stack list를 가질 필요는 없다!
    """

    # stack
    top = size = 0

    for a in A:
        # stack이 비어있으면 추가
        if size == 0:
            size += 1
            top = a
        else:
            # top과 같은 값이라면 append
            if top == a:
                size += 1
            # top과 다른 값이라면 top pop & not append
            else:
                size -= 1

    # check if the candidate(top) is dominant
    idx = cnt = 0
    for i, a in enumerate(A):
        if a == top:
            cnt += 1
            idx = i

    return idx if cnt > len(A) // 2 else -1