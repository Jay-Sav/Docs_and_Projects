#Locate Network Device Information from a CSV File
#This program uses the router_data.csv file for data


import csv


def main_menu():
    user_choice = 0
    while user_choice != 7:
        print('\n')
        print('Welcome to Network Information Locator!')
        print('---------------------------------------')
        print('1. Display all network device information')
        print('2. Add a new network device')
        print('3. Find network device(s) by device name')
        print('4. Find network device(s) by WAN IP address')
        print('5. Find network device(s) by Business Name')
        print('6. Find network device(s) by Business Location')
        print('7. Exit program')
        user_choice = int(input('Enter your choice: '))
        print('\n')
        if user_choice == 1:
            display_all()
        elif user_choice == 2:
            add_router()
        elif user_choice == 3:
            find_by_router_name()
        elif user_choice == 4:
            find_by_wan()
        elif user_choice == 5:
            find_by_business_name()
        elif user_choice == 6:
            find_by_location()
        elif user_choice == 7:
            exit()



def display_all():
    with open('router_data.csv') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            device_name = row[0]
            local_ip = row[1]
            wan_ip = row[2]
            device_location = row[3]
            isp = row[4]
            business_name = row[5]
            print (f'Device name: {device_name}, '
                   f'LAN: {local_ip}, WAN:{wan_ip}, '
                   f'Location: {device_location}, '
                   f'ISP: {isp}, '
                   f'Business Name: {business_name}')

def add_router():
    name = input('Name of new router')
    ip_address = input('IP address of new router')
    location = input('Location of new router')
    new_router = [name,ip_address,location]
    with open('router_data.csv', 'a') as csvfile:
        new_entry = csv.writer(csvfile)
        new_entry.writerow(new_router)

def find_by_router_name():
    router_name = input('Enter router name: ')
    with open('router_data.csv') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row[0] == router_name:
                print(f'Device name: {row[0]}\n'
                      f'LAN: {row[1]}, WAN: {row[2]}\n'
                      f'Location: {row[3]}\n'
                      f'ISP: {row[4]}\n'
                      f'Business Name: {row[5]}')

def find_by_wan():
    router_ip = input('Enter WAN IP address: ')
    with open('router_data.csv') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row[2] == router_ip:
                print(f'Device name: {row[0]}\n'
                      f'LAN: {row[1]}, WAN: {row[2]}\n'
                      f'Location: {row[3]}\n'
                      f'ISP: {row[4]}\n'
                      f'Business Name: {row[5]}')

def find_by_business_name():
    business_name = input('Enter business name: ')
    with open('router_data.csv') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row[5] == business_name:
                print(f'Device name: {row[0]}\n'
                      f'LAN: {row[1]}, WAN: {row[2]}\n'
                      f'Location: {row[3]}\n'
                      f'ISP: {row[4]}\n'
                      f'Business Name: {row[5]}\n')

def find_by_location():
    location = input('Enter location: ')
    with open('router_data.csv') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row[3] == location:
                print(f'Device name: {row[0]}\n'
                      f'LAN: {row[1]}, WAN: {row[2]}\n'
                      f'Location: {row[3]}\n'
                      f'ISP: {row[4]}\n'
                      f'Business Name: {row[5]}\n')




if __name__ == '__main__':
    main_menu()

