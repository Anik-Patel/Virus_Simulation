import numpy as np
import math
import random
import time 
import turtle
from fractions import Fraction




infection_chance = 1
infection_chance = 100/infection_chance




singular_infection_chance = 1
singular_infection_chance = 100/infection_chance

curing_chance = 100
curing_chance = 100/curing_chance



class Dot():
	def __init__(self):

		self.infected = False
		self.cured = False
		self.dead = False

		
		if random.randint(0, round(infection_chance)) == 1:
			self.infected = True
			
		else:
			self.infected = False
		
		


		self.dot = turtle.Turtle()
		self.dot.speed(0)
		self.dot.color('black')
		self.dot.shape('circle')
		self.dot.up()

	def change_color(self):
		if self.dead == False:
			if self.infected == False:
				self.dot.color('blue')

			if self.infected == True:
				self.dot.color('red')



		if self.dead == True:
			self.dot.color('black')



		



	def move_to(self, x, y):
		self.dot.goto(x, y)


	def infect(self):
		if self.dead == False:
			if self.cured == False:
				if random.randint(0, singular_infection_chance) == 1:
					self.infected = True


	def cure(self, chance):
		if self.dead == False:

			if random.randint(0, chance) == 1:
				self.infected = False
				self.cured = True
			
		



