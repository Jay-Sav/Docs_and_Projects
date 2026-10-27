import time

def progress_bar():
    for i in range(0,101,20):
        time.sleep(0.1)
        print(f'\rLoading Game: {i}%', end='')
    print('\nDone!')
    for i in range(0,25,5):
        time.sleep(0.1)
