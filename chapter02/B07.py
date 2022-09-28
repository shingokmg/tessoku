# B07 - Convenience Store 2
# https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_al
# 一次元の累積和

T = int(input())
N = int(input())
A = [0]*(T+1)
for i in range(N):
    L, R = map(int, input().split())
    A[L] += 1
    A[R] -= 1
for i in range(T):
    print(A[i])
    A[i+1] += A[i]
