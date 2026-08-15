print('''
 -----------------------------.----------------------------------.
|                             |                                  |
|    .    .    ,---------     |     ------------------------.    |
|    |    |    |              |                             |    |
|    |    `----"--------------'    ,-------------------.    |    |
|    |                             |                   |    |    |
|    :--------------.--------------"----     ,---------:    |    |
|    |              |                        |         |    |    |
|    :---------     |    .    ,---------.    |    .    |    `----:
|    |              |    |    |         |    |    |    |         |
|    |     ---------'    |    :----     |    |    |    |    .    |
|    |                   |    |         |    |    |    |    |    |
|    `-------------------'    |     ----'    |    |    |    |    |
|                             |              |    |    |    |    |
:--------------.---------.    :--------------'    |    :----'    |
|              |         |    |                   |    |         |
|    .    .    |    .    |    |    ,--------------:    `----     |
|    |    |    |    |    |    |    |              |              |
|    |    |    "    |    |    |    |     ---------"---------.    |
|    |    |         |    |    |    |                        |    |
|    |    `---------"----'    |    |    ,---------.    .    |    |
|    |                        |    |    |         |    |    |    |
|    :---------.--------------:    |    |    .    |    |    |    |
|    |         | X            |    |    |    |    |    |    |    |
|    "    .    `---------     |    |    `----'    |    `----'    |
|         |                   |    |              |              |
`---------"-------------------'    `--------------"--------------''')

print("Welcome to treasure island. Your mission is to find the treasure")
direction = input("Where do you want to go? Left or Right? ")
if direction == "Right":
    print("You fell into a hole. Game Over")
if direction == "Left":
    swimorwait = input("Swim or wait? ")
    if swimorwait == "Swim":
        print("You got attacked by an angry trout. Game Over")  
    else:
        door =input("Which door? Red, Blue or Yellow? ")
        if door == "Red":
            print("You got burned by fire. Game Over")
        elif door == "Blue":
            print("You got eaten by beasts. Game Over")
        elif door == "Yellow":
            print("You Win!")
        else:
            print("Game Over")