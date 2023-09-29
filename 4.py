black = "\u001b[40m"
white = '\u001b[47m'
end = '\u001b[0m'
red = '\u001b[41m'
green = '\u001b[42;1m'

f = open('itmo_study/laba2/sequence.txt')
a = []
for x in f:
    a.append(float(x[:-1]))
s1 = sum(a[:125]) / 125
s2 = sum(a[125:]) / 125

print( green + ' ' * int(10 + s1 * 10) + end + ' -- first 125 nums' )
print( red + ' ' * int(10 + s2 * 10) + end + ' -- second 125 nums')
f.close()