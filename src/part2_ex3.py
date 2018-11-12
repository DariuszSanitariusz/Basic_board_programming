from board_driver_simulator_v2 import open,close,but,pot,det,led
import time
"""
3.Funkcja step() przesuwająca punkt świetlny o jeden ‘w górę’ modulo 4. 
Przykład 
step() # 0->1
step() # 1->2
...
step() # 3->0

Test1:
Program przesuwający punkt świetlny
Test 2: 
Program przesuwający punkt świetlny, jeżeli naciśnieto przycisk 0.
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
			
	point=0
	def step():
		global point #zmienna globalna
		set_point(point)
		point=(point+1)%4
		print(point)
			
	while(True): #pętla nieskończona
		if get_key()==0:	#test2
			step()			#test1
finally:
	close()
