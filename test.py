number =input("please enter two digit \n")
first_number=int(number[0])
second_number=int(number[1])
print(first_number+second_number)
print(2*3-6+9/3)


x = input("input for x: " )
x = int(x)
y = input("input for y: " )
y= int(y)
z = x + y
print(z)

str_length= input("type length?:\n")
str_width= input("type width?:\n")
str_price =input ("how much for 1 m? :\n")
# convert type
length = float(str_length)
width = float(str_width)
price = float  (str_price)
# calculate the area length*width
area=length*width
total_price = price*area
str_area = str(area)
str_toatal_price = str(total_price)
print("the total area is"+ str_area)
print ("give the guy:" + str_toatal_price)

# division /
# floor divison //

total_minuttes = input ("type the number of minutes \n") # minuttes str
int_minutes = int(total_minuttes)  # change from the str to in
hours = int_minutes // 60 # change from min to h
minutes = int_minutes % 60 
print ("this cours is : " +str(hours) + "hours and "+ str(minutes ) + "minutes long"  )

age = input ("how old are you \n")
int_age = int (age)
year = 2023
born_in = year - int_age
str_born_in = str(born_in)
print ("you born inthe year: "+ str_born_in)

int_age = int(input("how old are you? \n"))
print(f"you were born in the year{2024-int_age}")
 
# f_srring 

# if or else
print ("welcom to my app")
age = (int(input("how old are you \n")))
if age > 18:
   print("you can ues it")
else:
   print("you cant use it ")

print ("welcom to my app")
number=float(input("enter a number \n"))
if number > 0: 
    print ("postive")
elif number < 0:
     print (" negative")
else:
     print("the number is zeroe")

for i in range(10) :
     grades = float(input(f"enter the grades for person {i + 1}:  \n"))
if grades >= 90 :
    print("excellent")
elif  grades >= 70 :
    print("good")
elif grades >= 50 :
    print ("ok")
else:
    print ("weak")

number=(int(input("enter ur number \n")))
if number == 13:
    print ("win")
else:
    print ("lose")  

choose = (str(input("c yes no maybe \n")))
if choose == "yes":
    print("yes")
elif choose == "no":
    print("no")
elif choose== "maybe":
    print ("maybe")
else:
    print("wrong")  

    number = int(input("enter number \n"))
if number ==7:
    print("win")
else:
    print(f"lose, but the number is{7}")

#   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
    area= input ("choes (Helsnki)(Espoo)(Vantaa)\n")
if area.lower()=="helsnki " or area.loweree()=="eSPOO" or area.lower()=="vantaa":
   print(f"soryy{area}is not here")

name=input("entr ur name \n")
password=(input("enter ur pasword \n"))
if name.lower () == "abdullah" and password =="123":
    print ("go head")
else:
    print("try agin")

    nationality = input ("wher are u from \n "). lower ()
if nationality== "finnish":
 print("go to the  2th step")

 is_18 = input("how old are u \n  ").lower()
if is_18 =="18":
 print("you can get id")
else:
 print("we cnat help u")

 print("""̶T̶̶y̶̶p̶̶e̶ ̶s̶̶o̶̶m̶̶e̶̶t̶̶h̶̶i̶̶n̶̶g̶ ̶t̶̶o̶ ̶s̶̶t̶̶a̶̶r̶̶t̶""")
 

 print("welcomme")

number=int(input("you have 2 boxs choes 1🎁,2🎁,\n"))
if number==1:
    print("win")
door=int(input("you have 3 doors choes 1🚪2🚪3🚪  \n"))
if door==1:
  print("win")
elif door==2:
 print("you got 🍒🍒")  
elif door==3: 
     print("you got🖕🖕 ")

elif number==2:
  print("you got 🍒🍒") 
else:   
    print("wrong try agin") 


