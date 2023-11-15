RED = '\u001b[41m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
LENGHT = 20
ITERATIONS = 3

for _ in range(ITERATIONS):
    print(f"{WHITE + ' ' * LENGHT + END}")
for _ in range(ITERATIONS):
    print(f"{RED + ' ' * LENGHT + END}")