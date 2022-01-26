# [SEA] 6109 - 추억의 2048게임

import sys
from typing import List

sys.stdin = open('input.txt')
input = sys.stdin.readline


def rotate_map(game_map: List[int]) -> List[int]:
    l = len(game_map)
    rotated = [[0] * l for _ in range(l)]
    for i in range(l):
        for j in range(l):
            rotated[j][l-i-1] = game_map[i][j]
    return rotated


def move_tiles(game_map: List[int]) -> List[int]:
    l = len(game_map)
    if l < 2:
        return game_map
    for i in range(l):
        j, k = 0, 1
        for _ in range(game_map[i].count(0)):
            game_map[i].remove(0)
            game_map[i].append(0)
        while k < l:
            if game_map[i][j] == game_map[i][k]:
                game_map[i][j] += game_map[i].pop(k)
                game_map[i].append(0)
            j += 1
            k += 1
    return game_map


def print_map(n: int, game_map: List[int]) -> None:
    l = len(game_map)
    print(f'#{n}')
    for i in range(l):
        # print(' '.join(map(str, game_map[i])))
        print(*game_map[i])


T = int(input())
for test_case in range(1, T + 1):
    l, d = map(str, input().split())
    game_map = []
    for _ in range(int(l)):
        game_map.append(list(map(int, input().split())))
    if d == "up":
        print_map(test_case, rotate_map(move_tiles(rotate_map(rotate_map(rotate_map(game_map))))))
    elif d == "right":
        print_map(test_case, rotate_map(rotate_map(move_tiles(rotate_map(rotate_map(game_map))))))
    elif d == "down":
        print_map(test_case, rotate_map(rotate_map(rotate_map(move_tiles(rotate_map(game_map))))))
    else:
        print_map(test_case, move_tiles(game_map))
