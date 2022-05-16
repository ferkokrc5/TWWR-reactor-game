import random
import time
import os

cpi = int(100)
spi = int(100)
sti = int(100)
fpa = int(100)

clear = lambda: os.system('cls')

while True:
    clear()
    tickfreq = random.randint(1,4)
    if tickfreq == 1:
        cpi = cpi - 1
    if tickfreq == 2:
        spi = spi - 1
    if tickfreq == 3:
        sti = sti - 1
    if tickfreq == 4:
        fpa = fpa - 1
    print(f"Coolant pipe integrity: {cpi}%\nSteam pipe integrity: {spi}%\nSteam turbine integrity: {sti}%\nFuel pellets amount: {fpa}%")
    time.sleep(5)

