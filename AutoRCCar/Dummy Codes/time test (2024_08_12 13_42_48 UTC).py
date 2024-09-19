import time

# Print current time
print("Current time:", time.strftime("%Y-%m-%d %H:%M:%S"))

# Pause for 2 seconds
print("Pausing for 2 seconds...")
time.sleep(2)
print("New time:", time.strftime("%Y-%m-%d %H:%M:%S"))
print("Resuming after pause")
