# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
# https://app.codility.com/demo/results/trainingJ6HSVB-ZEU/

def solution(A):
    # hash table
    appeared_odd = set()

    for a in A:
        if a in appeared_odd:
            appeared_odd.remove(a)
        else:
            appeared_odd.add(a)

    return appeared_odd.pop()
