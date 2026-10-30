#Returns all processes currently running
#Outputs to file "running_process.csv"

import csv
import psutil


export_file = 'running_processes.csv'
process_counter = 0


with open(export_file, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['PID', 'Name', 'Status', 'CPU%'])
    for process in psutil.process_iter(['pid', 'name','status', 'cpu_percent']):
        writer.writerow([f'Process ID: {process.info['pid']}',
                         f'Process Name: {process.info['name']}',
                         f'Process Status: {process.info['status']}',
                         f'Process CPU Percent: {process.info['cpu_percent']}',
                         ])
        process_counter += 1
    writer.writerow([f'Total Running Processes: {process_counter}',])


print(f'Computer Processes have been sent to file {export_file} ')