import random
import time
import os
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

# stype = input("stype:")
# smsg = input("msg:")
# socket.send_string(f"{stype} {smsg}") 

gamelanguage = str

def reactorstartup():
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
            stype = "c4"
            smsg = "cpi" + {cpi}
        if tickfreq == 2:
            spi = spi - 1
            stype = "c5"
            smsg = "spi" + {spi}
        if tickfreq == 3:
            sti = sti - 1
            stype = "c5"
            smsg = "sti" + {sti}
        if tickfreq == 4:
            fpa = fpa - 1
            stype = "c2"
            smsg = "fpa" + {fpa}
        socket.send_string(f"{stype} {smsg}") 
        print(f"Coolant pipe integrity: {cpi}%\nSteam pipe integrity: {spi}%\nSteam turbine integrity: {sti}%\nFuel pellets amount: {fpa}%")
        time.sleep(5)

