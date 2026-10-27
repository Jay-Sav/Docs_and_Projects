#Outputs CPU%, Ram%, and Disk Usage

import psutil
from psutil import cpu_percent
import os
import time


print('Gathering Computer Statistics')

cpu = cpu_percent(interval=3)
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage('C:/').percent

os.system('cls')

print('Displaying Computer Performance')
time.sleep(1)

print()
print(f'CPU Usage: {cpu}%')
time.sleep(1)
print()
print(f'Current RAM Usage: {ram}%')
time.sleep(1)
print()
print(f'Current Disk Usage: {disk}%')
print()
input('Press ENTER to exit...')