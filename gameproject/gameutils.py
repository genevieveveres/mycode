# Utility functions to display information to the player

def gameOpening():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    Spooky Scary Ghost Game
    ========
    In this world, it's exorcise or be 
    exorcised.... from this world
    ========
    Commands:
      go [up | down | north | south | east | west]
      get [item]
      inventory
      help
    ''')

def showHelp():
    print('''
    Commands:
      go [up | down | north | south | east | west]
      get [item]
      use [item]
      inventory
      help (this screen)
      spoil (directions to win)
    ''')

def spoilers():
    print('''
    To win the game in as few moves as possible, enter the following:
      -go up
      -get tome
      -go east
      -go south
      -get candles
      -go down
      -go north
      -go north
      -go west
      -go down
      -go north
      -get knife
      -go east
    The above commands must be entered in order from the starting point of the game. 
    ''')