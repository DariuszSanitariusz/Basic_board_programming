from board_driver_simulator_v2 import open,close,but,pot,det,led
import time

"""
10. Program zapalający pasek diod. Długość paska zależna od naciśnietego przycisku 
(But0->1000, But1->1100, But2>1110, But3->1111). 
Jeżeli nie będzie naciśnięty żaden przycisk wszystkie diody powinny być zgaszone. 
Użyć zapisu heksadecymalnego. W instrukcji warunkowej użyć wywołania funkcji but() (5 razy) 
"""

try:
    open()

    while(True):
        if but() == 1:
            led(int('1', 16))
        if but() == 2:
            led(int('3', 16))
        if but() == 4:
            led(int('7', 16))
        if but() == 8:
            led(int('f', 16))
        if but() == 0:
            led(int('0', 16))
finally:
    close()
