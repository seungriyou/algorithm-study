# https://www.acmicpc.net/problem/18110
import sys; input = sys.stdin.readline

n = int(input())
opinions = [int(input()) for _ in range(n)]

# 30% 절사평균 -> 상위 15%, 하위 15% 제외
# 반올림

def _round(original):
    if original >= int(original) + 0.5:
        return int(original) + 1
    else:
        return int(original)

if n > 0:
    opinions.sort()
    except_num = _round(n * .15)
    if except_num:
        print(_round(sum(opinions[except_num:-except_num]) / (n - 2 * except_num)))
    else:
        print(_round(sum(opinions) / n))
else:
    print(0)
