# A02 - Linear Search
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_b

N, X = map(int, input().split())
A = list(map(int, input().split()))
if X in A:
    print('Yes')
else:
    print('No')
