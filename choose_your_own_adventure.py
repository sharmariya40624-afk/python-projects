name = input("Type your name:")
print("welcome",name,"to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you ike to go? ").lower()

if answer == "left":
     answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across:")

     if answer == "swim":
       print("you swam across and were eaten by an alligator.")
       
     elif answer == "walk":
       print("you walked for many miles, ran out of water and you lost the game.")
   
     else:
       print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back?")

    if answer == "back":
      print("You go back and lose.")

    elif answer == "cross":
       answer = input("You cross a bridge and meet a stranger. Do you talk to them (yes/no)? ")

    if answer == "yes":
       print("You talk to the stranger and they give you gold. You win!")
       
    elif answer == "no":
       print("You ignore to the stranger and they are offended and you lose.")
       
    else:
       print("Not a valid option. You lose.")


print("Thank you for trying", name)

