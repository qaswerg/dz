sums = 0
N = int(input())
for i in range(2, N+1):
    for j in range(2, i):
        if i%j == 0: break
    else:
        sums += i

print(sums)