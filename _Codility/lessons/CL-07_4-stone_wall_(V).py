# https://app.codility.com/programmers/lessons/7-stacks_and_queues/stone_wall/
# https://app.codility.com/demo/results/trainingJN5PCG-UU8/

def solution(H):
    # 연속된 구간에 대해 이전의 기준값을 토대로 판단해나가기 위해 stack 사용!
    stack = []
    # 이전 높이보다 현재 높이가 낮을 경우, 추가된 block의 수
    cnt = 0

    for h in H:
        # stack에 쌓여있는 block들을 뒤에서부터 확인해나가기
        while stack:
            # 이전 높이 > 현재 높이: 이전 block pop 후 block 개수 증가
            if stack[-1] > h:
                stack.pop()
                cnt += 1
            # 이전 높이 < 현재 높이: stack에 추가
            elif stack[-1] < h:
                stack.append(h)
                break
            # 이전 높이 == 현재 높이: 이전 높이와 하나의 block으로 커버되므로 그냥 넘어가기
            else:
                break
        # stack이 비어있다면 현재 높이 append
        if not stack:
            stack.append(h)

    # stack에 남아있는 block 개수도 반영
    return cnt + len(stack)
