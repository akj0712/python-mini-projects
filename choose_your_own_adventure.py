name = input("Type your name: ")
print("Welcome",name,"to this adventure")

answer = input("You are on a dirt road and it has com to an end. Which way you wanna go(LEFT/RIGHT)?  ").lower()

if answer == "left":
    answer = input("You come to a river, You can walk around it or swim, to cross. (WALK/SWIM):  ").lower()

    if answer == "swim":
        print("You swim across and were eaten by an alligator to the death.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and eventually died.")
    else:
        print("Not a valid option. You lose")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back. (CROSS/BACK):  ")

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You crossed the bridge and see a stranger. Do you wanna talk to them? (YES/NO):  ")

        if answer == "yes":
            print("You talk to the stranger and they gave you gold. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose")
        else:
            print("Not a vaild option. You lose.")

    else:
        print("Not a valid option. You lose")

else:
    print("Not a valid option. You lose")

print("Thank you for trying", name)
