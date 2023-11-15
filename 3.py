BLACK = "\u001b[40m"
WHITE = '\u001b[47m'
END = '\u001b[0m'
LEN_X = 82
LEN_Y = 10

chart = [[WHITE + ' '] * LEN_X for _ in range(LEN_Y)]
for dot in range(10):
    chart[dot][dot**2] = BLACK + ' '

for axis_y in reversed(range(len(chart))):
    print(f"{WHITE + str(axis_y)}", *chart[axis_y])
axis = '  '
for num in range(10):
    axis += str(num) + ' '
for num in range(10, 82):
    if num ** 0.5 == int(num ** 0.5):
        axis += str(num)
    else:
        axis += '  '
print(f"{axis + END}")
print('f(x) = x ^ 0.5')