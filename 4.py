black = "\u001b[40m"
white = '\u001b[47m'
end = '\u001b[0m'
red = '\u001b[41m'
green = '\u001b[42;1m'
length = 10
part = 125

file = open('itmo_study/laba2/sequence.txt')
numbers = []
for number in file:
    numbers.append(float(number[:-1]))
first_125 = sum(numbers[:part]) / part
second_125 = sum(numbers[part:]) / part

print(f"{green + ' ' * int(length + first_125 * length) + end} -- first 125 nums")
print(f"{red + ' ' * int(length + second_125 * length) + end} -- second 125 nums")
file.close()