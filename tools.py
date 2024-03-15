libary=[]
wishlist=[]
book_name=(input(f"enter name of book you have"))
libary.append(book_name)
book_name=(input(f"do you have another book"))
if book_name:
    libary.append(book_name)
print("\nyour libary" , libary)

book_name=(input("enter your wish_book"))
wishlist.append(book_name)
book_name=(input("enter your wish_book you can skp if you pres enter"))
if book_name:
    wishlist.append(book_name)
    print("\n wish_book",wishlist)
book_got=(input("enter name of book you got it if not prees enter "))
if book_got:
    libary.append(book_got)
    wishlist.remove(book_got)
book_gave=(input("enter name of book you want to give to anyone if you dont want press enter\n"))
if book_gave in libary:
 libary.remove(book_gave)
print(libary)
print(wishlist)

countries=["finland","sweden","grmene","italy","espen",]
countries[1]="ruotsi"
print(f"{countries [-1]}\n{countries [0]}")

class_a=["abdullah","tom"]
class_b=["jak","roni"]
class_a.extend(class_b)
print(class_a,)

examplelist = []
while True:
    examplelist.append(input("insert data"))
    if len(examplelist)>=5:
        break
    else:
        continue
print(examplelist,len(examplelist))
for i in examplelist:
    print(i)

    nnumber=input("enter numbers and but comma betwen them \n")
number = nnumber.split(", ")
print(number)
print(type(number))

books=["book1","book3","book4"]
books.insert(1,"book2")
books.insert(4,"book5")
got_book="book6"
books.append(got_book)
got_book="book7"
books.insert(6,got_book)
print(books)

shope_basket=[["apple","banana"],["milk","water"]]
print(shope_basket)
input("press enter to cahnge the content ")
shope_basket[0].insert(0,"orange")
shope_basket[0].append("kiwi")
shope_basket[1].insert(0,"coffee")
shope_basket[1].append("tea")
shope_basket[1].remove("water")
number=[1,2,3]
shope_basket.append(number)
print("here is the updated shope_basket")
print(shope_basket)

guest=["Abdullah","Ali","Amer"]
name=input("enter ur name \n").capitalize()
if name in guest:
    print("welcome")
else:
    print("sorry ur name not in the list")
name=[]
while True:
    name.append(input("name"))
    if len(name)>=5:
         break 
    else:
         continue
for item in [name]:
     print[item]

name=[]
def functionexample():
 while True:
    name.append(input("name: "))
    if len(name)>=5:
        for i in name:
           print(i)
        print("\n","exiting"),exit()
functionexample()
 
name={"abdullah":"student",
      "abdullah":"student",
      "abdullah":"student"}
for x in name:
    print(name[x])
    print("\n") 
for x,y in name.items():
    print(x,y)

colors=["red","blue","green","yellow"]
for x in colors :
    if x=="red":
        print(f"this is my favoert color is {x}")
    else:
        print(x)
        
number={1,2,3,4,5,6,7,8,9,10}
while True:
 for y in number:
    if y%2==0:
        print(F"{y}")
 else:
    break
print("done the loop")

attendees=["ali","abdullah","amer"]
for person in attendees:
    print(person)
    name=input("if person come type yes or no type no: ")
    if name=="yes":
        print("attendance confirmed !")
    else:
        print("attendance not confirmed !")
    print("---------")

      
    
armorslots=("head","chest","hande")
for i in armorslots:
    print (i)
print(armorslots)
tuplechange= list(armorslots)
print(tuplechange)
tuplechange.pop(1)
armorslots= tuple (tuplechange)
print(armorslots)
        
print("welcome")
items=[]
prices=[]
items_of_items=int(input("how mane itmes u have: "))
if items_of_items>0:
   print("ltes caont it ")   
   for i in range(items_of_items): 
      name=input(f"enter name of itme number {i}: ")
      items.append(name)
      price=int(input("enter price of {price}: "))
      prices.append(price)
see_items=input("do u want see ur items: yes or no: ")
if see_items=="yes":
   print(items)
see_prices=input("do u want to see prices: yes or no: ")
if see_prices=="yes":
   print(sum(prices))
else:
   print("have good day")
########
numbers=[1,2,3,4,5]
total=0
print("lets add each number to the next")
for i in numbers:
    total +=i
    print(f"->{total}")
print(f"the total number is: {total}")


names=input("enter ur names and the last nime of ur friends sperated by a comma: ").split(", ")
abbreviated_names =[]
for name in  names:
     name_parts = name.split()
     print(name_parts)
     first_name=name_parts[0]
     last_name=name_parts[1]
     short_name=first_name[0]
     short_last_name=last_name[0]
     abbreviation=short_name + "<-->" + short_last_name + "."
     abbreviated_names.append (abbreviation)
print("abbreviated_names")
for x in abbreviated_names:
     print(x)

ur_input=input("enter a sentence:  ")
word=ur_input.split()
flep = word[::-1]
print(flep)
word_flep=" ".join(flep)
print(word_flep)

the_dictinory={
    "abdullah" : "student in class a" ,
    "ali" : "student in class c ",
    "markus" : "teacher in class a"
}
while True:
    ur_input=input("search term:").lower()
    if ur_input in the_dictinory:
       print(F"{ur_input} : {the_dictinory[ur_input]}")
       break
    else:
        print("ur_input not in the dictinory: ")

import sys
name=[]
for x in range(1,25):
      name.append(x)
      ur_input=len(input("enter ur name : ") )
      if ur_input== 25:
          break
      else:
         continue         
print(name)
sys.exit("done")

ansewer="10"
ur_ansewr=""
caunt=0
limit=3
lose=False
while ansewer !=ur_ansewr and not  lose:
    if caunt < limit:
        ur_ansewr=input("enter number: ")
        caunt +=1
    else:
        lose=True
if lose:
    print("u lose")
else:
    print("win")

ansewer="10"
ur_ansewr=""
for ur_ansewr in range(3):
    ur_ansewr=input("enter number. ")
    if ur_ansewr == ansewer:
         break
    if ur_ansewr ==3:
          break
    else:
         continue
if ur_ansewr== ansewer:
     print ("win")
else:
     print("lose")
    
namelist=[]
tablelist=[]
for x in range(1,25):
    tablelist.append(x)
while True:
    ur_input=input("enter the name: ")
    if not ur_input:
        break
    elif len(namelist)>=25:
        break
    else:
        namelist.append(ur_input)
for x in range(0,len(namelist)):
    print (namelist[x]," : ",tablelist[x])
print("done")

def my_faction (name,age):
    name=input("enter ur name: ")
    age=input("enter ur age: ")
    print(name , age)

def cube(num):
    return num*num*num
result=cube(3)
print(result)

def sub(num, num2):
    return num + num2
print (sub(5,5))

def max_num(num1,num2,num3):
    if num1>=num2 and num1>= num3:
        return num1
    elif num2>=num1 and num2>= num3:
        return num2
    else:
        return num3
print(max_num(3 ,2,5))

try:
    ur_input=int(input("enter some number:"))    
except:
    print("invalid: ")
try: 
    ur_input=int(input("enter some number:")) 
    print(ur_input)   
    x=10/0
except ZeroDivisionError as error:
    print(error)
except ValueError as error :
    print(error)

def power (num1,num2):
    result=1
    for x in range(num2):
        result= result *num1
    return result
print(power(3,4))

my_list=[[1,2,3],[4,5,6],[7,8,9]]
for row in my_list:
    for colum in row:
        print(colum**2)

try:
   ur_input=int(input("enter a number: "))
   x=10/0
except ValueError as error:
    print(error)
except ZeroDivisionError as error:
    print(error)
print("done")

import math
print("welcome to my program.")
name_list=[]
result=[]

try:
    for name_listin in (range(1,3)):
        name=input("enter  the name of student: ")
        name_list.append(name)
        exame1=int(input("enter the total number of exame: "))
        exame2=int(input("enter the total number of exame: "))
        exames=exame1 + exame2
        the_result= exames / 2
        result.append( the_result)
except ValueError as error:
    print(error)
print(f"{name_list}::{result}")
print("done")
    
ur_input=input("enter ur input: ")
try:
    ur_input=int(ur_input)
    result= ur_input*ur_input
except Exception as e:
    print(f"ERROR:{e}")
else:
    print(result)
     
name_list=[]
while True:
    ur_input=int(input("enter name of ur student: "))
    try:   
        if ur_input == 100:
            break
        name_list.append(ur_input)
    except Exception as error:
        print (error)
print(name_list)

# massage to encryption software
# use import sting &and the alpeapet
# and move 2 step and fix y,z and fix " "

import string
alphapet=string.ascii_lowercase
# alphabet_length=len(alphapet)
word=input("enter a word: ").lower()

encrypted_word=""

for letter in word:
   if letter == " ":
    encrypted_word += " "
   else:
    original_position=alphapet.index(letter)
    new_position = (original_position + 2)%26 
    encrypted_word += alphapet[new_position]
    
    
print(f"here is the encrypted word: {encrypted_word}")

print(pow(5,2))
print(abs(10.19))
print(abs(10.19))
print(min(1,10,20,-50-100))
print(max(1,10,20,-50-100))

scop=3 
n=int(input("how many scop u want: "))
if n %scop ==0 :
    print("ok")
else:
    print("we dont have this option")



a="hello helsnki"
reversed_words=' '.join(a.split()[::-1])
print(reversed_words)
print(a[::-1])      

number=[]
while True:
  
    ur_input=int(input("enter number:"))
    
    if ur_input== 0:
        break
    else:
        number.append(ur_input)

print(max(number))

number=[]
while True:
  
    ur_input=int(input("enter number:"))
    
    if ur_input== 0:
        break
    else:
        number.append(ur_input)
max_number = max(number)
number.remove(max_number)
max2_number=max(number)
print(max2_number)


mylist=[]
n=input("enter:")
mylist.append(n)
print(mylist)
print(mylist[0][2])
print(mylist[0][-2])
print(mylist[0][0:5])
print(mylist[0][0:-2])
print(mylist[0][0:-2:2])
print(mylist[0][-1:0])

print(mylist[0][1:-1:3])









      


