from board_driver_simulator_v2 import open,close,but,pot,det,led
import time
"""
2.Funkcja get_key(), zwracająca informację o numerze
naciskanego przycisku (0-3).
Jeżeli żaden przycisk nie jest 
naciśniety lub jeżeli naciśnięto więcej przycisków to funkcja 
powinna zwracać wartość ‘-1’.
Test1: program wyświetlający numer naciśnietego przycisku.
Test2: Test z punktu 1. Program zapalający
diodę odpowiadającą naciśnietemu przyciskowi
"""
try:
	open()

	def set_point(position):
		if position==0:
			led(1) #0b0001
		elif position==1:
			led(2) #0b0010
		elif position==2:
			led(4) #0b0100
		elif position==3:
			led(8) #0b1000
		else:
			led(0)

	def get_key():
		key=but()
		if key==1:
			return 0
		elif key==2:
			return 1
		elif key==4:
			return 2
		elif key==8:
			return 3
		else:
			return -1

	while(True): #pętla nieskończona
		k=get_key()
		if k!= -1:   #nie zwraca nic jeżeli nic nie zostało naciśnięte
			print(k) #test1
		set_point(k) #test2
finally:
	close()
