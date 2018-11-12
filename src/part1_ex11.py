from board_driver_simulator_v2 import open,close,but,pot,det,led
import time

"""
11. Program z poprzedniego punktu stosunkowo wolno reaguje na przyciski. 
Przyczyną jest stosunkowo długi czas wykonania funkcji but(). 
Zmodyfikować program tak aby wywoływał funkcję but() tylko raz na jeden obrót pętli. 
Jak modyfikacja skróciła reakcji programu na naciśnięcie przycisku?
"""

try:
    open()

    while(True):
        state=but()
        if state == 1:
            led(int('1', 16))
        if state == 2:
            led(int('3', 16))
        if state == 4:
            led(int('7', 16))
        if state == 8:
            led(int('f', 16))
        if state == 0:
            led(int('0', 16))
finally:
    close()
