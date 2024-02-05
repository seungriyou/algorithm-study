# https://www.acmicpc.net/problem/13164
import sys; input = sys.stdin.readline

N, K = map(int, input().split())
children = list(map(int, input().split()))

# 인접한 원생들 간의 키 차이(= 비용)를 모으고, 그것을 기준으로 내림차순 정렬
diff = [children[i] - children[i - 1] for i in range(1, N)]
diff.sort()

# 가장 큰 비용부터 K - 1 개 제외한 총 비용 더하기
print(sum(diff[:N - K]))
