# [PG] 42577 - 전화번호 목록 (Lv2)
# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    sorted_pb = sorted(phone_book)

    for p, c in zip(sorted_pb, sorted_pb[1:]):
        if c.startswith(p):
            return False

    return True


def solution2(phone_book):
    sorted_pb = sorted(phone_book)

    for i in range(1, len(phone_book)):
        prev = sorted_pb[i - 1]
        if sorted_pb[i][:len(prev)] == prev:
            return False

    return True

##### review #####
def solution1(phone_book):
    _set = set(phone_book)

    for p in phone_book:
        prefix = ""

        for n in p:
            prefix += n
            if prefix in _set and prefix != p:
                return False

    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution1(["119", "97674223", "1195524421"]))
print(solution2(["119", "97674223", "1195524421"]))
