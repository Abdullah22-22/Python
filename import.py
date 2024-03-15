import random
pin=int(input("enter pin code\n"))
my_random_number=random.randint(1000,9999)
print(my_random_number)
if len(str(pin))!=4:
    print("enter 4 digits")
elif pin==my_random_number:
    print("welcom")
else:
    print("somting wrong")

import random   #random.random() that means float if want get  more then one for exmpol 5
number=random.random()     #random.random()*5   #random.random()*100
print(number)

import random
input("prees enter to start the game")
my_random_number=random.random()
if my_random_number<=0.5:
    print("heads")
else:
    print("tails")


print("welcome to my game")
print("choess one of thoes")
import random
game=input("choes 1 or 2\n")
choess1=random.randint(1,2)
if game==1:
  print("heads")
elif game==2:
  print("tailas")
else:
 print ("erro")
  
countries=["finland","sweden","grmene","italy","espen",]
countries[1]="ruotsi"
print(f"{countries [-1]}\n{countries [0]}")


import random
print("welcome to 'whose wallet:")
name = input("give me the list of the name but but betwen the names comman ").split(", ")
selected_name = random.choice(name)
print(f"ask {selected_name} to pay for food")

import random
numbers=[1,2,3,4,5,6,7,8,9,0]
print(random.choices(numbers, k=4))

import random
import string
random_5=random.choices(string.ascii_letters,k=5)
print(random_5)



import string
ur_input=input("enter ur words: ")
ur_sentence=" "
for x in ur_input:
    if x not in string.punctuation:
        ur_sentence += x
print("\n\*** here isthe same sentence with out punctuation***",ur_sentence)

import random
import string
print("welcome to the password generator.")
ur_input=int(input("enter the total of ur pasword: "))
my_letters=int(input("enter the number of letters in the pasword: "))
my_numbers=int(input("enter the number of   the pasword: "))
my_sympols=int(input("enter the number of sympols in the pasword: "))
if ur_input !=(my_letters+my_numbers+my_sympols):
    print("invalid input the sum of letters, numbers, sympols dosent match with ur_input:")
else:  
    the_pasword=(random.choices(string.ascii_letters,k=my_letters)+
        random.choices(string.digits,k=my_numbers)+
        random.choices(string.punctuation,k=my_sympols ) )              
    random.shuffle(the_pasword)
    pasword="".join(the_pasword)
    print("password generator", pasword )


import random
secrt_number= random.randint(1,10)
guess=int(input("gues number between 1-10: "))
while guess!=secrt_number:
    if guess<secrt_number:
        guess=int(input("too low! guess try agin: "))
    else:
        guess=int(input("too high! guess try agin: "))
print("u win")

import math
result=[]
history=[]
def operator ():
    num1=int(input("enter the first number: "))
    operator=input("enter ur operator:  ")
    num2=int(input("enter the second number: "))
    if operator =="+":
       result=(num1+num2)
       history.append(result)
       print(result)
       print(history)
    elif operator =="-":
      result=(num1-num2)
      history.append(result)
      print(result)
      print(history)
    elif operator =="/":
       result=(num1/num2)
       history.append(result)
       print(result)
       print(history)
    elif operator =="*":
       result=(num1*num2)
       history.append(result)
       print(result)
       print(history)
    elif operator =="**":
       result=(num1**num2)
       history.append(result)
       print(result)
       print(history) 
    else: 
       print("somting wromg:")
while True:
    operator ()  


import random
words=["good","bad","yes"]
random_words=random.choice(words)
display=[]
for letters in random_words:
    display.append("_")
print(display)
live=6
while "_" in display and live >0:
    ur_input=input("enter some letter: ").lower()
    display.append(ur_input)
    if ur_input not in display:
        live -=1
    for position in  range(6,len(random_words)):
        if random_words[position]== ur_input:
            display[position]= ur_input
        else:
            ur_input[display]==6
            
            
    print(display)
    print(f"you have mor{live}")

if live == 0:
    print("u lose")
else:
    print ("u win")

import random
number=[1,2,3,4,5,6,7,8,9,10]
print("welcome to my game")
print("try to guess number fom 1-10")
the_random=random.choice(number)
try:
    ur_input=int(input(f"enter number from {number}: "))
except ZeroDivisionError as error:
    print(error)
except ValueError as error:
    print(error)
except:
    print("invalid inout")
print(the_random)
if the_random==ur_input:
    print("win")
else:
    print("tyr agin ")

try:
    ur_input=int(input("enter a number:  "))
    print(ur_input)
except ValueError as err:

    print(err)
print("done")

import random
try:
    random_list=[x for x in range(1,11)]
    the_guess=random.choice(random_list)
    ur_input=[]
    ur_input=int(input(f"enter number from{random_list}: "))
    if the_guess==ur_input:
         print("good")
    else: 
        print("wrong")
except ValueError as error:
    print(error)
print(the_guess)
print("done")

class employee:
    def __init__(self,name,age,department,is_manger) :
        self.name=name
        self.age=age
        self.department=department
        self.is_manger=is_manger


    