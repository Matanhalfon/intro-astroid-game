import random as rand
# import random module so we could choose random numbers for cords,
# speed etc.
import math
# import math module so we could use in math equations to calculate speed,
# distance etc.

SAFETY_SPEED = 10
# faster than these and you'll crap your pants
DEFULT_RADIUS=1
# the ship radius as was given by the school

class Ship():
    """a class holding all the information for an object of type ship. it has
    heading we choose randomly for it to move by on the screen. it holds
    it's coordinates which at the beginning are randomly chosen and than
    changes with the ship movment and tells us where it is at a given
    time. it has the speed value, how fast it moves on the x&y scale which
    at the start of the game is 0 and has a radius value to check for
    coalitions with asteroids"""
    def __init__(self, heading=0):
        """ sets all the information a ship needs to start her life"""
        self.__heading = heading
        self.__x_cord = rand.choice(range(-500, 500))
        self.__y_cord = rand.choice(range(-500, 500))
        self.__x_speed = 0
        self.__y_speed = 0
        self.__radius=DEFULT_RADIUS

    def get_cords(self):
        """ returns a tuple with the x,y coordinates of the ship (x,y)"""
        return (self.__x_cord, self.__y_cord)

    def set_cords(self, new_cords):
        """ lets us set the position of the ship, takes in a tuple (x,y)"""
        self.__y_cord = new_cords[1]
        self.__x_cord = new_cords[0]

    def get_speed(self):
        """ returns a tuple with the numbers value for the speed of the ship
        in x&y scale (x_speed,y_speed)"""
        return (self.__x_speed, self.__y_speed)

    def set_speed(self,speed_tuple):
        """ lets us set speed to the ship, takes in a tuple (x_speed,y_speed)"""
        self.__x_speed=speed_tuple[0]
        self.__y_speed=speed_tuple[1]

    def get_heading(self):
        """ returns a value number of the degrre our ship moves by"""
        return self.__heading

    def set_heading(self, turn_deg):
        """ let us set a degree for the ship to move by, takes in a number"""
        self.__heading += turn_deg

    def get_radius(self):
        """ returns the radius value"""
        return self.__radius

    def acelerator(self):
        """ a function to calculate how much gas to push more for the ship to
        move faster, has a limit so it would not loos control"""
        new_speed_x = self.__x_speed + math.cos(math.radians(self.__heading))
        if new_speed_x>SAFETY_SPEED:
            new_speed_x=SAFETY_SPEED
        self.__x_speed = new_speed_x
        new_speed_y = self.__y_speed + math.sin(math.radians(self.__heading))
        if new_speed_y>SAFETY_SPEED:
            new_speed_y=SAFETY_SPEED
        self.__y_speed = new_speed_y

