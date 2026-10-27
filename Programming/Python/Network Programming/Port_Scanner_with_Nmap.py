#Performs a port scan on target host using Nmap
#Nmap must be installed

import subprocess

target_host = input('Enter the target host: ')

subprocess.run(f'nmap {target_host}', shell=True)

input('Press any Key to quit')



