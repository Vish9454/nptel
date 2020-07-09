def lcs(g):
    X = g[0];
    Y = g[1]
    n = len(X)
    m = len(Y)
    print(X, Y)
    dp = [[0] * (m + 1) for z in range(n + 1)]
    print(dp)
    for i in range(n):
        for j in range(m):
            if X[i] == Y[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    return dp[-1][-1]


m = ["AGGTAB", "GXTXAYB"]
print(lcs(m))
