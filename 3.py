black = "\u001b[40m"
white = '\u001b[47m'
end = '\u001b[0m'

chart = [[white + ' '] * 82 for _ in range(10)]
for dot in range(10):
    chart[dot][dot**2] = black + ' '

for axis_y in reversed(range(len(chart))):
    print(white + str(axis_y), *chart[axis_y])
axis = '  '
for num in range(10):
    axis += str(num) + ' '
for num in range(10, 82):
    if num ** 0.5 == int(num ** 0.5):
        axis += str(num)
    else:
        axis += '  '
print(axis + end)
print('f(x) = x ^ 0.5')