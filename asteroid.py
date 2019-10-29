import random as rand
# import random module so we could choose random numbers for cords,
# speed etc.
import math
# import math module so we could use in math equations to calculate speed,
# distance etc.
DEFULFET_SIZE=3
SIZE_factor = 10
NORMAL_FACTOR = 5
MAX_SPEED=4
MIN_SPEED=1
# these are the fixed parameters the school gave us to calculate radius for
# asteroid


class Astroid():
    """ this is A class of asteroids and every object in this class holds the
    following information: heading - choose randomly the degree it moves on
    our screen
    x&y coordinates choose randomly at the start and tell us
    where the asteroid is at a given moment
    x&y speed choose randomly for start with and tells us how fast it
    moves on the x and y coordinates
    has a radius value
    has the size of the asteroid"""
    def __init__(self, size=DEFULFET_SIZE):
        """ sets all the starting information for a newborn asteroid"""
        self.__heading = rand.choice(range(0, 360))
        self.__x_cord = rand.choice(range(-500, 500))
        self.__y_cord = rand.choice(range(-500, 500))
        self.__x_speed = rand.choice(range(MIN_SPEED,MAX_SPEED))
        self.__y_speed = rand.choice(range(MIN_SPEED,MAX_SPEED))
        self.__size = size
        self.__radius = self.__size * SIZE_factor - NORMAL_FACTOR

    def get_size(self):
        """ returns a number between 1-3 representing the size of the asteroid"""
        return self.__size

    def get_cords(self):
        """ returns a tuple holds the x,y coordinates in numbers (x,y)"""
        return (self.__x_cord, self.__y_cord)

    def set_cords(self, new_cords):
        """ A class function that lets us change the asteroid position by
        changing its coordinates"""
        self.__y_cord = new_cords[1]
        self.__x_cord = new_cords[0]

    def get_speed(self):
        """ returns a tuple holds the x,y speed in numbers (x,y) how fast it
        moves on each scale"""
        return (self.__x_speed, self.__y_speed)

    def set_speed(self,new_speed):
        """ A class function that lets us set a speed for an existing asteroid"""
        self.__x_speed=new_speed[0]
        self.__y_speed=new_speed[1]

    def set_heading(self, turn_deg):
        """ A class function that lets us change the direction of an existing
        asteroid"""
        self.__heading += turn_deg

    def get_heading(self):
        """ returns a value number representing the degrre our asteroid moves by"""
        return self.__heading

    def get_radius(self):
        """ returns the asteroid radius value in numbers """
        return self.__radius

    def has_intersection(self, obj):
        """ A class functions takes in an object and checks by a given formula
         if it was too close to the asteroid it collided and returns True
        if it did and False if it doesn't"""
        obj_cords=obj.get_cords()
        distance=math.sqrt(math.pow(obj_cords[0]-self.__x_cord,2)+math.pow(obj_cords[1]-self.__y_cord,2))
        combine_radius=self.__radius+obj.get_radius()
        if distance<=combine_radius:
            return True
        else:
            return False
