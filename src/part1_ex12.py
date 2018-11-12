from board_driver_simulator_v2 import open,close,but,pot,det,led
import time

"""
12. Program wyświetlający na ekranie stan potencjometru (w kodzie dziesiętnym). 
Działanie programu sprawdzić obracając potencjometrem. 
"""

try:
    open()

    while(True):
        print(bin(pot()))
finally:
    close()
