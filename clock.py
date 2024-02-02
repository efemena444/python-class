import datetime
import time

def display_clock():
    while True:
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%H:%M:%S")
        print("Current time:", formatted_time)
        time.sleep(1)

# Start the clock
display_clock()

