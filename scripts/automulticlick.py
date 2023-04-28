import pyautogui
import threading
import time
import keyboard

# Define a function that simulates a mouse click at a given location with a given time interval
def click_location_with_interval(location, interval):
    time.sleep(interval)
    pyautogui.moveTo(location[0], location[1])
    pyautogui.click()

# Define a list of target locations and time intervals
locations_and_intervals = [((100, 100), 1), ((200, 200), 2), ((300, 300), 0.5), ((400, 400), 1.5), ((500, 500), 0.5)]

# Loop indefinitely until the "q" key is pressed
while True:
    # Loop through the list of target locations and time intervals, and create a thread for each location
    threads = []
    for location, interval in locations_and_intervals:
        thread = threading.Thread(target=click_location_with_interval, args=[location, interval])
        threads.append(thread)

    # Start all the threads
    for thread in threads:
        thread.start()

    # Wait for all the threads to finish
    for thread in threads:
        thread.join()

    # Check if the "q" key has been pressed, and break out of the loop if it has
    if keyboard.is_pressed('q'):
        break
