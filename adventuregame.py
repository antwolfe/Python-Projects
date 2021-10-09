'''
        .-~~~~~~~~~-._       _.-~~~~~~~~~-.
            __.'              ~.   .~              `.__
          .'//                  \./                  \\`.
        .'//                     |                     \\`.
      .'// .-~"""""""~~~~-._     |     _,-~~~~"""""""~-. \\`.     Unknown
    .'//.-"                 `-.  |  .-'                 "-.\\`.
  .'//______.============-..   \ | /   ..-============.______\\`.
.'______________________________\|/______________________________`.

'''

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

l_or_r = input('''"You come to a crossroad while hiking, are you turning "left" or "right?"\n''').lower()
if l_or_r != "right":
    print("You came across a hungry and violent bear. You are dead. Very dead. Game Over.")
else:
    go_or_stay = input('''You come to a clearing of trees surrounding a hole. Do you "go" into the hole or "stay" put?\n''').lower()
    if go_or_stay != "go":
        print("You have waited until dark and the wolves are waiting for you to fall asleep. Game Over.")
    else:
        three_choices = input('''In the hole there are three large stones with carvings.\nA "chest", a "map" and a "river". Pick one up.\n''').lower()
        if three_choices == "chest":
            print("The floor opens beneath you and you fall into a deep pit filled with treasure. The fall kills you. Game Over.")
        elif three_choices == "river":
            print("You have no time to react as the cave fills with water. You are drowned. Game Over.")
        elif three_choices == "map":
            print("The wall opens next to you and reveals a map. You follow the map and it leads you to the secret of life. Congrats you won!")
        else:
            print("You lose. Game Over.")
