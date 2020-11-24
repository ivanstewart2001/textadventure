import time
import sys

CHEST_LOCKED = "The chest is locked!"
CLOSE_DOOR = "The door closes."
DOOR_CLOSED = "The door is closed."
DOOR_DESC_CLOSED = "The door is made of heavy oak, but is unlocked."
DOOR_DESC_OPEN = "The open door is made of heavy oak"
HALL_DESC = "You enter a long stone hallway, lit by torches. To the North is a room with a fireplace and a chest. To the east is a room with a key on a table. To the west is a dark cell."
KEY_DESC = "You enter a sparse room with a small wooden table."
KEY_DESC_WITH_KEY = KEY_DESC + " There is a small golden key on the table."
KEY_GET = "You pick up the key. It is gold-colored and weighs a lot."
LOOK_CHEST = "The chest is large and made of oak."
LOOK_FIRE = "The fire is roaring."
LOOK_KEY = "The key is made of gold."
OPEN_DOOR = "The door opens."
SORRY = "Sorry."
START_DESC = "You are in a cold, dark, stone room. There is a large oak door to the East."
TREASURE_ROOM_DESC = "You enter a lavish living space. There is a roaring fire in a fireplace, and an enormous wooden chest."
WIN = "You have retrieved the treasure! You win."

# Here are some handy constants for recognizing your locations.
ROOM_HALL = "hall"
ROOM_KEY = "key"
ROOM_START = "start"
ROOM_TREASURE = "treasure"

# And some variables. You may need to add some more here.
door_open = False
location = ROOM_START
won = False
has_key = False

# Start by printing the first room description.


def time_convert(sec) :
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    return "Time lapsed = {0} hour(s): {1} minute(s) : {2} seconds".format(int(hours), int(round(mins,2)), round(sec, 2))

# Now we loop until the user finds the treasure!
input("Press Enter to start")
start_time = time.time()
timeout = time.time() + 60*1
count = 0

print(START_DESC)
#


while count <= 10 or time.time() < timeout:
    command = input("> ")
    print(count)

    if command == "quit":
        end_time = time.time()
        time_lapsed = end_time - start_time
        print(time_convert(time_lapsed))
        break # This breaks the loop and ends the game.

    if location == ROOM_START:
        if command == "open door" and not door_open:
            count += 1
            print(OPEN_DOOR)
            door_open = True
        elif command == "close door" and door_open:
            count += 1
            print(CLOSE_DOOR)
            door_open = False
        elif command == "look at door":
            count += 1
            if door_open:
                print(DOOR_DESC_OPEN)
            else:
                print(DOOR_DESC_CLOSED)
        elif command == "go east":
            count += 1
            if door_open:
                print(HALL_DESC)
                location = ROOM_HALL
            else:
                print(DOOR_CLOSED)
        else:
            print (SORRY)
            
    elif location == ROOM_HALL:
        if command == "go north":
            count += 1
            print (TREASURE_ROOM_DESC)
            location = ROOM_TREASURE
        elif command == "go east":
            count += 1
            if has_key == False:
                print (KEY_DESC_WITH_KEY)
                location = ROOM_KEY
            else:
                print (KEY_DESC)
                location = ROOM_KEY
        elif command == "go west":
            count += 1
            print(START_DESC)
            location = ROOM_START
        else:
            print(SORRY)
        
    elif location == ROOM_KEY:
        if command == "get key" and has_key == False:
            count += 1
            print(KEY_GET)
            has_key = True
        elif command == "look at key" and has_key == False:
            count += 1
            print (LOOK_KEY)
        elif command == "go west":
            print (HALL_DESC)
            location = ROOM_HALL
        elif command == "get key" and has_key == True:
            count += 1
            print(SORRY)
        elif command == "look at key" and has_key == True:
            count += 1
            print(SORRY)

        
    elif location == ROOM_TREASURE:
        if command == "look at fire":
            count += 1
            print (LOOK_FIRE)
        elif command == "look at chest":
            count += 1
            print (LOOK_CHEST)
        elif command == "go south":
            count += 1
            print (HALL_DESC)
            location = ROOM_HALL
        elif command == "open chest":
            count += 1
            if has_key == False:
                print (CHEST_LOCKED)
            elif has_key == True:
                won = True
        else:
            print (SORRY)

    if won:
        print (WIN)
        end_time = time.time()
        time_lapsed = end_time - start_time
        print(time_convert(time_lapsed))
        break
    elif count == 10:
        end_time = time.time()
        time_lapsed = end_time - start_time
        print(time_convert(time_lapsed))
        print('Looks like you ran out of moves!')
        break
    elif time.time() >= timeout:
        end_time = time.time()
        time_lapsed = end_time - start_time
        print(time_convert(time_lapsed))
        print('Looks like you ran out of time!')
        break
