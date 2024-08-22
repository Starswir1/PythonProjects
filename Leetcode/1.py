import numpy as np

arrivalTime = 15
delayedTime = 16
arrival = (arrivalTime + delayedTime) % 24
print(arrival)
