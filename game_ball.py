import random
import pygame

# Define Four Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Setting the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

"""
    This is a simple Ball class for respresenting a ball 
    in the game. 
"""


class Ball(object):
    def __init__(self, screen, radius, x, y):
        self.__screen = screen
        self._radius = radius
        self._xLoc = x
        self._yLoc = y
        self.__xVel = 7
        self.__yVel = 2
        w, h = pygame.display.get_surface().get_size()
        self.__width = w
        self.__height = h

    def getXVel(self):
        return self.__xVel

    def getYVel(self):
        return self.__yVel

    def draw(self):
        """
            draws the ball onto screen.
        """
        pygame.draw.circle(screen, (255, 0, 0), (self._xLoc, self._yLoc), self._radius)

    def update(self, paddle, brickwall):
        """
            moves the ball at the screen.
            contains some collision detection.
        """
        self._xLoc += self.__xVel
        self._yLoc += self.__yVel
        # left screen wall bounce
        if self._xLoc <= self._radius:
            self.__xVel *= -1
        # right screen wall bounce
        elif self._xLoc >= self.__width - self._radius:
            self.__xVel *= -1
        # top wall bounce
        if self._yLoc <= self._radius:
            self.__yVel *= -1
        # bottom drop out
        elif self._yLoc >= self.__width - self._radius:
            return True

        # for bouncing off the bricks.
        if brickwall.collide(self):
            self.__yVel *= -1

        # collision detection between ball and paddle
        paddleY = paddle._yLoc
        paddleW = paddle._width
        paddleH = paddle._height
        paddleX = paddle._xLoc
        ballX = self._xLoc
        ballY = self._yLoc

        if ((ballX + self._radius) >= paddleX and ballX <= (paddleX + paddleW)) \
                and ((ballY + self._radius) >= paddleY and ballY <= (paddleY + paddleH)):
            self.__yVel *= -1

        return False

    
ball = Ball(screen, 25, random.randint(1, 700), 250)