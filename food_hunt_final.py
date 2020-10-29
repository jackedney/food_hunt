###############################################################################################
#                                          FOOD HUNT                                          #
###############################################################################################

"""
            Welcome to Food Hunt, a text based RPG adventure written in python
                                                                                            """

###############################################################################################
#                                          PACKAGES                                           #
###############################################################################################

# Import packages needed
import random
from time import sleep
import sys


###############################################################################################
#                                           GRAPHICS                                          #
###############################################################################################

# typewriter style print
def print_t(txt):
    for x in txt:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.05)

# faster version - for dialogue and options
def print_tf(txt):
    for x in txt:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.025)

# even faster version
def print_tff(txt):
    for x in txt:
        print(x, end='')
        sys.stdout.flush()

# ASCII images

foodhunt_ascii = """

███████╗ ██████╗  ██████╗ ██████╗     ██╗  ██╗██╗   ██╗███╗   ██╗████████╗
██╔════╝██╔═══██╗██╔═══██╗██╔══██╗    ██║  ██║██║   ██║████╗  ██║╚══██╔══╝
█████╗  ██║   ██║██║   ██║██║  ██║    ███████║██║   ██║██╔██╗ ██║   ██║   
██╔══╝  ██║   ██║██║   ██║██║  ██║    ██╔══██║██║   ██║██║╚██╗██║   ██║   
██║     ╚██████╔╝╚██████╔╝██████╔╝    ██║  ██║╚██████╔╝██║ ╚████║   ██║   
╚═╝      ╚═════╝  ╚═════╝ ╚═════╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   

"""

knight_ascii = r"""

      ++          {}
 / \  ||         .--.
|| ||=|==>      /.--.\
 \ /` ||        |====|
      ||        |\::/|
      ||    .-|`\..../|__.-^-.__
     /\\/  /  |...::..|`   :   `|
     |:'\ |  //'''::''|   .:.   |
      \ /\|-//\   ::  |..:::::..|
      |\ <` >  >._::_.| ':::::' |
      ||`''`  /.  ^^  |   ':'   |
      ||      |:      \    :    /
      ||      |:  ::   \   :   /
      ||      |___/\___|`-.:.-`
      ||       \__||__/    `
      ||       <_.><._>
      ||       |  ||  |
      ||       |  ||  |
      ||      _\.:||:./_
      ||     (____/\____)"""

beheaded_ascii = """
███   ▄███▄    ▄  █ ▄███▄   ██   ██▄   ▄███▄   ██▄   
█  █  █▀   ▀  █   █ █▀   ▀  █ █  █  █  █▀   ▀  █  █  
█ ▀ ▄ ██▄▄    ██▀▀█ ██▄▄    █▄▄█ █   █ ██▄▄    █   █ 
█  ▄▀ █▄   ▄▀ █   █ █▄   ▄▀ █  █ █  █  █▄   ▄▀ █  █  
███   ▀███▀      █  ▀███▀      █ ███▀  ▀███▀   ███▀  
                ▀             █                      
                             ▀                       """

murdered_ascii = """
█▀▄▀█   ▄   █▄▄▄▄ ██▄   ▄███▄   █▄▄▄▄ ▄███▄   ██▄   
█ █ █    █  █  ▄▀ █  █  █▀   ▀  █  ▄▀ █▀   ▀  █  █  
█ ▄ █ █   █ █▀▀▌  █   █ ██▄▄    █▀▀▌  ██▄▄    █   █ 
█   █ █   █ █  █  █  █  █▄   ▄▀ █  █  █▄   ▄▀ █  █  
   █  █▄ ▄█   █   ███▀  ▀███▀     █   ▀███▀   ███▀  
  ▀    ▀▀▀   ▀                   ▀                  
                                                    """

eaten_ascii = """
▄███▄   ██     ▄▄▄▄▀ ▄███▄      ▄   
█▀   ▀  █ █ ▀▀▀ █    █▀   ▀      █  
██▄▄    █▄▄█    █    ██▄▄    ██   █ 
█▄   ▄▀ █  █   █     █▄   ▄▀ █ █  █ 
▀███▀      █  ▀      ▀███▀   █  █ █ 
          █                  █   ██ 
         ▀                          """

impaled_ascii = """
▄█ █▀▄▀█ █ ▄▄  ██   █     ▄███▄   ██▄   
██ █ █ █ █   █ █ █  █     █▀   ▀  █  █  
██ █ ▄ █ █▀▀▀  █▄▄█ █     ██▄▄    █   █ 
▐█ █   █ █     █  █ ███▄  █▄   ▄▀ █  █  
 ▐    █   █       █     ▀ ▀███▀   ███▀  
     ▀     ▀     █                      
                ▀                       """

liquified_ascii = """
█    ▄█  ▄▄ █    ▄   ▄█ ▄████  ▄█ ▄███▄   ██▄   
█    ██ █   █     █  ██ █▀   ▀ ██ █▀   ▀  █  █  
█    ██  ▀▀▀█  █   █ ██ █▀▀    ██ ██▄▄    █   █ 
███▄ ▐█     █  █   █ ▐█ █      ▐█ █▄   ▄▀ █  █  
    ▀ ▐      █ █▄ ▄█  ▐  █      ▐ ▀███▀   ███▀  
              ▀ ▀▀▀       ▀                     
                                               """

queen_ascii = r"""
        w*W*W*W*w
         \"."."/
         _/___\_
        ( /_ _\ )
        (*\ - /*) 
        .-~'='~-.
       /`~`"Y"`~`\
      / /(_ * _)\ \
     / /  )   (  \ \
     \ \_/\\_//\_/ / 
      \/_) '*' (_\/
        |       |
        |       |
        |       |
        |       |
        |       |
        |       |
        |       |
        |       |
        w*W*W*W*w"""

soup_ascii = r"""
    (\
     \ \
 __    \/ ___,.-------..__        __
//\\ _,-'\\               `'--._ //\\
\\ ;'      \\                   `: //
 `(          \\                   )'
   :.          \\,----,         ,;
    `.`--.___   (    /  ___.--','
      `.     ``-----'-''     ,'
         -.               ,-
            `-._______.-'
            
"""

castle_ascii = r"""
                      .---.                  .---.
                      |  .'                  |  .'
                      |-'                    |-'
                      |                      |
                    .---.                  .---.
                   (:::::)________________(:::::)
                   / \/ \/ \/ \/ \/ \/ \/ \/ \/ \
       __         /(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)\         __
      (  ) _.-.  /''''''''''''''''''''''''''''''''\       (  ) _.-.
       ||-|    `-._                                \       ||-|    `.
       || |        `.                               \      || |      `.
       ||-|_.-`-._   `.                              \     ||-|_.-`.   `.
       ||    /  .'`-. .'                              \    ||     .'`-. .'
       ||   /.-'  _.-'                                 \   ||  .-'  _.-'
       ||  /`._.-'                                      \  || `._.-'
       || /                                              \ ||
      //\\                                                //\\
     //  \\                                              //  \\
    // /\ \\                                            // /\ \\
   // /  \ \\                                          // /  \ \\
  // / /\ \ \\                                        // / /\ \ \\
 /_|_|/__\_\_\\                                      /_|_|/__\|_|_\
/ _   _   _   _\____________________________________/  _   _   _   \
|| |_| |_| |_| |------------------------------------|_| |_| |_| |_||
|______________|[=][=][=][=][=][=][=][=][=][=][=][=]|______________|
|--------------|____________________________________|--------------|
|   _______    |------------------------------------|    _______   |
|  |   _   |   |     |           .-.           /    |   |   _   |  |
|  |.'* *'.|   |     \     _..--('[|)-..__     |    |   |.'* *'.|  |
|  |'. * .'|   |      |_.-'   .-'/'\'-.   '-._/     |   |'. * .'|  |
|  '. )_( .'   |      /   _.-' .'   '. '-._   \     |   '. )_( .'  |
|    '._.'     |     /_.-' _.-'       '-._ '-._\    |     '._.'    |
|______________|     |_.--'               '--._|    |______________|
|-.   .--.   .-|    /'                         '\ ' |-.   .--.   .-|
|  \ /    \ /  |  | |      ________________    .' | |  \ /    \ /  |
| * v *  * v * | || '.    | |'|'|'|'|'|'|'|    | || | * v *  * v * |
|   *      *   | || ||    | | | | | | | | |    | || |   *      *   |
|              ||   ||    | | | | | | | | |    | || |              |
|              ||  | |    | | | | | | | | |    || | |              |
[=][=][==][=][=]'. ' |    | | | | | | | | |   | ' `.[=][=][==][=][=]
|              | | | |    | | | | | | | | |   | |  ||              |
|              | | | |    | | | | | | | | |   | |  ||              |
|              ||  \  \   | | | | | | | | |  /  /  ||              |
|      *       |'.   '/___|_V_V_V_V_V_V_V_|__\'    `|       *      |
[=][=][==][=][=] '    \----------------------/    / [=][=][==][=][=]
|      *       |  '.  |                      |  .`  |       *      |
|              |   .`-`                      `-`.   |              |
|              | `:\                            /:` |              |
|              | ' .`                          `. ' |              |
|              |--`                              `--|              |
`--...____...--'                                    `--...____...--'
"""


cottage_ascii = r"""
                          (   )
                          (    )
                           (    )
                          (    )
                            )  )
                           (  (                  /\\
                            (_)                 /  \  /\\
                    ________[_]________      /\/    \/  \\
           /\      /\        ______    \    /   /\/\  /\/\\
          /  \    //_\       \    /\    \  /\/\/    \/    \\
   /\    / /\/\  //___\       \__/  \    \/
  /  \  /\/    \//_____\       \ |[]|     \\
 /\/\/\/       //_______\       \|__|      \\
/      \      /XXXXXXXXXX\                  \\
        \    /_I_II  I__I_\__________________\\
               I_I|  I__I_____[]_|_[]_____I
               I_II  I__I_____[]_|_[]_____I
               I II__I  I     XXXXXXX     I
            ~~~~~"   "~~~~~~~~~~~~~~~~~~~~~~~~
"""



bridge_ascii = r"""
 ______________________________________________________
   [[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]
   .-.`| `-/-.__/.-'\_.-._,'/`-._'\_.-._`-'_/-._.'|/.-'\-
   \_.-`./`-._'\__.-`-.__.-`--._/--.`-._\`-._\__.-)`-'._/
   `._-'.\_.---._-.\_`-..`\_.---._`-.__.-`'._.--./`-'._,'
   __/`.-/       `.'_`./`.'       '.\__.-`.'    (_.-\_,-.
   `._-/'          |._.-|           |.'`.|       `(_.`-._
   .-',`)          | /`.|           |`-/`|         ;.-'_/
   `\,-/           |\.-'|           |\-'`|          ;\_,-
    -./`._        [[[[[[[[         [[[[[[[[         .',-'
    `.`--.~~-^_~-/.`-._`-.\^~-_~-^/`-.'-,.'\^~-~_^"'`-.'_
    -,.'"-"~^-~_~- - - _- -~^-_.~ - -_ - - -~- . "'"-"-""
    ""-'"-""-"~- _~.^-~-^.-^_.- .^~.-  ~-. ~^_-""-""-"'-"
        ""-'"-"    ~- ^. - ~ -~^ - ~  ^~- ~     ""-"'-'
"""

mountains_ascii = r'''
                                /^L_      ,."\
           /~\       __       /~    \   ./    \
          /   _\   _/  \     /T~\|~\_\ / \_  /~|          _^
        / \ /W  \ / V^\/X  /~         T  . \/   \    ,v-./
 ,'`-. /~   ^     H  ,  . \/    ;   .   \      `. \-'   /
     M      ~     | . ;  /         ,  _   :  .    ~\_,-'
    /    ~    .    \    /   :                   '   \   ,/`
   I o. ^    oP     '98b         -      _  9.`       `\9b.
 8oO888.  oO888P  d888b9bo. .8o 888o.       8bo.  o     988o.
 88888888888888888888888888bo.98888888bo.    98888bo. .d888P
 88888888888888888888888888888888888888888888888888888888888
 88888888888888P"   "" "   """9888P" P" "8P"   ""*9888888888
 '''


cave_ascii = r"""
                    /   \              /'\       _                              
_ ..           /'.,/     \_         .,'   \     / \_                            
    \         /            \      _/       \_  /    \     _                     
     \__,.   /              \    /           \/.,   _|  _/ \                    
          \_/                \  /',.,''\      \_ \_/  \/    \                   
                           _  \/   /    ',../',.\    _/      \                  
             /           _/%\  \  /    |         \  /.,/'\   _\                 
           _/           /██%%\  \_     |          \/      \_/  \                
          /      \     |█████%|   \__   \          \_       \   \_              
                  \   /██████%|      \   \           \       \    \             
                   \  |██████%%\      \___            \_      \_   \            
                    \|████████%%|____.'  /\_            \       \   \_          
                    /'.,___________...,,'   \            \   \        \         
                   /       \          |      \    |__     \   \_       \        
                   """

market_ascii = r"""
                                                                      
                   _                      _                             
    ____________ .' '.    _____/----/-\ .' './========\    / \               
   //// ////// /V_.-._\  |.-.-.|===| _ |-----| u    u |   /___\              
  // /// // ///==\ u |.  || | ||===||||| |T| |   ||   | ..| u |_ _ _ _ _ _   
 ///////-\////====\==|::::::::::::::::::::::::::::::::::::|u u| U U U U U    
 |----/\u |--|++++|..|       _____ :::::::::::: _____  O  |+++|+-+-+-+-+-+   
 |u u|u | |u ||||||..|   O  /=}}=/| '::::::::' |\ %X:\=|  |===|>=== _ _ ==   
 |===|  |u|==|++++|==|   |</..../   .::::::::.   \ ,P \M  | T |....| V |..   
 |u u|u | |u ||HH||      M/ "L /    ::::::::::.   \  8 \                     
 |===|_.|u|_.|+HH+|      /____/    ::::::::::::.   \____\                 
                ________ |    |   .::::::::::::.   |    | ________          
---------------/       /|       .:::::;;;:::;;:::.       |\       \-------  
______________/_______/ |      .::::::;;:::::;;:::.      | \_______\________
|       |     [===  =] /|     .:::::;;;::::::;;;:::.     |\ [==  = ]   |    
|_______|_____[ = == ]/ |    .:::::;;;:::::::;;;::::.    | \[ ===  ]___|____
     |       |[  === ] /|   .:::::;;;::::::::;;;:::::.   |\ [=  ===] |      
_____|_______|[== = =]/ |  .:::::;;;::::::::::;;;:::::.  | \[ ==  =]_|______
 |       |    [ == = ] /| .::::::;;:::::::::::;;;::::::. |\ [== == ]      | 
_|_______|____[=  == ]/ |.::::::;;:::::::::::::;;;::::::.| \[  === ]______|_
   |       |  [ === =] /.::::::;;::::::::::::::;;;:::::::.\ [===  =]   |    
___|_______|__[ == ==]/.::::::;;;:::::::::::::::;;;:::::::.\[=  == ]___|_____
"""

woods_ascii = r"""
                                                   
                  _                                            
                 /;-._,-.____        ,-----.__                      
                (_:#::_.:::. `-._   /:, /-._, `._,             
                    \   _|`"=:_::.`.);  \ __/ /                     
                      ,    `./  \:. `.   )==-'                 
           ., ,-=-.  ,\, +#./`   \:.  / /                      
            \/:/`-' , ,\ '` ` `   ): , /_  -o                  
            /:+- - + +- : :- + + -:'  /(o-) \)                 
         ,=':  \    ` `/` ' , , ,:' `'--".--"---._/`7          
        (    \: \,-._` ` + '\, ,"   _,--._,---":.__/           
              \:  `  X` _| _,\/'   .-'                         
                ":._:`\____  /:'  /                            
                    \::.  :\/:'  /                             
                     `.:.  /:'  }                              
                       ):_(:;   \                              
                      /:. _/ ,  |                              
                     (|::.     ,`                              
                      |::.    {\                               
                      |::.\  \ `.                              
                      |:::(\    |                              
                      |:::/{ }  |                  (o          
               )  ___/#\::`/ (O "==._____   O, (O  /`          
          ~~~w/w~"~~,\` `:/,-(~`"~~~~~~~~"~o~\~/~w|/~          
      ~~~~~~~~~~~~~~~~~~~~~~~\\W~~~~~~~~~~~~\|/~~              

"""

kitchen_ascii = """

(_)-',_. |:         | | ~    | |      | |          _         
~.(( )_ (|:         | |      | | `    | |         (_)_       
 ))__`  .|:         | |  ~~  | |    ` | |       *-;)(_)      
_____]   |:         | |______| |______| |        .-(_).-.    
    /    |:         |___________________|       (/ ||  ( )   
 __/     |:        (_____________________)        ===== \|   
---------':  _.-    }___________________{        _\   /_     
'''''''''_.-'   ;                               ( |\_/| )    
       .'   _.-'|                                 `---'      
       ;_.-'|  ||                                 |___|      
       ||  ||(\||                                 |   |      
_____.-||`-||_\\\\|_________________________________)---(______
 _.-'  ||  ||_.\\\\     /       |       \       `(_/     \_)   
[-._-._||_.-_.-;\\\\__ /________| ~~~ ___\ _______`,__________ 
||  `-.||.-'  .||\\\\ /       ~~~.===.~~  \         `.         
||     ||,'  _.|| \\\\        ~.' ~~~ `.~~ \          `.       
||`-._ ||_.-'__||(\\\\\\\\--.__~o_.-----._o~__\ __________`._____
||   ,`||      ||/|/\\\\  //~~~\`-...-'/~~   \            `,   
|| ,'  ||       / / /\)//~~~~~\     /~~     \             `, 
 ,'    ||      /  \/__// ~~~~~~`---'~~~      \              `
              /   )__)'    ~~~|~~~~~~         \              

"""
enemy_ascii = r"""
         _______
         | | | |
         | | | |
         | | | |
        /_______\
        ( \   / )
       m (o) (o) m
        |   <   |
        (  ===  )
         \_____/
       ____|  |____
      /    \__/    \
     /              \
    /\_/|        |\_/\
   / /  |        |  \ \
  ( <   |        |   > )
   \ \  |        |  / /
    \ \ |________| / /
     \ \|"""
 
###############################################################################################
#                                             INVENTORY                                       #
###############################################################################################

# List containing all ingredients found in the game

list_of_ingredients = ["chicken", 
                       "eggs",
                       "cheese",
                       "lettuce",
                       "beef",
                       "wild berries",
                       "poisonous berries",
                       "rice",
                       "banana",
                       "salmon",
                       "water",
                       "prawns",
                       "seaweed",
                       "mango",
                       "mushroom",
                       "poisonous mushroom",
                       "apple",
                       "honey",
                       "bread",
                       "sausage",
                       "biscuits",
                       "pork",
                       "wine",
                       "potato",
                       "truffle",
                       "tuna",
                       "pasta",
                       "chorizo"]

# Dictionary containing all of the scores for all of the ingredients

food_scores = {
    "chicken": 1,
    "eggs": 2,
    "cheese": 3,
    "lettuce": 4,
    "beef": 5,
    "wild berries": 6,
    "poisonous berries": -100,
    "rice": 1,
    "banana": 2,
    "salmon": 4,
    "water": 1,
    "prawns": 6,
    "seaweed": 3,
    "mango": 4,
    "mushroom": 6,
    "poisonous mushroom": -100,
    "apple": 3,
    "honey": 5,
    "bread": 2,
    "sausage": 6,
    "biscuits": 3,
    "pork": 5,
    "wine": 4,
    "potato": 3,
    "truffle": 6,
    "tuna": 6,
    "pasta" : 3,
    "chorizo" : 4
} 

# Function that appends items in the inventory

def add_item_to_inventory(item):
    global inventory
    print_tff(f"\n            \x1B[3m{item} has been added to you inventory...\x1B[23m\n\n")
    if item == "mushroom":
        pick_mushroom()
    elif item == "berries":
        pick_berries()
    else:
        inventory.append(item)

# Function for mushrooms that have a 25% chance of being poisonous

def pick_mushroom():
    global inventory
    random_num = random.randint(1,100)
    if random_num > 75:
        inventory.append("poisonous mushroom")
    else:
        inventory.append("mushroom")

# Function for wilde berries that have a 25% chance of being poisonous

def pick_berries():
    random_num = random.randint(1,100)
    if random_num > 75:
        add_item_to_inventory("poisonous berries")
    else:
        add_item_to_inventory("wild berries")  

# Function that calculates the score of all items in the inventory, for the endgame

def add_inventory_scores():
    final_score = 0
    for item in inventory:
        if item in food_scores:
            final_score += food_scores[item]
    return final_score

# Function for describing the cooked meal at the end of the game

def describe_cooked_meal():
    global inventory
    if len(inventory) == 1:
        print_t(f"You explain to the Queen that you have cooked her a lovely {inventory[0]} stew\n")
    else:
        ingredient_list = ""
        for ingredient in inventory[:-2]:
            ingredient_list = ingredient_list + ingredient + ", "
                
        ingredient_list = ingredient_list + inventory[-2] + " and " + inventory[-1]
        print_t(f"You explain to the Queen that you have cooked her a lovely {ingredient_list} stew\n")

###############################################################################################
#                                             PLAYER                                          #
###############################################################################################

# Initialising player attributes 

player_name = " "
weapon_of_choice = " "
weapon_damage = 0

# Function that changes player's weapon/tool attributes, when picking that item up

def choose_weapon(weapon, damage):
    global weapon_of_choice
    global weapon_damage
    weapon_of_choice = weapon
    weapon_damage = damage

# Function for getting player name

def getplayername():
    print_t("What is your name?\n")
    player_name = input()
    if len(player_name) > 16:
        print_t("Sorry, please try a shorter name\n")
        return getplayername()
    elif len(player_name) < 2:
        print_t("Sorry, please try a longer name\n")
        return getplayername()
    elif checkinput(player_name):
        print_t("Sorry, please only use letters for your name\n")
        return getplayername()
        
    else:
        print("Is your name " + '\033[1m' + player_name + '\033[0m' + "? yes [y] no [n]")
        player_choice = input()
        if player_choice not in ["y", "Y"]:
            return getplayername()
        else:
            return player_name

# Function for checking that player name is a suitable format, returns a boolean

def checkinput(usr_input):
  spaces = 0
  for i in usr_input:
    if i.isspace() == True and spaces < 1:
      spaces += 1
    elif i.isalpha():
      continue
    else:
      return True
  return False

###############################################################################################
#                                             QUEEN                                           #
###############################################################################################

# Class called queen that contains all functions and attributes that are associated with the queen in the game

class queen:
    
    # Initialising function that randomly selects two ingredients to be her favourites and two for her to be allergic to

    def __init__(self):

        self.allergy = []
        self.favourite = []
        temp_list = list_of_ingredients
        temp_list.remove("poisonous mushroom")
        temp_list.remove("poisonous berries")

        self.allergy.append(random.choice(temp_list))
        
        temp_list.remove(self.allergy[0])
        self.allergy.append(random.choice(temp_list))
        temp_list.remove(self.allergy[1])
        
        self.favourite.append(random.choice(temp_list))
        temp_list.remove(self.favourite[0])
        self.favourite.append(random.choice(temp_list))

        for food in self.allergy:
            food_scores[food] = -100
        
        for food in self.favourite:
            food_scores[food] = 50

   # Function for returning the list that contains the queen's favourite food without being able to change the list

    def return_favourite_food(self):
        return self.favourite

    # Function for returning the list that contains the queen's allergies without being able to change the list

    def return_allergy(self):
        return self.allergy
    
    # End game function that is called if the player feeds the queen a poisonous ingredient or one of her allergies

    def chokes(self):
        global inventory
        print_tf('\n\n\033[1mQueen Destiny:\033[0m '  + """This food, it has a peculiar flavour... ehem... ghhh....\n\n""")
        if "poison berries" in inventory:
            print_t("""Those wild berries you picked were a poisonous variety, now you have killed the Queen...
The Queen's bodyguard charges at you...""")
        elif "poison mushrooms" in inventory:
            print_t("""Those mushrooms you picked were a poisonous variety, now you have killed the Queen...
The Queen's bodyguard charges at you...""")

        elif self.return_allergy()[0] in inventory and self.return_allergy()[1] in inventory:
            print_t(f"""Unfortunately the Queen was allergic to both {self.return_allergy()[0]} and {self.return_allergy()[1]}, somehow you included both in your meal
so now you killed the Queen...
The Queen's bodyguard charges at you...""")

        elif self.return_allergy()[0] in inventory or self.return_allergy()[1] in inventory:
            if self.return_allergy()[0] in inventory:
                queen_allergy = self.return_allergy()[0]
            else:
                queen_allergy = self.return_allergy()[1]
            print_t(f"""Unfortunately the Queen was allergic to {queen_allergy} so now you killed the Queen...
The Queen's bodyguard charges at you...""")

        print_tf('\n\n\033[1mKnight:\033[0m '  + """You traitor!! You purposefully killed the Queen, you'll pay for this!!\n\n""")
        return
        
    # End game function that is called if the player scores well without using one of her favourite foods

    def happy(self):
        print_tf('\n\n\033[1mQueen Destiny:\033[0m '  + f"""This food, it is wonderful... I was never a big fan of {random.choice(inventory)}
                but the way you have cooked with it is sublime... You truly are the best chef in the land...\n\n""")
        return

    # End game function that is called if the player scores poorly

    def unhappy(self):
        print_tf('\n\n\033[1mQueen Destiny:\033[0m '  + f"""This food, it is not good... I just don't like {random.choice(inventory)} very much
                and I've tasted far better food from Joe Chefy you know... 
                You aren't the best chef in the land, you are simply average...\n\n""")
        return

    # End game function that is called if the player scores very poorly

    def disgust(self):
        print_tf('\n\n\033[1mQueen Destiny:\033[0m '  + f"""This food, it is horrible... you are a complete and utter fraud...
                I don't want any frauds in my kingdom...
                GUARDS!!!\n\n""")
        print_t("The Queen is not happy, and neither is her bodyguard now rushing towards you...""")
        return
    
    # End game function that is called if the player feeds the queen one or both of her favourite foods

    def extatic(self):
        global inventory
        print_tf('\n\n\033[1mQueen Destiny:\033[0m '  + """This food, it is fantastic, I am simply amazed\n""")

        
        if (self.return_favourite_food()[0] and self.return_favourite_food()[1]) in inventory:
            print_t(f"""Fortunately the Queen's two favourite foods are {self.return_favourite_food()[0]} and {self.return_favourite_food()[1]}, somehow you included both in your meal
the Queen is extatic...""")

        elif (self.return_favourite_food()[0] or self.return_favourite_food()[1]) in inventory:
            if self.return_favourite_food()[0] in inventory:
                queen_favourite = self.return_favourite_food()[0]
            else:
                queen_favourite = self.return_favourite_food()[1]
            print_t(f"""Fortunately {queen_favourite} is one of the Queen's favourite foods
the Queen is extatic...""")

        print_tf('\n\n\033[1mQueen:\033[0m '  + """You truly are an amazing chef!! Take whatever land you want, I could eat that whole meal 5 times over!\n\n""")
        return

# Initialising the queen at the start of the game

the_queen = queen()

###############################################################################################
#                                             GAMEOVER                                        #
###############################################################################################

# Class called death that prints ascii images relating to how the player died

class death:
    @staticmethod
    def eaten():
        print_t("Oops you have been...\n")
        print(eaten_ascii)
        print_t("Better Luck Next Time...\n")
        endgame()
        return

    @staticmethod
    def murdered():
        print_t("Oops you have been...\n")
        print(murdered_ascii)
        print_t("Better Luck Next Time...\n")
        endgame()
        return

    @staticmethod
    def beheaded():
        print_t("Oops you have been...\n")
        print(beheaded_ascii)
        print_t("Better Luck Next Time...\n")
        endgame()
        return

    @staticmethod
    def impaled():
        print_t("Oops you have been...\n")
        print(impaled_ascii)
        print_t("Better Luck Next Time...\n")
        endgame()
        return

    @staticmethod
    def liquified():
        print_t("Oops you have been...\n")
        print(liquified_ascii)
        print_t("Better Luck Next Time...\n")
        endgame()
        return

# Endgame function that is called when the player wins the game

def win():
    print_t("You have won the game, would you like to see your reward?\n")
    print_t("""
            Press enter
""")
    input_in = input()
    print_t("You are now the owner of this beautiful castle, and you retain your position as best chef in the realm...\n")
    print(castle_ascii)
    print_t("We hope you enjoyed playing...\n")
    endgame()
    return

# Endgame function that is called at the end of the game and allows the player to start again if they want

def endgame():
    global the_queen
    print_tf("The game has ended, do you want to start again? yes [y] or no [n]\n")
    player_choice = input()
    if player_choice not in ["y", "Y", "n", "N"]:
      print("Your answer is not recognised/n")
      endgame()
    elif player_choice in ["y", "Y"]:
        the_queen = queen()
        gamestart()
    else:
      return


###############################################################################################
#                                             GAMEPLAY                                        #
###############################################################################################

# Function for all intersection choices in the game

def intersection_choice(option_a, option_b):\

    player_choice = input(f"""                  Would you like to turn... 

                    [l] Left  or  Right [r] \n""")\

    if player_choice in ["l", "L"]:
        return 1
    elif player_choice in ["r", "R"]:
        return 2
    else:
        print("That is not a valid choice, please type either [l], or [r]")
        intersection_choice(option_a, option_b)

# Function for opening section where the player is prompted to ask the queen's knight a question about the challenge

def queens_diet():
    global the_queen
    print_t("\nBefore the knight leaves, you have time to ask him one question about the mission:")
    print_tf("""

    [1] Does Her Majesty have any allergies?
    [2] What is Her Majesty's favourite food? \n\n""")
    print_t("Which question do you want to ask [1] or [2]?\n")
    player_choice = input()

    if player_choice not in ["1", "2"]:
        print_t("\nThat is not a valid choice, please type either 1, or 2")
        queens_diet()
    elif player_choice == "1":
        print_t('\033[1m' + "\nKnight: " + '\033[0m' + f"Yes, her majesty is allergic to {the_queen.return_allergy()[0]} and {the_queen.return_allergy()[1]}, farewell my friend and good luck...\n\n")
    else:
        print_t('\033[1m' + "\nKnight: " + '\033[0m' + f"Her majesty particularly likes {the_queen.return_favourite_food()[0]} and {the_queen.return_favourite_food()[1]}, farewell my friend and good luck...\n\n")

# Function that prompts the player to either accept or reject the challenge

def challengeaccept():
  print_t("\nDo you accept this challenge? yes [y] no [n]\n")
  player_choice = input()
  if player_choice in ["y", "Y"]:
    print_tf("You have accepted the challenge\n")
    return True
  else:
    print_tf("You have declined the Queens challenge, the knight does not look impressed...\n")
    death.beheaded()
    return False

# Function that is called in certain points of the game where the player has a choice of one of four ingredients to pick up

def area_pickup(food_here):
    print(f"""              Which food item do you choose? 

        [1] {food_here[0]}  [2] {food_here[1]}  [3] {food_here[2]}  [4] {food_here[3]}
    """)
    item_take = input()

    if item_take not in ["1", "2", "3", "4"] + food_here:
        print_tf("Not a valid choice, please try again...")
        return area_pickup(food_here)
    
    elif item_take in food_here:
        add_item_to_inventory(item_take)
    
    else:
        add_item_to_inventory(food_here[int(item_take)-1])

# Function that is called in the cottage when asking the player which item they want to take

def cottage_item(food_here):

    print(f"""
            Which food item do you choose? 

        [1] {food_here[0]}  [2] {food_here[1]}  [3] {food_here[2]}  [4] {food_here[3]}
    """)
    item_take = input()

    if item_take == "3":
        print_t("You pick up a bottle of wine you find in a cupboard, but your hand slips as you stand up...\n")
        if weapon_of_choice == "bottle":
            print_t("Luckily, you only crack the bottle, causing a small leak. You quickly decant the wine into the bottle you have had with you this whole time...\n")
            add_item_to_inventory("wine")
            return True
        else:
            print_t("The bottle smashes on the floor and causes you to slip up...\n")
            inventory_temp = inventory
            if "water" in inventory_temp:
                inventory_temp.remove("water")
            ruin = random.choice(inventory_temp)
            print_t(f"The {ruin} you had in your inventory is ruined, you can't feed it to the queen any more so you discard it...\n")
            inventory.remove(ruin)
            return True
    
    if item_take == "4":
        print_t("You find a couple of potatoes in the larder...\n")
        add_item_to_inventory("potato")
        return True
    
    if item_take == "2":
        print_t("You find some chorizo hanging up to cure, so you take it, what a weird thing to leave behind...\n")
        add_item_to_inventory("chorizo")
        return True
    
    if item_take == "1":
        print_t("You take a packet of biscuits that you find in the cupboard\n")
        add_item_to_inventory("biscuits")
        return True
    
    else:
        print_t("Your input is invalid please enter 1, 2, 3 or 4...\n")
        return cottage_item(food_here)

# Function that is called if the player encounters the trolls

def troll_encounter():
    print_t(f"""
                Forest Trolls are here...

    You approach the troll camp... There are three trolls... 
    The biggest one is cooking a beef steak over a campfire, the other two are having an arm wrestle... 
    Around the camp, there are banana trees full of bananas, you also notice a sack of rice on the other side of the camp...
    and you remembered seeing some wild berries on your way through the wood...

            What do you want to do?
""")

    print_tf(f"""
            [1] Attack the trolls with your {weapon_of_choice} and take the beef
            [2] Hide and wait for the trolls to leave and pick the bananas
            [3] Confront the trolls, and demand they let you past taking the sack of rice as you pass through
            [4] Turn back and pick the berries you saw as you came through the woods
        """)

    player_choice = input()
    if player_choice == "1":
        random_number = random.randint(1,10)
        if random_number > weapon_damage:
            print_t("Unfortunately the trolls have bested you in combat...\n")
            death.murdered()
            return False
        else: 
            if weapon_damage > 5:
                print_t("You defeated the trolls and took the beef, well done...\n")
            else:
                print_t(f"Somehow you fought off the trolls with only a {weapon_of_choice} and took the beef, well done...\n")
                        
            add_item_to_inventory("beef")
            return True

    elif player_choice == "2":
        print_t("You wait for the trolls to leave and pick a few ripe bananas...\n")
        add_item_to_inventory("banana")
        return True
    
    elif player_choice == "3":
        print_t("You shout at the trolls to indimidate them, the trolls are so busy they don't even notice you, so you sneak through the camp, snatch the rice, and leave...\n")
        add_item_to_inventory("rice")
        return True
    
    elif player_choice == "4":
        print_t("You turn back the way you came, picking a few red berries...\n")
        add_item_to_inventory("berries")
        return True
    
    else:
        print_t("Your input is invalid please enter 1, 2, 3 or 4...\n")
        return troll_encounter()

# Function that is called if the player encounters the boar

def boar_encounter():
    print_t("""
    
            What do you want to do?
    """)

    print_tf(f"""
            [1] Defend yourself against the boar with your {weapon_of_choice}
            [2] Try to calm down the boar
            [3] Attempt to dodge the boar and enter the cave behind it to get try and get the mushrooms
            [4] Run away from the boar back the way you came
        """)
    
    player_choice = input()
    if player_choice == "1":
        random_number = random.randint(1,12)
        if random_number > weapon_damage:
            print_t("Unfortunately the boar bested you in combat...\n")
            death.impaled()
            return False
        else: 
            if weapon_damage > 5:
                print_t("You killed the boar, and you harvest some raw pork from its carcass, well done... \n")
            else:
                print_t(f"Somehow you fought off the boar with only a {weapon_of_choice} and took some pork from is carcass, well done...\n")
                        
            add_item_to_inventory("pork")
            return True

    elif player_choice == "2":
        if weapon_of_choice == "flute":
            print_t("You play a nice melody on your flute and the boar stops its charge, it looks like it enjoys the sound of the music, once you stop, the boar starts digging with its tusks in the dirt in the front of the cave...\n")
            print_t("The boar tosses up a truffle and flicks it towards you with its nose, nice one...\n")
            add_item_to_inventory("truffle")
            return True
        
        else:
            print_t("You try singing to calm the boar down but your singing skills are far worse than your cooking skills. It only enrages the boar even more...\n")
            death.impaled()
            return False
    
    elif player_choice == "3":
        print_t("You dodge the boar's charge and you enter the cave, the boar doesn't seem to want to chase you back into the cave, perhaps it was just messing about...\n")
        print_t("At the back of the cave you see some delicious looking mushrooms growing, so you pick them\n")
        add_item_to_inventory("mushroom")
        return True
    
    elif player_choice == "4":
        print_t("You sprint back along the path you came, the boar is catching up with you so you climb the nearest tree and wait until the boar leaves...\n")
        print_t("You notice a nice large mango hanging from a nearby branch and grab it\n")
        add_item_to_inventory("mango")
        return True
    
    else:
        print_t("Your input is invalid please enter 1, 2, 3 or 4...\n")
        return boar_encounter()

# Function that is called if the player accepts the cook off

def cook_off():
    print_t("""
    What do you want to do?
    """)

    print_tf(f"""
            [1] Enter the cook off
            [2] Tell the shopkeeper that there is not point because you are already the best cook in the land and leave
            [3] Watch the other chefs in the cook off
            [4] Thank the shopkeeper for the information but explain that you don't have enough time
        """)
   
    
    player_choice = input()
    if player_choice == "1":
        if weapon_of_choice == "spoon":
            print_t("You enter the cook off, glad that you brought your wooden spoon...\n")
            print_t("Your culinary brain whirrs and your fingertips masterfully control your wooden spoon, the judges try your broth...\n")
            print_t("You smoke your opposition, because of course you do, you are the best chef in the kingdom after all...\n")
            print_t("As your prize you recieve a whole fresh tuna, good job...\n")
            add_item_to_inventory("tuna")
            return True
        
        else:
            print_t("You enter the cook off but get disqualified for using your finger to stir the broth, how unhygeinic...")
            print_t("You should have picked up your wooden spoon before you left...\n")
            return True 

    elif player_choice == "2":
        print_t("The shopkeeper is too busy serving other customers to aknowledge your boast, making you feel a little silly...\n")
        return True
    
    elif player_choice == "3":
        print_t("You watch the other chefs in the competition, none of them look any good so you leave before the winner is announced, what a waste of time...\n")
        return True
    
    elif player_choice == "4":
        print_tf('\n\n\033[1mShopkeeper:\033[0m ' + "Very well my friend, have a good day...\n")
        return True
    
    else:
        print_t("Your input is invalid please enter 1, 2, 3 or 4...\n")
        return boar_encounter()

###############################################################################################
#                                             STORY                                           #
###############################################################################################

# Opening function that starts the game

def gamestart():
    global the_queen
    print(foodhunt_ascii)
    global player_name
    global inventory
    inventory = []
    player_name = getplayername()

    print_t(
        "You are sat in your beautiful fantasy cottage, the sun is shining, you are watching the birds as they fly past your window when you hear a sound at your front door...\n")
    print_tf(""" KNOCK!
       KNOCK!\n""")
    print_t("You open your door to see a knight in full armour, with a shield bearing the royal coat of arms...\n")
    print('\033[1m' + '\033[74m' + knight_ascii)
    
    print_tf('\n\n\033[1mKnight:\033[0m ' + f"Hello {player_name}, I have been sent here by Her Majesty the Queen, to personally deliver a letter to you...\n\n")

    print_t("You look down at the letter and it reads...\n\n")

    print_t('\x1B[3m' + 
            f"Dear {player_name},\n" + """
        It is with great pleasure with which I announce that I the Queen of Newville will be visiting your humble abode on the morrow.
        word has reached me that you are one of the best chefs in all the land and I request that you prepare one of your finest meals for me,
        If I am impressed, I will give you fertile land and a beautiful castle, and grant you a noble title befitting of your honour. Fail me and you'll see my disappointment.

        Her Royal Highness Queen Destiny of Newville""" + '\x1B[0m\n')

    if challengeaccept():
        queens_diet()

        print_t("The Knight mounts his horse and rides off, your perilous adventure has begun...\n\n")
        kitchen_area()
    
# Function for the kitchen area

def kitchen_area():

    print_t("""You head back towards your kitchen and check your cupboards for ingredients.
    """)
    print(kitchen_ascii)
    print_t("""
    Maybe skipping the shopping trip wasn't such a good idea, they are all empty.  
    Time to go gather the freshest most delicious ingredients in the realm.""")
    user_choice = ""
    while not user_choice in ["1", "2", "3", "4"]:
        print_t("""
    \nBefore you leave you take one piece of equipment from the kitchen, choose carefully...
    """)
        print_tf("""
                Which item would you like to take?

        [1] Knife    [2] Bottle   [3] Flute   [4] Spoon
    """)
        user_choice = input()
        if user_choice not in ["1", "2", "3", "4"]:
            print("That is not a valid choice\n")

        elif user_choice == "1":
            choose_weapon("knife", 10)
            
        elif user_choice == "2":
            choose_weapon("bottle", 7)
            
        elif user_choice == "3":
            choose_weapon("flute", 1)
            
        else:
            choose_weapon("spoon", 3)
    
    print_t(f"""You haven't got long to get all the ingredients for the meal, you put on your coat, 
grab your backpack and head out of your front door with your trusty {weapon_of_choice} in your pocket\n""")
        
    intersection1()

# Function for the first intersection
    

def intersection1():
    global player_name
    option_a = "woods"
    option_b = "market"
    print_t("\nYou walk down the path away from your lovely home, the first intersection in the path is a fork, the sign says: ")
    print(r"""
    
                     .--._..--.
              ___   ( _'-_  -_.'
          _.-'   `-._|  - :- |
      _.-'           `--...__|
   .-'                       '--..___
  / `._         Bear Woods            \
   `. `._                             |
     `. `._                           /
       '. `._    :__________....-----'
         `..`---'    |-_  _- |___...----..._
                     |_....--'             `.`.
               _...--'                       `.`.
          _..-'                            _.'.'
       .-'        Pickletown Market      _.'.'
       |                               _.'.'
       |                   __....------'-'
       |     __...------''' _|
       '--'''        |-  - _ |

""")


    choice = intersection_choice(option_a, option_b)
    if choice == 1:
        print_t("""As you follow the path to the woods, you notice someone following you...
        ...""")
        print(enemy_ascii)
        print_tf('\n\n\033[1mJoe Chefy:\033[0m ' + f"""Everyone knows I am in fact the best chef in the land, the Queen should have chosen me to cook her meal... \n\tI'll show you... Watch your back {player_name}\n\n""")
        print_t("""Joe Chefy turns and walks away, better make sure no-one tries to interfere with the Queen's meal...
        
        You continue on your merry way down the long path towards Bear Woods...
        \n""")
        woods()
    else:
        print_t("""As you follow the path to the market, you notice someone following you...
...""")
        print(enemy_ascii)
        print_tf('\n\n\033[1mJoe Chefy:\033[0m ' + f"""Everyone knows I am in fact the best chef in the land, the Queen should have chosen me to cook her meal... \n\tI'll show you... Watch your back {player_name}\n\n""")
        print_t("""Joe Chefy turns and walks away, better make sure no-one tries to interfere with the Queen's meal...
        
        You continue on your merry way down the long path towards Pickletown...
        \n""")
        market()

# Function for the forest area

def woods():
    food_here = ["beef", "wild berries", "rice", "banana"] 
    print_t("\n\tYou enter Bear Woods...")
    print(woods_ascii)
    print_t("""
Bear woods is not as clear as it usually is, the bushes and vines are getting thicker and thicker, almost to the point that you cannot see anything, 
You smell the terrible smell of rotten eggs, this could only mean one thing...\n""")
    if troll_encounter():
        intersection2()

# Function for the market area

def market():
    food_here = ["chicken", "eggs", "cheese", "lettuce"]
    print_t("\n\tYou enter Pickletown Market....")
    print(market_ascii)
    print_t("""
The market is bustling with noise and there are many street food stalls, you approach a nearby stall and ask the shopkeeper what he has on offer...""")
    print_tf('\n\n\033[1mShopkeeper:\033[0m ' + "I have Chicken breasts, plenty of eggs, nice local cheese and plenty of lettuce, what would you like to buy?\n\n")
    print_t("You only have enough change in your pocket for one of the shop keeper's items...\n\n")
    area_pickup(food_here)
    print_tf('\n\n\033[1mShopkeeper:\033[0m ' + "Thank you for your purchase! By the way my friend, there is a mini cook off about to begin over by the village hall, they have a very special local ingredient as the prize if you are interested...\n")
    if cook_off():
        intersection2()

# Function for the second intersection

def intersection2():
    option_a = "beach"
    option_b = "cave"
    print_t("""You follow another path further from home. The ingredients you have so far, are not enough for you to cook a meal befitting a Queen. 
And you are starting to worry about the time you have left...\n""")
    print_t("A short while down the path you come across a fork in the road, with a signpost: ")

    print(r"""
    
                     .--._..--.
              ___   ( _'-_  -_.'
          _.-'   `-._|  - :- |
      _.-'           `--...__|
   .-'                       '--..___
  / `._     Mountain valley           \
   `. `._                             |
     `. `._                           /
       '. `._    :__________....-----'
         `..`---'    |-_  _- |___...----..._
                     |_....--'             `.`.
               _...--'                       `.`.
          _..-'            Ancient Cave     _.'.'
       .-'                                _.'.'
       |                               _.'.'
       |                   __....------'-'
       |     __...------''' _|
       '--'''        |-  - _ |

""")
    choice = intersection_choice(option_a, option_b)
    if choice == 1:
        mountains()
    else:
        cave()

# Function for the mountains area

def mountains():
    food_here = ["salmon", "pasta", "prawns", "seaweed"]
    alive = True
    print(mountains_ascii)
    print_t("""
    You walk up the long treacherous mountain path, the mountain peaks stretch high into the sky above you, 
    the valley is just beyond the nearest peak, you worry you might not get there in time...
    ...
    ...
    ...""")

    print_t("""

    After walking for what seems like an hour, out of the fog you make out an elderly lady struggling to walk towards you, 
    she is carrying a heavy sack, as she gets nearer she notices you and gives you a weak smile..."""
    )

    print_tf('\n\n\033[1mElderly Lady:\033[0m ' + "Please, traveller, could you possibly help me carry my groceries back to my house? My poor back will give way anytime soon!\n")
    print_tf("""
        Do you?

            [1] Help the elderly lady and lose some time with preparation?
            [2] Ignore her and rush to find your last ingredient, the queen is more important
            [3] Snatch the groceries from the elderly lady and run away
    """)
    user_choice = ""
    while user_choice not in ["1", "2", "3"]:
        user_choice = input()
        if user_choice == "1":
            print_t("Surprise, this is no ordinary woman, This is the witch of the mountains. She thanks you for your help and gifts you any ingredient in her grocery bag that you want")
            print_tf('\n\n\033[1mWitch:\033[0m ' + "When you are good to others you will be rewarded!\n\n")
            area_pickup(food_here)
            print_t("You thank the witch and carry on your merry way...\n")
        elif user_choice == "2":
            print_t("Oh no! This is no ordinary woman, its the witch of the mountains and you chose to ignore her. She curses you as she hops on her broomstick and turns your coat into seaweed.\n")
            print_t("\nNext time you should help those in need.\n")
            add_item_to_inventory("seaweed") 
        elif user_choice == "3":
            print_t("You try to snatch the woman's bag, but strangely your body doesn't seem to be able to move. Oh no! This is no ordinary woman, its the witch of the mountains and she has cast a spell on you!")
            print_tf('\n\n\033[1mWitch:\033[0m ' + "Evil foe, you would try to steal from a struggling elderly lady?\n\n")
            print_t("The witch mutters some words under her tongue and looks at you dead in the eye. You start getting a very strange sensation all over your body...\n")
            death.liquified()
            alive = False
        else:
            print("That is not a valid selection, please select again.\n")
    

    if alive:
        intersection3()

# Function for the cave area

def cave():
    food_here = ["ham", "mushroom", "mango", "truffle"]
    print(cave_ascii)
    print_t("\n\tYou approach an old cave.... it looks spooky, but you know there are mushrooms in there")
    print_tf("""
            EEEEEEKKKK!!!!
                           EEEEEEKKKKKK!!!\n""")
    print_t("A monstrous wild boar charges out the cave, it doesn't look very happy!")
    if boar_encounter():
        intersection3()

# Function for the third intersection

def intersection3():
    option_a = "bridge"
    option_b = "abandoned cottage"
    print_t("\n\tYou carry along the path through the rocky terrain, eventually approaching a fork in the road with a signpost that reads:")
    print(r"""
    
                     .--._..--.
              ___   ( _'-_  -_.'
          _.-'   `-._|  - :- |
      _.-'           `--...__|
   .-'                       '--..___
  / `._     Lilly Bridge             \
   `. `._                             |
     `. `._                           /
       '. `._    :__________....-----'
         `..`---'    |-_  _- |___...----..._
                     |_....--'             `.`.
               _...--'                       `.`.
          _..-'          Fairview Cottage   _.'.'
       .-'                                _.'.'
       |                               _.'.'
       |                   __....------'-'
       |     __...------''' _|
       '--'''        |-  - _ |

""")

    choice = intersection_choice(option_a, option_b)  # run function for getting player input
    if choice == 1:
        bridge()
    else:
        cottage()
    
# Function for the bridge area

def bridge():
    food_here = ["apple", "honey", "bread", "water"]
    print(bridge_ascii)
    print_t("\n\tYou approach a old stone bridge, sitting on the bridge, blocking the path is a goblin")
    print_tf('\n\n\033[1mGoblin:\033[0m '  + """Halt! You dare to attempt to cross the Bridge of the Riddle-master Goblin? 
        Answer my riddle and I'll allow you to cross and give you some food for the journey, get the answer wrong and i'll throw you off the bridge
    """)
    print_tf("""
    I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?

            [1] Trees
            [2] Water
            [3] Fire
            [4] Air

    """)
    user_choice = ""
    while user_choice not in ["1", "2", "3", "4"]:
        print("What do you pick?\n")
        user_choice = input()
        if user_choice == "1":
            print_tf('\n\n\033[1mGoblin:\033[0m ' + "Wrong answer, looks like you ain't crossing this bridge today\n")
            add_item_to_inventory("water")
        elif user_choice == "2":
            print_tf('\n\n\033[1mGoblin:\033[0m ' + "Wrong answer, looks like you ain't crossing this bridge today\n")
            add_item_to_inventory("water")
        elif user_choice == "3":
            print_tf('\n\n\033[1mGoblin:\033[0m ' + "Correct, didn't think you'd get that one. Take your pick of food traveller...\n")
            area_pickup(food_here)
        elif user_choice == "4":
            print_tf('\n\n\033[1mGoblin:\033[0m ' + "Wrong answer, looks like you ain't crossing this bridge today\n")
            add_item_to_inventory("water")
        else:
            print_t("That is not a valid selection\n")
    
    intersection4()

# Function for the cottage area

def cottage():
    food_here = ["biscuits", "chorizo", "wine", "potato"]
    print(cottage_ascii)
    print_t("""\nAs you approach the cottage you can tell something is wrong, the windows are broken and the front door is wide open, 
    you worry about the kind family of merchants who used to live here...\n""")
    print_t("""You enter the house and have a look around, there are no clothes or personal items left in the house so it looks like the merchant family left of their own accord, 
    luckily they have left some food items but you only have space in your rucksack for one item...\n""")
    
    if cottage_item(food_here):
        intersection4()

    
# Function for the fourth intersection

def intersection4():
    
    """
    option_a = "home"
    option_b = "extra area" # potential to create extra areas once ready
    print("\n\tshort text decribing the area...\n\t")
    # add extra story here describing the area, ascii art etc
    choice = intersection_choice(option_a, option_b) # run function for getting player input
    if choice == 1:
        home()
    else:
        extra_area()  # potential to create extra areas once ready
    """
    print("the Sun begins to set, you need to be up early in the morning to start cooking for the queen, so you head home...\n")
    home()

# Function for the final stage of the game, at the home and for the queen's arrival

def home():
    global the_queen
    global inventory
    score = add_inventory_scores()
    
    print_t("""
    You arrive back at your house after your journey to find the food 
    and begin to unpack all of the ingredients you picked up along the 
    way. Nerves begin to kick in, you hope the queen is going to enjoy
                the meal you've worked so hard on.
    You prepare the meal ready for the queen to arrive and take a seat 
                      to relax for a moment...
    """)
 
    print_t("""
    You hear trumpets playing in the distance, you begin to get nervous
    but you are confident in your abilty to prepare a tasty meal.""")
    
    print_t("""
    
    The moment has arrived....
    """)
    
    print(queen_ascii)

    print_t("""
    The Queen enters and you exchange the required pleasantries. She sits 
    down to the your kitchen table where you place the meal in front of 
            her. She inquires the name of the dish...
    """)
    print(soup_ascii)
    describe_cooked_meal()
    loop = True

    while loop:
        for item in the_queen.return_allergy():
            if item in inventory and loop:
                the_queen.chokes()
                death.beheaded()
                loop = False
                break
        for item in the_queen.return_favourite_food():
            if item in inventory and loop:
                the_queen.extatic()
                win()
                loop = False
                break

        if score > 8 and loop:
            the_queen.happy()
            win()
            loop = False
            break
        
        elif score <= 8 and score >= 5 and loop:
            the_queen.unhappy()
            print_t("You have lost your pride but you are still alive, you should have been more daring...\n")
            endgame()
            loop = False
            break

        elif score < 5 and loop:
            the_queen.disgust()
            death.beheaded()
            loop = False
            break
        
        break

###############################################################################################
#                                             GAMESTART                                       #
###############################################################################################

# Start the game
gamestart()