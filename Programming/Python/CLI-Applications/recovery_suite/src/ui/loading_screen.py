import time

def progress_bar(duration):
    for i in range(0,101, 5):
        time.sleep(0.1)
        print(f"\rLoading: {i}%", end="")
    print("\nLoading complete!")
    for i in range(0,101, 20):
        time.sleep(0.1)
      
        