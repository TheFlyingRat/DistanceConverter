import sys


class convert:
	class kilometers:
		def distance(speed, time): 
			distance = speed * time
			print(distance)
		
		def speed(distance, time):
			speed = distance / time 
			print(speed)
		
		def time(distance, speed):
			time = distance / speed
			print(time)
		
		def miles(kilometers):
			miles = kilometers / 1.609
			print(miles)
		# pog champion
		
	class miles:
		def distance(speed, time): 
			distance = speed * time
			print(distance)
		
		def speed(distance, time):
			speed = distance / time 
			print(speed)
		
		def time(distance, speed):
			time = distance / speed
			print(time)
		
		def kilometers(miles):
			kilometers = miles * 1.609
			print(kilometers)
		




