from Location import Location
from TextUI import TextUI
from item import item
from Negotiator import negotiator
from Enemy import enemy
from Hostage import hostage
import time

"""
    This class is the main class of the "Adventure World" application. 
    'Adventure World' is a very simple, text based adventure game. Users 
    can walk around some scenery. That's all. It should really be extended 
    to make it more interesting!
    
    To play this game, create an instance of this class and call the "play"
    method.

    This main class creates and initialises all the others: it creates all
    rooms, creates the parser and starts the game. It also evaluates and
    executes the commands that the parser returns.
    
    This game is adapted from the 'World of Zuul' by Michael Kolling
    and David J. Barnes. The original was written in Java and has been
    simplified and converted to Python by Kingsley Sage.
"""

class Game:

    def __init__(self):
        """
        Initialises the game.
        """
        self.create_locations()
        self.current_location = self.airport
        self.textUI = TextUI()
        self.negotiator = negotiator((input('Say your Name: ')))
        self.entered_location = []

    print('BEGIN YOUR RESCUE MISSION...')
    time.sleep(0.5)
    print('...')
    time.sleep(0.5)
    print('...')
    time.sleep(1)

    def create_locations(self):
        """
        Sets up all locations.
        :return: None
        """
        self.airport = Location("You have arrived the airport", False, False, False)
        self.defence_academy = Location("in the defence academy", False, False, False)
        self.bandit_den = Location("in a bandit den", True, True, False)
        self.train_station = Location("in a train station... WOW! they left some cash while fleeting", True, False, False)
        self.industrial_zone = Location("in the industrial zone", True, False, False)
        self.prison_facility = Location("in the prison facility... WOW! this map should direct me", True, False, False)
        self.city_center = Location("in the city center", False, False, False)
        self.central_market = Location("in the central market... I must buy a bike as ransom", True, False, False)
        self.bureau_dechange = Location("in the bureau de change... Now let's change currency", True, False, False)
        self.hospital = Location("in the hospital", False, False, False)
        self.central_mosque = Location("in the central mosque", False, False, False)
        self.black_market = Location("in the black market, A key? where could i use this", True, False, False)
        self.check_point = Location("in the check point", False, False, False)
        self.bandit_hideout = Location("in the bandit hideout", True, True, False)
        self.exchange_point = Location("in the exchange_point... GBP needed for ransom", False, False, True)


        """
        Set exits and neighbouring locations
        """
        self.airport.set_exit("west", self.bandit_den)
        self.airport.set_exit("east", self.defence_academy)
        self.airport.set_exit("south", self.train_station)
        self.bandit_den.set_exit("east", self.airport)
        self.defence_academy.set_exit("west", self.airport)
        self.train_station.set_exit("north", self.airport)
        self.defence_academy.set_exit("east", self.city_center)
        self.defence_academy.set_exit("south", self.central_market)
        self.city_center.set_exit("west", self.defence_academy)
        self.central_market.set_exit("north", self.defence_academy)
        self.central_market.set_exit("south", self.central_mosque)
        self.central_market.set_exit("west", self.industrial_zone)
        self.central_mosque.set_exit("north", self.central_market)
        self.industrial_zone.set_exit("east", self.central_market)
        self.city_center.set_exit("east", self.hospital)
        self.city_center.set_exit("north", self.prison_facility)
        self.hospital.set_exit("west", self.city_center)
        self.prison_facility.set_exit("south", self.city_center)
        self.hospital.set_exit("south", self.check_point)
        self.check_point.set_exit("north", self.hospital)
        self.check_point.set_exit("south", self.black_market)
        self.check_point.set_exit("west", self.bandit_hideout)
        self.black_market.set_exit("north", self.check_point)
        self.bandit_hideout.set_exit("east", self.check_point)
        self.central_mosque.set_exit("south", self.bureau_dechange)
        self.central_mosque.set_exit("west", self.exchange_point)
        self.bureau_dechange.set_exit("north", self.central_mosque)
        self.exchange_point.set_exit("east", self.central_mosque)
        self.bureau_dechange.set_exit("west", self.exchange_point)

        """
        Let's add items to each location and their corresponding weights.
        """
        self.airport.addItems(item("phone"))
        self.train_station.addItems(item("bonusCash"))
        self.defence_academy.addItems(item("AK47"))
        self.defence_academy.addItems(item(" "))
        self.defence_academy.addItems(item("knife"))
        self.prison_facility.addItems(item("map"))
        self.hospital.addItems(item("vitamins"))
        self.central_market.addItems(item("bike"))
        self.industrial_zone.addItems(item("bonusCash"))
        self.central_mosque.addItems(item("bonusCash"))
        self.black_market.addItems(item("key"))
        self.bureau_dechange.addItems(item("GBP"))

        """
        Let's add enemies to selected location
        """
        self.black_market.addEnemy(enemy("thief"))
        self.bandit_den.addEnemy(enemy("isis"))
        self.bandit_hideout.addEnemy(enemy("bokoharam"))
        self.prison_facility.addEnemy(enemy("ugm"))
        self.train_station.addEnemy(enemy("heardsmen"))

        """
        Let's add hostage and kidnapper to the exchange location.
        """
        self.exchange_point.addHostage(hostage("kidnapper"))
        self.exchange_point.addHostage(hostage("chibok girls"))


    def play(self):
        """
            The main play loop, runs til playtime is finished.
        :return: None
        """
        if self.negotiator.health > 0:
            self.print_welcome()
            finished = False
            while not finished:  # while (finished == False):
                command = self.textUI.get_command()   # Returns a 2-tuple
                finished = self.process_command(command)
            print("Thank you for playing!")
        else:
            print(f'Game Over')

    def print_welcome(self):
        """
            Displays a welcome message.
        :return:
        """
        time.sleep(0.5)
        self.textUI.print_to_textUI("Touch down. You have arrived heat zone of kidnappers. Stay alert")
        print('...')
        time.sleep(1)
        self.textUI.print_to_textUI("Your current location is Kaduna airport.")
        print('...')
        time.sleep(1)
        self.textUI.print_to_textUI("Use the help command for location details. You may need to make a call to our local agents")
        print('...')
        time.sleep(1)
        self.textUI.print_to_textUI(f'Your command words are: {self.show_command_words()}')

    def show_command_words(self):
        """
            Show a list of available commands.
        :return: None
        """
        return ['help', 'go', 'quit', 'loc_inv', 'dock', 'pick', 'neg_data', 'use']

    def process_command(self, command):
        """
            Process a command from the TextUI.
        :param command: a 2-tuple of the form (command_word, second_word)
        :return: True if the game has been quit, False otherwise
        """
        command_word, second_word = command
        if command_word != None:
            command_word = command_word.upper()

        want_to_quit = False
        if command_word == "HELP":
            self.print_help()
        elif command_word == "GO":
            self.locationStatus = self.do_go_command(second_word)
        elif command_word == "QUIT":
            want_to_quit = True
        elif command_word == "PICK":
            self.pickup(second_word)
        elif command_word == "LOC_INV":
            self.show_loc_inv()
        elif command_word == "DOCK":
            self.current_location.booby_trap = False
            self.textUI.print_to_textUI("Ooch!!! Lost some health, the location is now safe")
            time.sleep(1)
            self.textUI.print_to_textUI(f"You lost a life")
            time.sleep(1)
            self.negotiator.dropHealth()
            self.negotiator.healthStatus()
            self.textUI.print_to_textUI(f'{self.negotiator.showHealth()} out of 5')
            time.sleep(1)
            self.textUI.print_to_textUI(self.current_location.get_long_description())
        elif command_word == "NEG_DATA":
            self.display_negInv()
        elif command_word == "USE":
            self.use_up(second_word)
            self.current_location.rescue_loc = False

        elif command_word == "DROP":
            self.dropOff(second_word)
        else:
            # Unknown command...
            self.textUI.print_to_textUI("Sorry, I Don't know what you mean.")

        return want_to_quit


    def print_help(self):
        """
            Display some useful help text.
        :return: None
        """
        self.textUI.print_to_textUI("You are in a highly terrorized zone. Stay alert!")
        self.textUI.print_to_textUI("...")
        self.textUI.print_to_textUI("around may be in danger of a booby trap, dock.")
        print('...')
        self.textUI.print_to_textUI(f'Your command words are: {self.show_command_words()}.')
        print('...')
        self.textUI.print_to_textUI(self.current_location.get_long_description())

    def display_negInv(self):
        """
        Prints out the items that have been picked up
        :return: None
        """
        self.textUI.print_to_textUI(self.negotiator.show_negotiator_inv())

    def show_loc_inv(self):
        """
        Print out the items in a location
        :return: List of items in a location
        """
        # return self.current_location.locationInv
        self.textUI.print_to_textUI(self.current_location.show_locationInv())

    def do_go_command(self, second_word):
        """
            Performs the GO command.
        :param second_word: the direction the player wishes to travel in
        :return: None
        """
        if second_word == None:
            # Missing second word...
            self.textUI.print_to_textUI("Go where?")
            return

        next_location = self.current_location.get_exit(second_word)
        #if second word inputted by user is unknown
        if next_location == None:
            self.textUI.print_to_textUI("River!, there is no access!")
            time.sleep(1)
            self.textUI.print_to_textUI(self.current_location.get_long_description())
            return

        else:
            self.current_location = next_location
            if self.current_location.booby_trap == True and self.current_location.deadZone == False:
                print(f'Zone is booby trapped, input dock command')

            elif self.current_location.deadZone == True and self.current_location.booby_trap == True:
                print(f'Danger, You just ambushed in the dead zone')
                print(f'Oh no! Better luck nest time')
                time.sleep(1)
                print(f'Game Over')
                time.sleep(1)
                return quit()

            elif self.current_location.rescue_loc == True:
                print('Ransom point, to use ransom item, input use command and second word')

            else:
                self.textUI.print_to_textUI(self.current_location.get_long_description())

    def pickup(self, second_word):
        """Creating the pickup items command"""
        if second_word == None:
            #Missing second word...
            self.textUI.print_to_textUI('I need clear instructions!!! Pick what?')
            return
        else:
            if second_word in self.current_location.locationInv:
                self.negotiator.negotiator_bag.append(second_word)
                self.current_location.locationInv.remove(second_word)
                self.textUI.print_to_textUI(f'You have picked a {second_word}')

    def use_up (self, second_word):
        """
        Use item at the ransom point
        :param second_word: item to be dropped
        return: None
        """
        if second_word == None:
            #Missing second_word...
            self.textUI.print_to_textUI('Use what?')
            return
        else:

            if second_word in self.negotiator.negotiator_bag:
                self.current_location.rescue_loc = False
                self.negotiator.negotiator_bag.remove(second_word)
                self.textUI.print_to_textUI(f'You just used the {second_word} as ransom')
                time.sleep(1)
                self.textUI.print_to_textUI("CONGRATULATION!!! HOSTAGE RESCUED")
                time.sleep(1)
                self.textUI.print_to_textUI(f"Head to the exit with the hostages")
                time.sleep(1)
                self.textUI.print_to_textUI("YOU WIN")
                quit()
                return
            else:
                self.textUI.print_to_textUI(self.current_location.get_long_description())

    def dropOff (self, second_word):
        """
        Drop off item at the ransom point
        :param second_word: item to be dropped
        return: None
        """
        if second_word == None:
            #Missing second_word...
            self.textUI.print_to_textUI('Drop what?')
            return
        else:
            if second_word in self.negotiator.negotiator_bag:
                self.negotiator.negotiator_bag.remove(second_word)
                self.current_location.locationInv.append(second_word)
                self.textUI.print_to_textUI(f'You just dropped {second_word}')

    def already_accessed(self):
        """
        Already explored locations
        :return: None
        """
        if self.current_location not in self .entered_location:
            self.entered_location.append(self.current_location)
        else:
            self.textUI.print_to_textUI("Already accessed this location")

def main():
    game = Game()
    game.play()

if __name__ == "__main__":
    main()
