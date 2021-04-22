from time import sleep
i = 0
while True:
    try:
        print(str(i) + " seconds have passed since you started this stupid loop.")
        i=i+1
        sleep(1)
    except KeyboardInterrupt:
        break

