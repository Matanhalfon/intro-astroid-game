import math
# import math module so we could use in math equations to calculate speed,
# distance etc.

ACCCILRTOR_FACTOR = 2
# A given factor from the school to accelerate by
DEFAULT_ridius = 4
# A given radius from the school to calculate coalition by
DEFAULT_time_span = 200
# A time set for the torpedo to live by, like a butterfly it's beauty can't
# stay here for long


class Torpedo:
    """ A class thats hold all the features of an average torpedo, it has a
     heading which means a degree it moves by, it has a x&y coordinates to
     tell us its location, it has x&y speed to tell us how fast it moves on
      each scale, it has a radius value and its has a life expectancy"""
    def __init__(self, ship_heading, x_cord, y_cord, speed_x, speed_y):
        """ set all the starting information relying on the current ship 
         information who gave birth to it at the time"""
        self.__heading = ship_heading
        self.__x_cord = x_cord
        self.__y_cord = y_cord
        self.__x_speed = speed_x + ACCCILRTOR_FACTOR * math.cos(math.radians(ship_heading))
        self.__y_speed = speed_y + ACCCILRTOR_FACTOR * math.sin((math.radians(ship_heading)))
        self.__radius = DEFAULT_ridius
        self.__time_span = DEFAULT_time_span

    def get_cords(self):
        """ returns a tuple of numbers means the x&y coordinates (x,y)"""
        return (self.__x_cord, self.__y_cord)

    def set_cords(self, new_cords):
        """ lets us set the x,y coordinates by taking in a tuple (x,y)"""
        self.__y_cord = new_cords[1]
        self.__x_cord = new_cords[0]

    def get_speed(self):
        """ returns a tuple of numbers means how fast it moves on each scale
        (x,y)"""    
        return (self.__x_speed, self.__y_speed)

    def get_heading(self):
        """ returns a number means the degree it moves by"""
        return self.__heading

    def get_radius(self):
        """ returns a number which is the radius of the torpedo"""
        return self.__radius

    def decrase_time_span(self):
        """ a function to countdown the torpedo existence"""
        self.__time_span -=1

    def get_life_span(self):
        """ returns how much longer our beloved torpedo has to leave"""
        return self.__time_span
