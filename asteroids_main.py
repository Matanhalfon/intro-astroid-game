from screen import Screen
# imports all the help we can get from the school file
import sys
# so it could get information from an out sourcing
import ship
# so we could create a ship by out beautiful class
import asteroid as astro
# so we could create asteroids by out beautiful class
import torpedo
# so we could create torpedoes by out beautiful class
import math

# import math module so we could use in math equations to calculate speed,
# distance etc.

SHIP_LIFES = 3
# the DEFULT life for ship in the game, to not change becouse the screen object have only 3
MAX_TORPEDO = 15
# The school max torpedo allowance
DEFAULT_ASTEROIDS_NUM = 5
# a default number of asteroids the school chose for the game to run by
GAME_TABLE = Screen.SCREEN_MAX_X - Screen.SCREEN_MIN_X
# sets our game screen size (1000X1000)
LEFT_TURN = 7
# a default value to add the degree sum for a turn left
BIG_ASTRO_SCORE=20
#the score you get for destroy a big asteroid
MEDIUM_ASTRO_SCORE=50
#the score you get for destroy a medium asteroid
SMALL_ASTRO_SCORE=100
BIG_ASTRO=3
#big asteroid
MEDIUM_ASTRO=2
#medium asteroid
SMALL_ASTRO=1
#small asteroid
#the score you get for destroy a small asteroid
RIGHT_TURN = -7
# a default value to add the degree sum for a turn right
HIT_title = "LOOSER: you've been crashed"
# an encouraging title when you drive your ship poorly into an asteroid
HIT_MAESSAGE = "you not supposed to hit the asteroid you know"
# the showing message when you're doing stuff you're not supposed to...
WIN_TITLE = 'You rock my world!'
# the title you get to see when you actually win the game
WIN_MESSAGE = 'well done NIL ;) \n you blew up all the asteroids'
# the showing message when you win
LOOSE_TITLE = "that's it"
# the title when all your lives run out
LOOSE_MESSAGE = "You've been crashed one too many times"
# the showing message when you run out of lives
QUIT_TITLE = 'Bye Bye'
# the title when you press quit
QUIT_MESSAGE = 'You pressed quit'


# the showing message when you press quit

class GameRunner:
    """ a class that holds all the information a game has when we play"""

    def __init__(self, asteroids_amnt):
        """ starting the game by creating a ship, creating a screen, sets the
         screen size, sets a list with all the moving objects of the user,
         sets a list with all the asteroids we have in the game and a
         starting score and torpedo count of 0 ,ship_life a life count of the ship"""
        ship1 = ship.Ship()
        self._screen = Screen()
        self.screen_max_x = Screen.SCREEN_MAX_X
        self.screen_max_y = Screen.SCREEN_MAX_Y
        self.screen_min_x = Screen.SCREEN_MIN_X
        self.screen_min_y = Screen.SCREEN_MIN_Y
        self.__ship1 = ship1
        self.__obj_list_user = [self.__ship1]
        self.__astro_list = []
        self._astro_amount = asteroids_amnt
        self.__score = 0
        self.__torpedo_count = 0
        self.__ship1_life = SHIP_LIFES

    def init_astroeids(self):
        """ creates asteroid amount we want at the start of the game"""
        avoid_cords = self.__ship1.get_cords
        for i in range(self._astro_amount):
            astroeid = astro.Astroid()
            while astroeid.get_cords == avoid_cords:
                '''The function cheaks if the asteroid have the same cordintes the ship has while Ture the game wil
                 create different asteroid'''
                astroeid = astro.Astroid
            self._screen.register_asteroid(astroeid, astroeid.get_size())
            self.add_to_obj_list(astroeid)

    def run(self):
        """ the function that runs the game by telling other functions what to do"""
        self._do_loop()
        self._screen.start_screen()

    def add_to_obj_list(self, obj):
        """ a function we need to add new objects to our lists"""
        if type(obj) == torpedo.Torpedo:
            # when it's a users object it goes to the users list
            user_list = self.__obj_list_user
            user_list.append(obj)
            self.__obj_list_user = user_list
        if type(obj) == astro.Astroid:
            # when it's an asteroid it goes to the asteroid list
            astro_list = self.__astro_list
            astro_list.append(obj)
            self.__astro_list = astro_list

    def initialize_torpedo(self):
        """ function to create a torpedo with the right information and taking
          care of it's appearance on the screen by calling the functions to
         do so"""
        torpedo1 = torpedo.Torpedo(self.__ship1.get_heading(), self.__ship1.get_cords()[0], self.__ship1.get_cords()[1],
                                   self.__ship1.get_speed()[0], self.__ship1.get_speed()[1])
        if self.__torpedo_count <= MAX_TORPEDO:
            self._screen.register_torpedo(torpedo1)
            self.add_to_obj_list(torpedo1)
            self.__torpedo_count += 1

    def move_obj(self):
        """ a function that hold the mighty formula we calculate with where
         every moving object int the game is going to be next and updates its
         coordinates by the calculations"""
        game_obj_list = self.__astro_list + self.__obj_list_user
        for i in game_obj_list:
            old_cords = i.get_cords()
            speed = i.get_speed()
            new_x = (speed[0] + old_cords[0] - self._screen.SCREEN_MIN_X) % GAME_TABLE + self._screen.SCREEN_MIN_X
            new_y = (speed[1] + old_cords[1] - self._screen.SCREEN_MIN_Y) % GAME_TABLE + self._screen.SCREEN_MIN_Y
            i.set_cords((new_x, new_y))

    def split_asteroid(self, org_asteroid, torpedo):
        """ function to calculate and create new asteroids after one got hit
        by a torpedo, it takes in the asteroid that got hit, the hitting
         torpedo and uses their information to create two new asteroids
         smaller by size and with different speed and coordinate according
         to the information from the above making sure its get on the
         screen instead of the one got hit"""
        org_cord = org_asteroid.get_cords()
        astro_speed = org_asteroid.get_speed()
        size = org_asteroid.get_size()
        new_size = size - 1
        torpedo_speed = torpedo.get_speed()
        new_speed_x = (torpedo_speed[0] + astro_speed[0]) / (math.sqrt(math.pow(astro_speed[0], 2) + \
                                                                       math.pow(astro_speed[1], 2)))
        new_speed_y = (torpedo_speed[1] + astro_speed[1]) / (math.sqrt(math.pow(astro_speed[0], 2) + \
                                                                       math.pow(astro_speed[1], 2)))
        astro_1_speed = (new_speed_x, new_speed_y)
        astro_2_speed = (-new_speed_x, -new_speed_y)
        asteroide1 = self.set_asteroid(astro_1_speed, org_cord, new_size)
        asteroide2 = self.set_asteroid(astro_2_speed, org_cord, new_size)
        self.add_to_obj_list(asteroide1)
        self._screen.register_asteroid(asteroide1, new_size)
        self.add_to_obj_list(asteroide2)
        self._screen.register_asteroid(asteroide2, new_size)

    def set_asteroid(self, speed, cords, size):
        """ gets speed, start coordinates and size to create a new asteroid
         and return one with that information"""
        astroied1 = astro.Astroid(size)
        astroied1.set_cords(cords)
        astroied1.set_speed(speed)
        return astroied1

    def remove_torpedo(self, torpedo):
        """ a function to remove a torpedo from the screen"""
        torpedo_list = self.__obj_list_user
        torpedo_list.remove(torpedo)
        self.__obj_list_user = torpedo_list
        self._screen.unregister_torpedo(torpedo)
        self.__torpedo_count -= 1

    def remove_asteroid(self, asteroide):
        """ a function to remove an asteroid from the screen"""
        astro_list = self.__astro_list
        astro_list.remove(asteroide)
        self.__astro_list = astro_list
        self._screen.unregister_asteroid(asteroide)

    def is_collide(self):
        """ checks for every asteroid if some user object (ship/torpedo) is
         close enough, if it is it acts accordingly, if we remove an asteroid we "cut" the function by
          return True so we wont run over a list that we just remove somthing from"""
        for i in self.__astro_list:
            for j in self.__obj_list_user:
                if i.has_intersection(j):
                    if type(j) == ship.Ship:
                        # a ship has collided so we're going to tell the
                        # user he sucks, remove a ship life, remove the
                        # asteroid it crashed on and let him start again
                        # with the relaxing speed of no speed
                        self._screen.show_message(HIT_title, HIT_MAESSAGE)
                        self._screen.remove_life()
                        self.remove_asteroid(i)
                        self.__ship1_life -= 1
                        j.set_speed((0, 0))
                        return True
                    elif type(j) == torpedo.Torpedo:
                        # a torpedo had hit his target so if the target was
                        # an asteroid larger than 1 it would call a function
                        #  to create two smaller one and remove the one got
                        # hit. if it is a size 1 asteroid it would vanish
                        # with no trace
                        size = i.get_size()
                        if size > 1:
                            self.split_asteroid(i, j)
                            self.remove_asteroid(i)
                            self.score_count(size)
                        else:
                            self.__astro_list.remove(i)
                            self._screen.unregister_asteroid(i)
                            self.score_count(size)
                        self.remove_torpedo(j)
                        return True

    def drew_obj(self):
        """ a function that drawing all the objects to the screen by their
         coordinates"""
        game_obj_list = self.__astro_list + self.__obj_list_user
        self._screen.draw_ship(self.__ship1.get_cords()[0], self.__ship1.get_cords()[1], \
                               self.__ship1.get_heading())
        for i in game_obj_list:
            if type(i) == torpedo.Torpedo:
                if i.get_life_span() > 1:
                    self._screen.draw_torpedo(i, i.get_cords()[0], i.get_cords()[1], i.get_heading())
                    i.decrase_time_span()
                else:
                    self.remove_torpedo(i)
            elif type(i) == astro.Astroid:
                self._screen.draw_asteroid(i, i.get_cords()[0], i.get_cords()[1])

    def _do_loop(self):
        """The function do the game_loop(get the user input,move the objects cheaks for coliisens,drew the game
        and cheaks if the game is finished) and than update the screen"""
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self._screen.update()
        self._screen.ontimer(self._do_loop, 5)

    def _game_loop(self):
        """this function is a single round after initializing the game it
        check for users key press than moves stuff according to the
        information it has checking to see if something got hit and than
        drawing the current situation at the end of the loop"""
        self.get_keyboard(self.__ship1)
        #get user input
        self.move_obj()
        #move all the game objects
        self.is_collide()
        #cheaks if somthing intresting has happend
        self.drew_obj()
        #draw all the game objects
        self.check_if_done()
        #cheaks if the game is finished

    def get_keyboard(self, ship):
        """if a key was pressed it identify's it and update what is needed
        else it passes"""
        if self._screen.is_left_pressed():
            ship.set_heading(LEFT_TURN)
        elif self._screen.is_right_pressed():
            ship.set_heading(RIGHT_TURN)
        elif self._screen.is_up_pressed():
            ship.acelerator()
        elif self._screen.is_space_pressed():
            self.initialize_torpedo()
        else:
            pass

    def score_count(self, size):
        """A function that set the score accordingly  to the asteroid you vanished so you know you are
        awesome"""
        if size == BIG_ASTRO:
            self.__score += BIG_ASTRO_SCORE
            self._screen.set_score(self.__score)
        elif size == MEDIUM_ASTRO:
            self.__score += MEDIUM_ASTRO_SCORE
            self._screen.set_score(self.__score)
        elif size ==SMALL_ASTRO:
            self.__score += SMALL_ASTRO_SCORE
            self._screen.set_score(self.__score)

    def check_if_done(self):
        """the function cheaks if the game is over for some reason"""
        if len(self.__astro_list) == 0:
            self._screen.show_message(WIN_TITLE, WIN_MESSAGE)
            self._screen.end_game()
        elif self.__ship1_life == 0:
            self._screen.show_message(LOOSE_TITLE, LOOSE_MESSAGE)
            self._screen.end_game()
        elif self._screen.should_end():
            self._screen.show_message(QUIT_TITLE, QUIT_MESSAGE)
            self._screen.end_game()


def main(amnt):
    """a function that takes in the amount of asteroids we want and create a game by it and tuns it"""
    runner = GameRunner(amnt)
    runner.init_astroeids()
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
