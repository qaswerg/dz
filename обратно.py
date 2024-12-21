a = input()

a_new = ''
for i in range(len(a)):
    a_new += a[-i-1]

print(a_new)