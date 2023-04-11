str1 = input()
str2 = input()

def edit_distance(str1, str2):
    n = len(str1)
    m = len(str2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n):
        dp[i][0] = i
    for j in range(m):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 두 문자가 같다면, upper left에 해당하는 값 그대로
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # 두 문자가 다르다면 연산이 필요한 것이므로,
            # min(upper left(교체), left(삽입), upper(삭제)) + 1
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])

    return dp[n][m]

print(edit_distance(str1, str2))
