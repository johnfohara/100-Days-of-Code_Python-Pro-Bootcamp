print(r'''    
                           {}           {}
                             \  _---_  /
                              \/     \/
                               |() ()|
                                \ + /
                               / HHH  \
                              /  \_/   \
                            {}          {}          
    
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
 
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n\n")

turn_1 = input("You\'re at a fork in the road. "
               "\nTo the left is the mouth of a cave. "
               "\nTo the right is a well-worn path with white flowers along the edges. "
               "\nWhich way do you go? \n Type \"Left\" or \"Right\"\n\n").lower()
if turn_1 == "left":
    turn_2 = input("\n\nThe cave descends into an underground freshwater pool. "
                   "\nIt seems safe enough to swim, but in the darkness you can't see under the water. "
                   "\nA sign shows departure times for a boat, with the next one arriving in 30 minutes. "
                   "\nWhat do you want to do? \nType \"wait\" or \"swim\"\n\n").lower()
    if turn_2 == "wait":
        turn_3 = input("\n\nThe boat takes you across the water to a castle with three doors, "
                       "each a different color. \nWhich door do you open? "
                       "Type \"red\", \"yellow\", or \"blue\"\n\n").lower()
        if turn_3 == "red":
            print("\n\nIt's a room full of fire. GAME OVER")
        elif turn_3 == "blue":
            print("\n\nHungry hyenas await you. You are eaten by them. GAME OVER")
        elif turn_3 == "yellow":
            print("\n\nYou found the treasure. You Win!")
        else:
            print("\n\nYou chose a hidden door. It opens into the vacuum of space. "
                  "You float into oblivion. GAME OVER")
    else:
        print("\n\nYou begin to swim. \nThe water is cool and refreshing. "
              "\nAbout halfway to shore, you feel a tug on your leg. "
              "\nYou look down into the water but can't see in the darkness. "
              "\n\nThe next tug is harder. \nYou're pulled under. \nGAME OVER.")
else:
    print(
        "\n\nYou start down the path and turn a corner. "
        "\nThe horizon opens up before you and takes your breath away. "
        "\nYou're looking out over the mountains and don't notice a giant hole "
        "in the middle of the trail. \nYou fall in the hole. \nGAME OVER.")


