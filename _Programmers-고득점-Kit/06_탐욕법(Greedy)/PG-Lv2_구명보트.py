# https://school.programmers.co.kr/learn/courses/30/lessons/42885

def solution1(people, limit):
    # TIP: 2명씩만 탈 수 있다! -> two pointer

    people.sort()
    left, right = 0, len(people) - 1
    cnt = 0

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        cnt += 1

    return cnt


def solution2(people, limit):
    # TIP: 2명씩만 탈 수 있다! -> two pointer

    people.sort()
    left, right = 0, len(people) - 1
    two_people_boat = 0

    while left < right:
        if people[left] + people[right] <= limit:
            left += 1
            two_people_boat += 1
        right -= 1

    return len(people) - two_people_boat


people, limit = [70, 50, 80, 50], 100
print(solution1(people, limit)) # should return 3
print(solution2(people, limit)) # should return 3
