import platform
import os
import sys
import time

# Don't use this script! Not good enough!
"""

1. loads everything I need to start my work.

2. print(sys.argv[0])   current-file-abs-path
3. print(os.getenv('USERNAME'))     user-name
4. print(platform.node())       PC-name
"""


def greet():
    print("晚上好！" + os.getenv('USERNAME'))
    print(f"{sys.argv[0]} is running on {platform.node()}")


def change_mac():
    os.chdir('/home/fc/')
    # print('\n'.join(os.listdir('.')))
    os.system('sudo python3 mac.py')
   

def open_editor():
    os.system('atom')
    os.system('subl')
    time.sleep(3)


if __name__ == '__main__':
    greet()
    change_mac()
    open_editor()
