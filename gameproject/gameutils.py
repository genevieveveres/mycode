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
      help
    ''')