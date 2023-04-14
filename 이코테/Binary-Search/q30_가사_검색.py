# https://school.programmers.co.kr/learn/courses/30/lessons/60060

from bisect import bisect_left, bisect_right

def count_by_range(arr, left_val, right_val):
    left_idx = bisect_left(arr, left_val)
    right_idx = bisect_right(arr, right_val)
    return right_idx - left_idx

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

words_per_len = [[] for _ in range(10001)]
r_words_per_len = [[] for _ in range(10001)]
lengths = set()

for word in words:
    l = len(word)
    lengths.add(l)

    words_per_len[l].append(word)
    r_words_per_len[l].append(word[::-1])

for l in lengths:
    words_per_len[l].sort()
    r_words_per_len[l].sort()

result = []
for q in queries:
    if q[0] == "?":
        result.append(
            count_by_range(
                r_words_per_len[len(q)],
                q[::-1].replace("?", "a"),
                q[::-1].replace("?", "z")
            )
        )
    else:
        result.append(
            count_by_range(
                words_per_len[len(q)],
                q.replace("?", "a"),
                q.replace("?", "z")
            )
        )

print(result)
