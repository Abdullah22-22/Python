import random
print("welcome to my game")
print("choess one of thoes")
print("2 for random.randint")
print("1 for random.random")
choes=input("choes 1,2\n")
if choes == "1":
  random_number=random.random()
  if random_number >=0.5:
     computer_result= "heads"
  else:
     computer_result= "tails"
elif choes=="2":
   random_number=random.randint(0,1)
   if random_number==0:
      computer_result= "heads"
   else:
       computer_result= "tails"
else:
   print("number invalid") 
user=input("enter ur guess(heads or tails)")   
if user.lower()== computer_result.lower():
   print("you win") 
else:
   print("you lose")
print(f"{computer_result}")   

import random
print("welcome to 'whose wallet:")
name=input("give me the list of the name but but betwen the names comman  ").split(", ")
print(f"ask{random.choice(name) } to pay for food")

# length=len(names)-1
# random_number= random.randint(0, length)
# random_person =names[random_number]
# print(f"{random_person}")

print("welcome to place thre rabbit")
list1=[["🍁","🍁","🍁"],["🍁","🍁","🍁"],["🍁","🍁","🍁"]]
print(f"{list1[0]}\n{list1[1]}\n{list1[2]}")
print(" \n where shuoldd the rabbit go?🐇")
postion=input("enter a postion for the rabbit\n")
row=int(postion[0])
column=int(postion[1])
list1[row][column]="🐇"
print(F"{list1[0]}\n{list1[1]}\n{list1[2]}")
#if want the computer calculate from 1 list1[row-1][column-1]
import random
rock_ascii="🪨"
paper_ascii="📃"
scissors_ascii="✂️"
print("wlcome to the Rock, Paper, Scissors game: ")
roles=["1) You chooes and the computer chooeses:","2) rock smashes Scissors -> ruok Win","3) Scissors cut Paper -> Scissors Win ","4) Paper covers rock -> Paper win"]
customer=input("press enter to continue or type (Yes) for the rules help\n")
if customer.lower()=="yes":
    print(f"{roles[0]}\n{roles[1]}\n{roles[2]}\n{roles[3]}")
enter_choice=input("enter ur choice :").lower()
if enter_choice not in ["rock","paper","scissors"]:
  print("wrong")
else:
    if enter_choice=="rock":
       print(f"your choes is:\n {rock_ascii}")
    elif enter_choice=="paper":
       print(f"your choes is :\n{paper_ascii}")
    else:
     print(f"your choes is :\n{scissors_ascii}")
computer_choice=random.choice(["rock","paper","scissors"])
if computer_choice=="rock":
    print(rock_ascii)
elif computer_choice=="paper":
    print(paper_ascii)
else:
     print(scissors_ascii)

if computer_choice==enter_choice:
   print("tie")
elif(
(computer_choice=="scissors" and enter_choice=="rock" )
or
(computer_choice=="rock" and enter_choice=="paper" )
or
(computer_choice=="paper" and enter_choice=="scissors" )):

   print(f"you win{enter_choice}")
else:
   print(f"you lose\n{enter_choice}")

# import random
# word = ["good","bad","ugly"]
# random_word=random.choice(word)
# list=[]
# for letter in word:
#     list.append("_")
#     #list += "_"
# print(list)
# while "_" in random_word:
#     guess=input("enter a letter a: ").lower()
#     for postion in range(len(random_word)):
#         if random_word[postion] == guess:
#          list[postion] = guess

# print(list)
# print(random_word)


import turtle 

wind=turtle.Screen()# make the windo of the  game
wind.title("ping pong") #make the name of the game
wind.bgcolor("black")# to make the bakceond of the game
wind.setup(width=800, height=600)
wind.tracer(0)# to block the update of the screen 

paddele1= turtle.Turtle()#intialize turtle object(shape)
paddele1.speed(0)# set the speed of the animation
paddele1.shape("square")# set the look of the object
paddele1.color("blue") # make the color of object
paddele1.penup() #stop the object to make lines in screen
paddele1.goto(-350,0) #set the postioin of object
paddele1.shapesize(stretch_wid=5,stretch_len=1)#make the object in the look u want it 

paddele2= turtle.Turtle()
paddele2.speed(0)
paddele2.shape("square")
paddele2.color("red")
paddele2.penup()
paddele2.goto(350,0)
paddele2.shapesize(stretch_wid=5,stretch_len=1)

ball= turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx =0.3
ball.dy =0.3

#score
scoer1=0
scoer2=0
scoer =turtle.Turtle()
scoer.speed(0)
scoer.color("white")
scoer.penup()
scoer.hideturtle()
scoer.goto(0,260)
scoer.write("player 1: 0 player 2:0",align="center",font=("courier",24,"normal"))

#faction
def paddele1_up():
    y=paddele1.ycor() # get the y coordinate of the paddel1
    y += 20  # set the y increass be  20
    paddele1.sety(y) # set the y of the paddele1 in the new y postion

def paddele1_down():
    y=paddele1.ycor()
    y -= 20
    paddele1.sety(y)

def paddele2_up():
    y=paddele2.ycor()
    y += 20
    paddele2.sety(y)

def paddele2_down():
    y=paddele2.ycor()
    y -= 20
    paddele2.sety(y)
#keybord bindings
wind.listen()   # tell the window to expect kepyord input
wind.onkeypress(paddele1_up, "w")   #when press w the paddele go up
wind.onkeypress(paddele1_down, "s") #when press s the paddele go down
wind.onkeypress(paddele2_up, "Up")
wind.onkeypress(paddele2_down, "Down")


while True: # make the loop game 
    wind.update()   #update the game when the loop work in evertime
    #move ball 
    ball.setx(ball.xcor() + ball.dx)     #ball start at 0 evertime when loop work the ball +2 x 
    ball.sety(ball.ycor() + ball.dy)    #ball start at 0 evertime when loop work the ball +2 y 
    #boeder check
    if ball.ycor() >290:    # if ball go to top border get back in the studiom
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() <-290:   # if ball go bottom border get back in the studiom
        ball.sety(-290)
        ball.dy *= -1  #reveres the x disectio

    if ball.xcor() >390:    # if ball is at right border
        ball.goto(0, 0)  #return the ball to center
        ball.dx *= -1   #reveres the x disectio
        scoer1 +=1  
        scoer.clear()
        scoer.write(f"player 1: {scoer1} player 2:{scoer2}",align="center",font=("courier",24,"normal"))
    
    if ball.xcor() <-390:   # if ball is at left border
        ball.goto(0, 0)  #return the ball to center
        ball.dx *= -1   #reveres the x disectio
        scoer2 +=1
        scoer.clear() 
        scoer.write(f"player 1: {scoer1} player 2:{scoer2}",align="center",font=("courier",24,"normal"))

    #when the paddel and the ball tuochet
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor() < paddele2.ycor() + 40 and ball.ycor() > paddele2.ycor()- 40 ):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor()< - 340 and ball.xcor()>-350) and (ball.ycor() < paddele1.ycor() + 40 and ball.ycor() > paddele1.ycor()- 40 ):
        ball.setx(-340)
        ball.dx *= -1



