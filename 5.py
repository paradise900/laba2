import os
from time import sleep


BLACK = "\u001b[40m"
END = '\u001b[0m'
RED = '\u001b[41m'
LENDTH = 10
for num in range(LENDTH):
    os.system("clear")
    if num % 2 == 0:
        print(f"{RED + '  ' + BLACK + '  ' + RED + '  ' + END}")
        print(f"{BLACK + '  ' + RED + '  ' + BLACK + '  ' + END}")
        print(f"{RED + '  ' + BLACK + '  ' + RED + '  '+ END}")
    else:
        print(f"{BLACK + '  ' + RED + '  ' + BLACK + '  '+ END}")
        print(f"{RED + '  ' + BLACK + '  ' + RED + '  '+ END}")
        print(f"{BLACK + '  ' + RED + '  ' + BLACK + '  '+ END}")
    sleep(0.1)
