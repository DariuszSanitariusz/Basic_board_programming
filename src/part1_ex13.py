from board_driver_simulator_v2 import open,close,but,pot,det,led
import time

"""
13. Program pozwalający na ustawianie potencjometrem pozycji punktu świetlnego. Wykorzystać cały zakres potencjometru. 
"""

try:
    open()

    while(True):
        val = int(pot()//250)
        if val==0:
            led(1)
        if val==1:
            led(2)
        if val==2:
            led(4)
        if val==3 or val==4:
            led(8)
finally:
    close()
