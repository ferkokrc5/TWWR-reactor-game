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

clear = lambda: os.system('cls')

gamelanguage = str

def reactorstartup():
    cpi = int(100)
    spi = int(100)
    sti = int(100)
    fpa = int(100)

    while True:
        clear()
        tickfreq = random.randint(1,4)
        if tickfreq == 1:
            cpi = cpi - 1
            stype = "c4"
            smsg = str(cpi)
            msgt = "cpi"
        if tickfreq == 2:
            spi = spi - 1
            stype = "c5"
            smsg = str(spi)
            msgt = "spi"
        if tickfreq == 3:
            sti = sti - 1
            stype = "c5"
            smsg = str(sti)
            msgt = "sti"
        if tickfreq == 4:
            fpa = fpa - 1
            stype = "c2"
            smsg = str(fpa)
            msgt = "fpa"
        socket.send_string(f"{stype} {smsg} {msgt}") 
        print(f"Coolant pipe integrity: {cpi}%\nSteam pipe integrity: {spi}%\nSteam turbine integrity: {sti}%\nFuel pellets amount: {fpa}%")
        time.sleep(5)


reactorstartup()

