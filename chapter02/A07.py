# A07 - Event Attendance
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_g
# 累積和

D = int(input())
N = int(input())
A = [0]*(D+1)
for i in range(N):
    L, R = map(int, input().split())
    A[L-1] += 1
    A[R] -= 1
for i in range(D):
    print(A[i])
    A[i+1] += A[i]
