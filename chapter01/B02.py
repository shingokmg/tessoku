# B02 - Divisor Check
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ca
# 全探索

A, B = map(int, input().split())
for i in range(A, B+1):
    if 100 % i == 0:
        print('Yes')
        exit()
print('No')
