import pygame
import sys

fallspeed = 1.0000000000
size = width, height = 1800, 900
black = 0, 0, 0
screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	speed = [0, fallspeed]

	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
	if ballrect.bottom > height and fallspeed != 0:
		fallspeed = (fallspeed - (fallspeed * .1)) * -1

	newfallspeed = fallspeed + .19

	if (newfallspeed - fallspeed < 0):
		newfallspeed = 0

	fallspeed = newfallspeed

	screen.fill(black)
	screen.blit(ball, ballrect)
	pygame.display.flip()

	print fallspeed
