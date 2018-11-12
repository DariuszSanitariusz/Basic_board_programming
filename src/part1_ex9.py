from board_driver_simulator_v2 import open,close,but,pot,det,led
import time

"""
9. Program ‘zapalający’ diodę 2 (i tylko 2) tylko w momencie naciśnięcia przycisku 3 
(w przeciwnym razie dioda ma być zgaszona). Pozostałe przyciski mają pozostać nieaktywne.
"""

try:
    open()

    while(True):
        state=but()
        if state==4:
            led(2)
        else:
            led(0)
finally:
    close()
