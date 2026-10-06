## AUTHOR: Rene DeLage
## Project Submission - Text-Based Game
## Created 9/20/2026
## Version 1.0

import random

### define available input options

options = ['1', '2', '3', '4', '5', '6']
direction = ['N', 'S', 'W', 'E', 'X']

### define rooms

rooms = {
    'Main Lobby' : {'W' : 'Evidence Room', 'E' : 'Records Room', 'N' : 'North Hall'},
    'Evidence Room' : {'E' : 'Main Lobby'},
    'Records Room' : {'W' : 'Main Lobby'},
    'North Hall' : {'W' : 'Armory', 'N' : "Chief's Office", 'E' : 'Locker Room', 'S' : 'Main Lobby'},
    'Armory' : {'E' : 'North Hall'},
    'Locker Room' : {'W' : 'North Hall'},
    "Chief's Office" : {'S' : 'North Hall'}
}
current_room = ''


### define items and create inventory lists

pistol = "M1911 Pistol"
partskit = "Pistol Parts Kit"
armor = "Body Armor"
charm = "Lucky Charm"
aidkit = "First Aid Kit"
lock = "Locker Key"
keycard = "Lab Keycard"
password = 'hope123'
code = 'GBKZ'
chief = "Something's been off with the chief lately. He's been holed up in his office more than usual lately, and he's been very territorial over that bookcase..."
admin = f"The IT guy was working on the chief's computer again. He said he had to reset the Chief's password; it's now '{password}'."
safe = f"Sam brought in a new safe for the Armory last week. The code needs to be reset; it's currently {code}."

inventory = []
notes = []


### define starting player stats

player_hp = 100
hp_limit = 100
weapon_mod = 0.0


### set up basic player actions

def actions(): 
    """Presents available actions to the player and prompts for their input, which will be validated."""

    print('-'*100)
    print(f"\n{f"You are in the {current_room}.":^100}\n")
    print('-'*100)
    while True:
        print("The following actions are available:\n1 - Explore the Room\n2 - Move to A Different Room\n3 - Check Stats\n4 - Check Inventory\n5 - Check Notes\n6 - Quit Game\n")
        selection = input("What would you like to do? ")
        if selection not in options:
            print('-'*50)
            print("You have made an invalid selection. Please try again.")
            print('-'*50)
        elif selection == '1':
            search()
            break
        elif selection == '2':
            movement()
            break
        elif selection == '3':
            get_stats()
            break
        elif selection == '4':
            get_inv()
            break
        elif selection == '5':
            get_notes()
            break
        elif selection == '6':
            quit()
            break


### set up movement between rooms

def movement():
    """Presents movement options to the player based on what room they're currently in."""

    global current_room
    while True:
        print('-'*50)
        print(f"The following rooms are available to explore: ")
        for x in rooms[current_room]:
            print(f"{x} - {rooms[current_room][x]}")
        print()
        selection = input("In which direction would you like to move (N, S, W, E, or X to cancel): ")
        if selection.upper() not in direction:
            print('-'*50)
            print("You've made an invalid selection please try again.")
        else:
            if selection.upper() == 'X':
                actions()
                break
            else:
                if selection.upper() in rooms[current_room]:
                    current_room = rooms[current_room][selection.upper()]
                    actions()
                    break
                else:
                    print('-'*50)
                    print("There's nothing in that direction. Please try again")


### setup request to pull player stats

def get_stats():
    """Displays the player's current stats"""

    print('-'*50)
    print(f"Jack Ryder HP: {player_hp}/{hp_limit}")
    print(f"Current room: {current_room}")
    print(f"Items found: {len(inventory)}")
    print(f"Notes found: {len(notes)}")
    print('-'*50)
    actions()


### setup request to pull inventory

def get_inv():
    """Lists the player's current inventory items"""

    print('-'*50)
    if not inventory:
        print("(You don't have any items yet.)")
    else:
        for i in inventory:
            print(f">>> {i}")
    print('-'*50)
    actions()


### setup request to pull notes

def get_notes():
    """Lists the player's current found notes"""

    print('-'*50)
    if not notes:
        print("(You don't have any notes yet.)")
    else:
        for i in notes:
            print(f">>> {i}")
    print('-'*50)
    actions()


### establish starting sequence

def start():
    """Start sequence of the game. Introduces story and places the player in the starting room."""

    global current_room
    print('-' * 140)
    print(f"{'OPERATION LOCKDOWN':^140}")
    print('-'*140)
    print(f"{'The city is in a state of shock as Police Chief John Hawkins has suddenly turned against the people he once swore to protect.':^140}\n" \
    f"{"Hawkins has taken control of the Police Station, armed with a device that he claims will unleash a deadly virus upon the city's population.":^140}\n" \
    f"{"The city's fate lies in the hands of FBI Special Agent Jack Ryder who is single-handedly infiltrating the Police Station to stop Hawkins.":^140}")
    print('-'*140)
    print()
    current_room = 'Main Lobby'
    actions()


### prompt for a new playthrough and reset stats

def restart():
    """"Gives the player the option to restart the game. Also resets starting stats and inventory."""
    
    global player_hp
    global hp_limit
    global inventory
    global notes
    global weapon_mod
    player_hp = 100
    hp_limit = 100
    inventory = []
    notes = []
    weapon_mod = 0.0
    selection = input("Enter 1 to play again. Enter any other character to exit. ")
    if selection == '1':
        start()
    else:
        print("Goodbye and thanks for playing!")


### player opts to quit game

def quit():
    """Asks the player for confirmation to quit the game."""

    confirm = ''
    while confirm != '1' and confirm != '2':
        print('-'*50)
        confirm = input("Are you sure you want to quit?\n1 - Confirm and Quit\n2 - Go Back\n\nWhat would you like to do? ")
        if confirm == '1':
            print('-'*140)
            print(f"{"Goodbye and thanks for playing!":^140}\n\n{"GAME OVER":^140}")
            print('-'*140)
            restart()
        elif confirm == '2':
            actions()
        else:
            print("You have made an invalid selection. Please try again.")


### setup search function for each room

def search():
    """Connects items to rooms, making them available to the player once the room is searched."""

    global player_hp
    global hp_limit
    global weapon_mod
    if current_room == 'Main Lobby':
        print('-'*50)
        print('There are various pamphlets and posters, but nothing of interest.')
        print('-'*50)
        actions()

    elif current_room == 'Evidence Room':
        while True:
            print('-'*50)
            print("There is a counter you can search as well as some shelves.\n\t1 - Search the Counter\n\t2 - Search the Shelves\n\t3 - Go Back\n")
            search = input("What would you like to do? ")
            if search == '1' and pistol not in inventory:
                inventory.append(pistol)
                weapon_mod = 1.0
                print('-'*50)
                print("You found a M1911 Pistol!")
            elif search == '1' and pistol in inventory:
                print('-'*50)
                print("A few containers of evidence sit on the counter, waiting to be logged.\nThere's nothing else of interest here.")
            elif search == '2' and charm not in inventory:
                inventory.append(charm)
                print('-'*50)
                print("You found a Lucky Charm; better hold on to it.")
            elif search == '2' and charm in inventory:
                print('-'*50)
                print("The shelves are lined with some of the station's most memorable pieces of evidence.\nThere's nothing else of interest here.")
            elif search == '3':
                print('-'*50)
                actions()
                break
            else:
                print("You've made an invalid selection. Please try again.")
                print('-'*50)

    elif current_room == 'Records Room':
        while True:
            print('-'*50)
            print("You spot a PC that is logged in and a large filing cabinet.\n\t1 - Use the PC\n\t2 - Search the Filing Cabinet\n\t3 - Go Back\n")
            search = input("What would you like to do? ")
            if search == '1' and admin not in notes:
                notes.append(admin)
                print('-'*50)
                print("You found a note!\n")
                print(admin)
            elif search == '1' and admin in notes:
                print('-'*50)
                print("No other files appear relevant.")
            elif search == '2' and chief not in notes:
                notes.append(chief)
                print('-'*50)
                print("You found a note!\n")
                print(chief)
            elif search == '2' and chief in notes:
                print('-'*50)
                print("Nothing but a filing cabinet full of intake files.\nThere's nothing else of interest here.")
            elif search == '3':
                print('-'*50)
                actions()
                break
            else:
                print("You've made an invalid selection. Please try again.")
                print('-'*50)

    elif current_room == 'North Hall':
        if safe not in notes:
            print('-'*50)
            print("You found a note!\n")
            notes.append(safe)
            print(safe)
            print('-'*50)
            actions()
        else:
            print('-'*50)
            print("It's a rather plain hall; there's nothing else of interest here.")
            print('-'*50)
            actions()

    elif current_room == 'Armory':
        while True:
            print('-'*50)
            print("The Armorer's Workbench is on the far wall, and there's a Safe in the corner.\n\t1 - Search the Armorer's Workbench\n\t2 - Search the Safe\n\t3 - Go Back\n")
            search = input("What would you like to do? ")
            if search == '1' and partskit not in inventory:
                print('-'*50)
                print("You found the Pistol Parts Kit!")
                if pistol in inventory:
                    inventory.append(partskit)
                    print("Your Pistol's damage has increased!")
                    weapon_mod = 1.5
                else:
                    print("You have nothing to use this with. Better come back when you have a weapon.")
            elif search == '1' and partskit in inventory:
                print('-'*50)
                print("Various tools and parts remain on the bench.\nNone of these will be useful though.")
            elif search == '2' and armor not in inventory:
                print('-'*50)
                enter_code = input("Enter the safe's code: ")
                if enter_code.upper() == code:
                    inventory.append(armor)
                    print('-'*50)
                    print("You opened the safe and found Body Armor!\nYour Max HP has increased!")
                    player_hp += 50
                    hp_limit += 50
                else:
                    print('-'*50)
                    print("The code you entered was incorrect.")
            elif search == '2' and armor in inventory:
                print('-'*50)
                print("The safe is empty.")
            elif search == '3':
                print('-'*50)
                actions()
                break
            else:
                print("You've made an invalid selection. Please try again.")
                print('-'*50)

    elif current_room == 'Locker Room':
        while True:
            print('-'*50)
            print("There is a set of lockers along the wall and showers off to the side.\n\t1 - Search the Lockers\n\t2 - Search the Showers\n\t3 - Go Back\n")
            search = input("What would you like to do? ")
            if search == '1' and keycard not in inventory:
                if lock in inventory:
                    print('-'*50)
                    print("You unlocked the Chief's locker!")
                    inventory.append(keycard)
                    print("You found the Lab Keycard!")
                else:
                    print('-'*50)
                    print("The lockers are all locked and can't be opened.")
            elif search == '1' and keycard in inventory:
                print('-'*50)
                print("All the other lockers here are locked.")
            elif search == '2' and aidkit not in inventory:
                inventory.append(aidkit)
                print('-'*50)
                print("You found a First Aid Kit!\nUse it to restore HP!")
            elif search == '2' and aidkit in inventory:
                print('-'*50)
                print("The showers smell a bit musty; better keep moving.")
            elif search == '3':
                print('-'*50)
                actions()
                break
            else:
                print("You've made an invalid selection. Please try again.")
                print('-'*50)

    elif current_room == "Chief's Office":
        while True:
            print('-'*50)
            print("The chief's desk sits in front of an impressive bookcase.\n\t1 - Search the Chief's Desk\n\t2 - Examine the Bookcase\n\t3 - Go Back\n")
            search = input("What would you like to do? ")
            if search == '1' and lock not in inventory:
                inventory.append(lock)
                print('-'*50)
                print("You found a Locker Key!")
            elif search == '1' and lock in inventory:
                print('-'*50)
                print("There are several stacks of paperwork and an interesting paperweight.\nThere's nothing else of interest here.")
            elif search == '2' and keycard not in inventory:
                print('-'*50)
                print("You slide the bookcase aside and find a hidden door!\nThere is a card reader next to the door.\nA keycard is needed to open this door.")
            elif search == '2' and keycard in inventory:
                print('-'*50)
                print("You use the Keycard, and the door slides open.\n\t1 - Enter Secret Lab\n\t2 - Go Back")
                print('-'*50)
                while True:
                    selection = input("What would you like to do? ")
                    if selection == '1' and keycard in inventory:
                        if pistol in inventory:
                            lab()
                            break
                        else:
                            print('-'*50)
                            print("\nI need to find a weapon before entering...\n")
                            print('-'*50)
                            actions()
                            break
                    elif selection == '1' and keycard not in inventory:
                        print("The door is locked.")
                    elif selection == '2':
                        break
                    else:
                        print("You've made an invalid selection. Please try again.")
                break
            elif search == '3':
                print('-'*50)
                actions()
                break
            else:
                print("You've made an invalid selection. Please try again.")
                print('-'*50)
        

### end game sequence

def lab():
    """Starts the end game sequence where the player must battle Cheif Hawkins.
    Damage output is calculated using random number generation, similar to rolling a 20-sided die.
    Possessing the Lucky Charm item adds 5 to each of the player's rolls.
    The First Aid Kit item can also be used to restore up to half of the player's HP; onle one is available though.
    If the player defeats Hawkins, they'll be prompted to disarm the device.
    The disarm sequence requires a password to be entered correctly; only 4 attempts are available."""

    print('-'*100)
    print(f"\n{"You have found the Chief's Secret Lab!":^100}\n\n{"Chief Hawkins is waiting for you and raises his pistol towards you.":^100}\n")
    print('-'*100)
    global player_hp
    hawkins_hp = 200
    hawkins_maxhp = 200

    while player_hp > 0 and hawkins_hp > 0:
        print("Available actions:\n\t1 - Attack Hawkins\n\t2 - Use First Aid Kit\n\t3 - Check Stats\n\t4 - Surrender")
        moves = ['1','2','3','4']
        selection = input("What would you like to do? ")
        if selection not in moves:
            print('-'*50)
            print("You made an invalid selection. Please try again.")
            print('-'*50)

        elif selection == '1':
            print('-'*50)
            roll = random.randint(0,20)
            if charm in inventory:
                roll += 5
            if roll <= 6:
                print("Your attack missed!")
            elif roll < 11:
                dmg = int(6 * weapon_mod)
                hawkins_hp -= dmg
                print(f"You struck one of Hawkins' limbs and did {dmg} damage!")
            elif roll < 16:
                dmg = int(12 * weapon_mod)
                hawkins_hp -= dmg
                print(f"You struck Hawkins in the chest and did {dmg} damage!")
            elif roll < 20:
                dmg = int(18 * weapon_mod)
                hawkins_hp -= dmg
                print(f"You landed a critical hit on Hawkins and did {dmg} damage!")
            else:
                dmg = int(25 * weapon_mod)
                hawkins_hp -= dmg
                print(f"You landed a critical headshot on Hawkins and did {dmg} damage!")

            if hawkins_hp > 0:
                print("Hawkins lines up a shot back at you!")
                roll = random.randint(0,20)
                if roll <= 6:
                    print("Hawkins' attack missed!")
                elif roll < 10:
                    dmg = 6
                    player_hp -= dmg
                    print(f"Hawkins grazed you and did {dmg} damage!")
                elif roll < 15:
                    dmg = 12
                    player_hp -= dmg
                    print(f"Hawkins struck you and did {dmg} damage!")
                elif roll < 19:
                    dmg = 18
                    player_hp -= dmg
                    print(f"Hawkins landed a critical hit on you and did {dmg} damage!")
                else:
                    dmg = 25
                    player_hp -= dmg
                    print(f"Hawkins landed a critical headshot on you and did {dmg} damage!")
                print('-'*50)

        elif selection == '2' and aidkit in inventory and player_hp == hp_limit:
            if player_hp == hp_limit:
                print('-'*50)
                print("Your health is already full. The First Aid Kit can't be used at this time.")
                print('-'*50)
                heal = 0

        elif selection == '2' and aidkit in inventory and player_hp != hp_limit:
            if player_hp <= (hp_limit / 2):
                heal = int(hp_limit / 2)
                print('-'*50)
                print(f"You restored {heal} HP!")
                inventory.remove(aidkit)
            else:
                heal = hp_limit - player_hp
                print('-'*50)
                print(f"You restored {heal} HP!")
                inventory.remove(aidkit)
            player_hp += heal

            print("Without hesitation, Hawkins prepares to take another shot at you!")
            roll = random.randint(0,20)
            if roll <= 6:
                print("Hawkins' attack missed!")
            elif roll < 10:
                dmg = 6
                player_hp -= dmg
                print(f"Hawkins grazed you and did {dmg} damage!")
            elif roll < 15:
                dmg = 12
                player_hp -= dmg
                print(f"Hawkins struck you and did {dmg} damage!")
            elif roll < 19:
                dmg = 18
                player_hp -= dmg
                print(f"Hawkins landed a critical hit on you and did {dmg} damage!")
            else:
                dmg = 25
                player_hp -= dmg
                print(f"Hawkins landed a critical headshot on you and did {dmg} damage!")
            print('-'*50)
        elif selection == '2' and aidkit not in inventory:
            print('-'*50)
            print("You don't have any first aid items to use.")
            print('-'*50)

        elif selection == '3':
            print('-'*50)
            print(f"Chief Hawkins HP: {hawkins_hp}/{hawkins_maxhp}\n")
            print(f"Jack Ryder HP: {player_hp}/{hp_limit}")
            print("Available Items: ", end="")
            if aidkit in inventory:
                print(aidkit)
            else:
                print("(none)")
            print('-'*50)

        else:
            player_hp = 0
            print('-'*50)
            print("You put down your weapon and surrender to Chief Hawkins.")
            print('-'*50)
            break

    if hawkins_hp <= 0:
        print('-'*50)
        print("\nYou have taken down Chief Hawkins!!\n\nNow it's time to disarm the device!\n")
        print('-'*50)
        while True:
            print("\t1 - Enter Password to Disarm\n\t2 - Check Notes\n\t3 - Do Nothing")
            print('-'*50)
            selection = input("What would you like to do? ")
            if selection == '1':
                count = 1
                while count < 5:
                    print('-'*50)
                    pw = input("Password: ")
                    if pw == password:
                        print('-'*140)
                        print(f"{"Congratulations! You successfully disarmed the device and saved the city!":^140}\n{"Great work, Jack!":^140}\n\n{"GAME OVER":^140}")
                        print('-'*140)
                        count = 5
                        restart()
                        break
                    else:
                        count += 1
                        print('-'*50)
                        print("The password you entered is incorrect.")
                        print(f"{5 - count} attempts remaining.")
                        print('-'*50)
                        if count == 5:
                            print('-'*140)
                            print(f"{"You stand idly by as the device detonates and the deadly virus is released.":^140}\n{"The city is doomed.":^140}\n\n{"GAME OVER":^140}")
                            print('-'*140)
                            restart()
                            break
                break
            elif selection == '2':
                print('-'*50)
                if not notes:
                    print("(You don't have any notes yet.)")
                else:
                    for i in notes:
                        print(f">>> {i}")
                print('-'*50)
            elif selection == '3':
                print('-'*140)
                print(f"{"You stand idly by as the device detonates and the deadly virus is released.":^140}\n{"The city is doomed.":^140}\n\n{"GAME OVER":^140}")
                print('-'*140)
                restart()
                break
            else:
                print('-'*50)
                print("You have made an invalid selection. Please try again.")
                print('-'*50)
    else:
        print('-'*140)
        print(f"{"Chief Hawkins got the best of you and unleashed the deadly virus.":^140}\n{"The city is doomed.":^140}\n\n{"GAME OVER":^140}")
        print('-'*140)
        restart()

### starts the application

start()