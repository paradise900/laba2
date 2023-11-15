BLACK = "\u001b[40m"
WHITE = '\u001b[47m'
END = '\u001b[0m'
WIDTH = 2
LENGTH = 9
print(f"{BLACK + ' ' * WIDTH * LENGTH + END}" )
print( f"{WHITE + ' ' * WIDTH * WIDTH**2 + BLACK + ' ' * WIDTH + WHITE + ' ' * WIDTH**3 + END}" )
print( f"{BLACK + ' ' * WIDTH * LENGTH + END}" )
print( f"{WHITE + ' ' * WIDTH + BLACK + ' ' * WIDTH + WHITE + ' ' * LENGTH + BLACK + ' ' * WIDTH + WHITE + ' ' * WIDTH + END}" )
print( f"{BLACK + ' ' * WIDTH * LENGTH + END}" )
