# B03 - Supermarket 1
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cb
# 全探索

N = int(input())
A = list(map(int, input().split()))

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if A[i] + A[j] + A[k] == 1000:
                print('Yes')
                exit()
print('No')
