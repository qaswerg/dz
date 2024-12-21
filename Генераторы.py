def even_generator(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num

print(list(even_generator([1,2,3,4,5,6,7,8,9])))


def long_strings_gen(strings):
    for s in strings:
        if len(s) > 3:
            yield s            

print(list(long_strings_gen(['asf', 'asfsadf', 'seexsex', 'chlen'])))


def unique_letters(string):
    seen = set()
    for char in string:
        if char not in seen:
            seen.add(char)
            yield char

print(list(unique_letters('SDGFGGFHTYNKTYNELWMKL;GMEBORNGMWP')))


def sqrt_generator(n):
    num = n
    while True:
        if num >= 0:
            num = num**0.5
            yield num

a = sqrt_generator(8)
print(next(a), next(a))
