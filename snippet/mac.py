import time
import os

interface = 'enp3s0'

def changeMac():
    os.system(f'sudo ifconfig {interface} down')
    time.sleep(0.2)
    os.system(f'sudo macchanger -r {interface}')
    time.sleep(0.2)
    os.system(f'sudo ifconfig {interface} up')
    time.sleep(0.2)
    os.system("ifconfig")
if __name__ == "__main__":
    changeMac()
