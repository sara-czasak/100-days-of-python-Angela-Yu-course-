print("*** WELCOME TO THE ADVENTURE GAME ***")

path1 = input("To start your journey choose which path you will take:\n- LEFT\n- RIGHT\n").lower()

if path1 == "left":
    print("You choose to go left..")
    path2 = input("You see a large river with a strong current ahead. What do you do?\n- SWIM ACROSS\n- WAIT FOR A BOAT\n").lower()
    if path2 == "wait for a boat":
        print("You wisely choose to wait for a boat..")
        path3 = input("A boat arrives and it takes you across the river.\nNow you face a wall with two doors. Above the doors a sign reads:\n*** ONE OF THESE DOORS LEAD TO FREEDOM AND WEALTH, THE OTHER HOLDS CERTAIN DOOM ***\nWhich door do you choose?\n- 1\n- 2\n")
        if path3 == "1":
            print("You open the door..")
            print("before you stands a huge chest with gold coins spilling out")
            print("*** YOU WIN ***")
            game_over = True
        elif path3 == "2":
            print("You walk through the second door..")
            print("As soon as you enter the door behind you closes and vanishes leaving you stuck in a dark room for all eternity")
            print("*** GAME OVER ***")


    elif path2 == "swim across":
        print("You try to brave the rapids but you fail. As you sink into the water you have a fleeting thought: 'I should have waited for the boat...'")
        print("*** GAME OVER ***")

elif path1 == "right":
    print("You choose to go right..")
    print("An unfortunate turn takes you to a clearing full of angry lions..")
    print("You try to escape, but it's too late..")
    print("*** GAME OVER ***")

