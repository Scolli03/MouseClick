import pyautogui
import threading
import keyboard

# Define a function that simulates a mouse click at a given location
def click_location(location):
    pyautogui.moveTo(location[0], location[1])
    pyautogui.click()

# Define a list of target locations and time intervals
locations_and_intervals = [((500, 500), 1), ((500, 600), 2)]

# Define a function that schedules the execution of a mouse click simulation
def schedule_click(location, interval, stop_event):
    while not stop_event.is_set():
        click_location(location)
        stop_event.wait(interval)

# Create an event object to signal all threads to stop
stop_event = threading.Event()

# Create a list to store all threads
threads = []

# Schedule the execution of the mouse click simulation for each target location
for location, interval in locations_and_intervals:
    t = threading.Thread(target=schedule_click, args=(location, interval, stop_event))
    t.start()
    threads.append(t)

# Define a function to stop the program
def stop_program():
    stop_event.set()

# Register the "q" key as a hotkey to stop the program
keyboard.add_hotkey('q', stop_program)

# Wait for all threads to finish
for t in threads:
    t.join()

# Stop the keyboard listener
keyboard.unhook_all()

# Print a message to confirm that the program has stopped
print("Program stopped.")
