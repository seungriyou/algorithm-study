# https://school.programmers.co.kr/learn/courses/30/lessons/17680

from collections import deque


def solution(cacheSize, cities):
    # cacheSize가 0인 경우, cache를 사용할 수 없으므로 빠르게 return!
    if cacheSize == 0:
        return len(cities) * 5

    cache = deque(maxlen=cacheSize)
    time = 0

    for city in cities:
        _city = city.lower()

        # cache hit
        if _city in cache:
            time += 1
            cache.remove(_city)

        # cache miss
        else:
            if len(cache) == cacheSize:
                cache.popleft()
            time += 5
        cache.append(_city)

    return time


def solution_maxlen(cacheSize, cities):
    cache = deque(maxlen=cacheSize)  # -- maxlen 인자 설정
    time = 0

    for city in cities:
        _city = city.lower()

        # cache hit
        if _city in cache:
            time += 1
            cache.remove(_city)
            cache.append(_city)

        # cache miss
        else:
            time += 5
            cache.append(_city)

    return time
