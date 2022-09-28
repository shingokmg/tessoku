# A06 - How Many Guests?
# https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_ai
# 累積和

N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = [A[0]]
for i in range(1, N):
    B.append(A[i]+B[-1])
for i in range(Q):
    L, R = map(int, input().split())
    print(B[R-1]-B[L-1]+A[L-1])
