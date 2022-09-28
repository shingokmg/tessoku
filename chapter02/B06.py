# B06 - Lottery
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ce
# 累積和

N = int(input())
A = list(map(int, input().split()))
B = [A[0]]
for i in range(1, N):
    B.append(B[-1]+A[i])
Q = int(input())
for i in range(Q):
    L, R = map(int, input().split())
    ans = (B[R-1]-B[L-1]+A[L-1])/(R-L+1)
    if ans > 0.5:
        print('win')
    elif ans < 0.5:
        print('lose')
    else:
        print('draw')
