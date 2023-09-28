import os
from time import sleep


black = "\u001b[40m"
white = '\u001b[47m'
end = '\u001b[0m'
red = '\u001b[41m'
green = '\u001b[42;1m'

for i in range(10):
    os.system("clear")
    if i % 2 == 0:
        print(red + '  ' + black + '  ' + red + '  ' + end)
        print(black + '  ' + red + '  ' + black + '  ' + end)
        print(red + '  ' + black + '  ' + red + '  '+ end)
    else:
        print(black + '  ' + red + '  ' + black + '  '+ end)
        print(red + '  ' + black + '  ' + red + '  '+ end)
        print(black + '  ' + red + '  ' + black + '  '+ end)
    sleep(0.1)
