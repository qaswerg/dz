x = input("Введите что-то: ")

for i in range(0, len(x)):
    if x[i] != x[-i-1]:
        print('no')
        break
else:
    print('yes')