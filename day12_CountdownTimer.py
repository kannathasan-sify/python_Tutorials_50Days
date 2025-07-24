import time

def coundownNumber():
    # Countdown from 10 to 0
    for i in range(10, -1, -1):
        print(i)
        time.sleep(1)

if __name__ == "__main__":
    coundownNumber()
