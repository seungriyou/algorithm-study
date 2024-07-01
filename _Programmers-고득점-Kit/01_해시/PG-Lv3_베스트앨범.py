# [PG] 42579 - 베스트앨범 (Lv3)
# https://school.programmers.co.kr/learn/courses/30/lessons/42579

from collections import defaultdict


def solution(genres, plays):
    result = []

    # (play, i) -> play 기준으로 내림차순, 같은 경우에는 고유 번호 i 기준으로 오름차순 정렬
    sorted_plays = sorted(((play, i) for i, play in enumerate(plays)), key=lambda x: (-x[0], x[1]))

    # hash table에 sort 된 순서대로 넣어주기
    genre_num = defaultdict(list)  # 장르별 고유 번호 (순서대로): {"genre": [고유 번호]}
    genre_sum = defaultdict(int)  # 장르별 총 재생 횟수: {"genre": 총 재생 횟수}
    for play, i in sorted_plays:
        genre_num[genres[i]].append(i)
        genre_sum[genres[i]] += play

    # genre 간 순서 sorting으로 구하기 (총 재생 횟수 기준 내림차순으로 정렬)
    for genre, _ in sorted(genre_sum.items(), key=lambda x: -x[1]):  # (genre 이름, 재생 횟수)
        # slicing으로 result에 extend
        result.extend(genre_num[genre][:2])

    return result


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
assert [4, 1, 3, 0] == solution(genres, plays)


##### review #####
def solution(genres, plays):
    from collections import defaultdict

    res = []

    # (play, i): play 기준 내림차순, i 기준 오름차순
    sorted_plays = sorted(((play, i) for i, play in enumerate(plays)), key=lambda x: (-x[0], x[1]))

    genre_num = defaultdict(list)  # 고유 번호
    genre_sum = defaultdict(int)  # 노래 개수

    for play, i in sorted_plays:
        genre_num[genres[i]].append(i)
        genre_sum[genres[i]] += play

    for genre, _ in sorted(genre_sum.items(), key=lambda x: -x[1]):
        res.extend(genre_num[genre][:2])

    return res
