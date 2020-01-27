import math
import random
import time 
import turtle
from Dot import Dot



wn = turtle.Screen()
wn.setup(1100, 1100)
wn.tracer(0)







num = 25

population = []



print("Population Size:", str(num*num))







for i in range(num):
	for z in range(num):
		population.append(Dot())


for i in population:
	i.dot.shapesize(1, 1)








x = -550
y = 500



count = 0
for i in range(num):
	for z in range(num):
		x += 40
		population[count].move_to(x, y)
		population[count].change_color()
		
		count += 1
	wn.update()

	
	y -= 40
	x = -550





des = population[0].dot.distance(population[1].dot)



def iterate(num):

	global count
	if population[num].dead == False:
		checked = population[num].dot

		count = 0

		nearbies = []
		
		
		population[num].change_color()

		
		for i in population:

			other = i.dot
			dis = checked.distance(other)
			if dis <= des:
				nearbies.append(count)

			count += 1

		



		count = 0
		
		if population[num].infected == True:
			
			for x in nearbies:
				if population[x].infected == True:
					nearbies.pop(count)

				count += 1

			for x in nearbies:
				population[x].infect()
				population[x].change_color()

		else:

			for x in nearbies:
				population[x].cure(80)
				if population[x].cured == True:
					population[x].infected == False





	
		



wn.update()
time.sleep(2)




for x in range(1000):
	n = 0
	
	for i in population:
		iterate(n)
		i.cure(80)
		if i.infected == True:
			c = 100/1
			c = round(c)
			if random.randint(0, c) == 1:
				
				i.dead = True
				i.change_color()


		n += 1

		#Uncomment This To See the live action
		'''
		if n % 25 == 0:
			wn.update()
		'''
		



	INS = 0
	ded = 0
	for i in population:
		if i.infected == False:
			INS += 1
		if i.dead == True:
			INS += 1 
			ded += 1




	a = num*num
	if INS > a-1:
		break


	
	
	wn.title(str(a-INS)+" Infected   "+str(INS)+" Not infected   "+str(ded)+" Dead")

	wn.update()

	


ded = 0
for i in population:
	if i.dead == True:
		ded += 1


print(str(ded), "dead")


	



wn.update()


wn.mainloop()
