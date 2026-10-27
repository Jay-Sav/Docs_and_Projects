import os
import subprocess

def clear_screen():
    if os.name == 'nt':  # For Windows
        subprocess.call('cls', shell=True)
    else:  # For Unix/Linux/Mac
        subprocess.call('clear', shell=True)  
        

