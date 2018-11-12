from board_driver_simulator_v2 import open,close,but,pot,det,led
import time

"""
7. Program wyświetlający na ekranie stan przycisków (w postaci dziesiętnej). 
Działanie programu sprawdzić naciskając przycisk 0 potem 3 a następnie jednocześnie 0 i 3. 
"""

try:
    open()

    led(0)
    while(True):
        print (but())

finally:
    close()
