import pygame
from Dot import Dot
import random
import math
import time


GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
BLUE = (0, 0, 255)

SCREENWIDTH = 370
SCREENHEIGHT = 370

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Plague")

# This will be a list that will contain all the sprites we intend to use in our game.
population = pygame.sprite.Group()

x = 10
y = 10
clock = pygame.time.Clock()
for i in range(35):
    for z in range(35):
        dot = Dot(BLUE, 9, 9)
        dot.x = x
        dot.y = y
        if random.randint(1, 200) == 1:
            dot.infected = True

        dot.update_()
        population.add(dot)





        x += 10


    x = 10
    y += 10
    population.update()
    population.draw(screen)





def get_nearbies(num):
    t = population.sprites()[1]
    ng = population.sprites()[0]
    user = population.sprites()[num]

    x1 = ng.rect.x
    y1 = ng.rect.y

    x2 = t.rect.x
    y2 = t.rect.y

    thres = math.hypot(x1-x2, y1-y2)
    x1 = user.rect.x
    y1 = user.rect.y

    nearbies = []
    if user.infected == True and user.dead == False:
        count = 0

        for dot in population:
            x2 = dot.rect.x
            y2 = dot.rect.y
            dist = math.hypot(x1-x2, y1-y2)

            if dist <= thres:
                nearbies.append(count)

            count += 1

        nearbies.pop(0)
    return nearbies



def update_all():
    infection_chance = 30

    infection_chance = round(100 / infection_chance)
    c = 0
    for dot in population:

        if dot.infected == True:
            if random.randint(0, 100) == 1:
                dot.dead = True
            if random.randint(0, 10) == 1:
                dot.cured = True
                dot.infected = False

        d = get_nearbies(c)

        for i in d:
            if random.randint(0, infection_chance) == 1:
                if population.sprites()[i].cured == False:
                    population.sprites()[i].infected = True

        c += 1

        dot.update_()






update_all()



carryOn = True


while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False



    update_all()







    population.update()


    screen.fill(WHITE)



    population.draw(screen)


    pygame.display.flip()


    clock.tick(60)

pygame.quit()
