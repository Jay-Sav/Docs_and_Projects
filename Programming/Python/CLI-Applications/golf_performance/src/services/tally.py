import time

def tally_bar():
    for i in range(0,120,5):
        time.sleep(0.1)
        print('-',end='',flush=True)
    