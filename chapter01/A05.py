# A05 - Three Cards
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_e
# 全探索

N, K = map(int, input().split())
ans = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if i + j < K <= i + j + N:
            ans += 1
print(ans)
