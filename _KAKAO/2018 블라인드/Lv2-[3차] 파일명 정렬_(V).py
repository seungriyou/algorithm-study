# https://school.programmers.co.kr/learn/courses/30/lessons/17686
import re


def solution(files):
    # 우선순위에 주의하자!
    # re 사용법 기억하기: re.search().group(), re.search().span(), re.split()

    # 1차: number로 sort (int 변환)
    files.sort(key=lambda x: int(re.search('\d+', x).group()))
    # 2차: head로 sort (case-sensitive X)
    files.sort(key=lambda x: re.split('\d+', x.lower())[0])

    return files


# merge sort 커스텀
# -> 효율성 별로임 x_x
def solution_merge_sort(files):
    def split_filename(file):
        ns, ne = re.search('[0-9]+', file.lower()).span()
        head, number = file[:ns], file[ns:ne]
        return head.lower(), int(number)

    def merge_sort(arr):
        if len(arr) < 2:
            return arr

        mid = len(arr) // 2
        low_arr = merge_sort(arr[:mid])
        high_arr = merge_sort(arr[mid:])

        merged_arr = []
        l = h = 0

        while l < len(low_arr) and h < len(high_arr):
            ls, hs = split_filename(low_arr[l]), split_filename(high_arr[h])

            if ls[0] == hs[0]:
                if ls[1] <= hs[1]:
                    merged_arr.append(low_arr[l])
                    l += 1
                else:
                    merged_arr.append(high_arr[h])
                    h += 1
            else:
                if ls[0] <= hs[0]:
                    merged_arr.append(low_arr[l])
                    l += 1
                else:
                    merged_arr.append(high_arr[h])
                    h += 1

        merged_arr += low_arr[l:]
        merged_arr += high_arr[h:]

        return merged_arr

    return merge_sort(files)
