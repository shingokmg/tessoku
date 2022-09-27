N = int(input())

B = bin(N)[2:]
print('0'*(10-len(B))+B)
