from colorama import init, Fore, Back, Style
init()

# pip3 install colorama
# colors :BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.

print(Fore.RED + "some red text")
print(Back.GREEN + "and with a green bg")
print(Style.DIM + "and with a dim text")    # dim 暗淡的
print(Style.RESET_ALL)
print("back to normal now")



