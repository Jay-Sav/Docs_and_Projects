import socket
import sys

# Create Socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print(f'Socket creation error: {msg}')
    sys.exit()



#Get target website or IP
target = input('Enter target website or IP address: ')



#Get target port number
try:
    port = int(input('Enter target port: '))
except ValueError:
    print(f'Invalid port number: {port}')
    sys.exit()


#Perfrom DNS Lookup of target host
try:
    host_ip = socket.gethostbyname(target)
except socket.gaierror:
    print(f'Hostname could not be resolved: {host_ip}')
    sys.exit()



#Attempt connection to target host over target port, then closes
try:
    s.connect((host_ip, port))
    print('Connected to ' + host_ip)
except socket.gaierror:
    print(f'Connection to {host_ip} failed: {host_ip}')
    sys.exit()
except TimeoutError:
    print(f'Connection to {host_ip} timed out')
    sys.exit()
except socket.error:
    print(f'Connection to {host_ip} failed: {host_ip}')
    sys.exit()
finally:
    s.close()

input('Press Enter to close...')

