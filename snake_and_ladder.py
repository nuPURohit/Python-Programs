import random

snake={19:5,55:27,98:69}
ladder={7:21,40:62,80:93}

pos_1=0
pos_2=0
throw_1=0
throw_2=0
turn=1

while(pos_1<100 and pos_2<100 ):
    if turn%2!=0:
        throw_1=throw_1+1
        print("user 1's chance")
        dice_1 = random.randrange(1, 7)
        print("dice_1=",dice_1)
        if dice_1 == 6 and pos_1==0:
            pos_1=1
        elif pos_1>=1:
            pos_1 = pos_1 + dice_1
            print("pos_1=",pos_1)
            for key,value in snake.items():
                if pos_1 == key:
                    pos_1 = value
                    print("Snake ate u up! :( ")
                    print("pos_1=", pos_1)
            for key,value in ladder.items():
                if pos_1 == key:
                    pos_1 = value
                    print("You climbed the ladder! :) ")
                    print("pos_1=", pos_1)
    else:
        throw_2 = throw_2 + 1
        print("user 2's chance")
        dice_2 = random.randrange(1, 7)
        print("dice_2=", dice_2)
        if dice_2 == 6 and pos_2==0:
            pos_2=1
        elif pos_2>=1:
            pos_2 = pos_2 + dice_2
            print("pos_2=", pos_2)
            for key,value in snake.items():
                if pos_2 == key:
                    pos_2 = value
                    print("Snake ate u up! :( ")
                    print("pos_2=", pos_2)
            for key,value in ladder.items():
                if pos_2 == key:
                    pos_2 = value
                    print("You climbed the ladder! :) ")
                    print("pos_2=", pos_2)
    turn = turn + 1

if pos_1>=100:
    print("user 1 is the winner after",throw_1,"throws")
    print("User 2 is still at",pos_2)
elif pos_2>=100:
    print("User 2 is the winner after",throw_2,"throws")
    print("User 1 is still at", pos_1)







