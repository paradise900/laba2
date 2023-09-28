black = "\u001b[40m"
white = '\u001b[47m'
end = '\u001b[0m'

a = [[white + ' '] * 82 for _ in range(10)]
for x in range(10):
    a[x][x**2] = black + ' '

for i in reversed(range(len(a))):
    print(white + str(i), *a[i])
s = '  '
for i in range(10):
    s += str(i) + ' '
for i in range(10, 82):
    if i ** 0.5 == int(i ** 0.5):
        s += str(i)
    else:
        s += '  '
print(s + end)
print('f(x) = x ^ 0.5')