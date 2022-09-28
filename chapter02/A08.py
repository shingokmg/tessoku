# A08 - Two Dimensional Sum
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_h
# 二次元の累積和

H, W = map(int, input().split())
S = [list(map(int, input().split())) for i in range(H)]
Q = int(input())
T = [[0]*(W+1) for _ in range(H+1)]
for i in range(H):
    for j in range(W):
        T[i+1][j+1] = T[i+1][j] + T[i][j+1] - T[i][j] + S[i][j]
for i in range(Q):
    A, B, C, D = map(int, input().split())
    ans = T[C][D] + T[A-1][B-1] - (T[C][B-1] + T[A-1][D])
    print(ans)
