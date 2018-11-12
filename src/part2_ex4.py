from board_driver_simulator_v2 import open, close, but, pot, det, led
import time

"""
4. Modyfikacja funkcji step pozwalająca na określenie kierunku przesunięcia:
step(‘right’) # 0->1
step(‘right’) # 1->2
step(‘left’) # 2->1
step(‘left’) # 1->0
Test 1: Program: obracający krążkiem w lewo jeżeli naciśnieto przycisk ‘0’ a w prawo jeśli naciśnieto przycisk ‘1’

"""
try:
    open()


    def set_point(position):
        if position == 0:
            led(1)  # 0b0001
        elif position == 1:
            led(2)  # 0b0010
        elif position == 2:
            led(4)  # 0b0100
        elif position == 3:
            led(8)  # 0b1000
        else:
            led(0)


    def get_key():
        key = but()
        if key == 1:
            return 0
        elif key == 2:
            return 1
        elif key == 4:
            return 2
        elif key == 8:
            return 3
        else:
            return -1


    point = 0


    def step(direction):
        global point  # zmienna globalna
        if direction == 'right':
            point += 1
        elif direction == 'left':
            point -= 1
        point = point % 4
        set_point(point)


    while (True):  # pętla nieskończona
        k = get_key()
        if k != -1:
            print("Naciśnięto przycisk nr: ", k)
            if k == 0:
                step('left')
            elif k == 1:
                step('right')
finally:
    close()
