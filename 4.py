BLACK = "\u001b[40m"
WHITE = '\u001b[47m'
END = '\u001b[0m'
RED = '\u001b[41m'
GREEN = '\u001b[42;1m'
LENGTH = 10
PART = 125

with open('itmo_study/laba2/sequence.txt') as file:
    numbers = []
    for number in file:
        numbers.append(float(number[:-1]))
    first_125 = sum(numbers[:PART]) / PART
    second_125 = sum(numbers[PART:]) / PART

    print(f"{GREEN + ' ' * int(LENGTH + first_125 * LENGTH) + END} -- first 125 nums")
    print(f"{RED + ' ' * int(LENGTH + second_125 * LENGTH) + END} -- second 125 nums")
    file.close()