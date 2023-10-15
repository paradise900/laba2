red = '\u001b[41m'
white = '\u001b[47m'
end = '\u001b[0m'

length = 20
for _ in range(3):
    print(white + ' ' * length + end)
for _ in range(3):
    print(red + ' ' * length + end)
