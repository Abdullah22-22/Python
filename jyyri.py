import string

alphapet=list(string.ascii_lowercase)
for i in range(len(alphapet)):
    if i % 2 == 0:
        alphapet[i]= alphapet[i].upper()
    else:
        alphapet[i]= alphapet[i].lower()
print("".join(alphapet))


z=str(input("enetr:"))

print("z")


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


number=[]
while True:
  
    ur_input=int(input("enter number:"))
    
    if ur_input== 0:
        break
    else:
        number.append(ur_input)

print(max(number))

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


n=int(input("enter number:"))
for x in range(n):
    number,string=input(f"enter{x+1}: ").split(" ")
    number=float(number)
    if string == "M":
        V=number * 3.2808
        print("{:.6F}".format(V),("FT"))
        
    elif string == "C":
        V1=number *1.8 
        
        print("{:.6F}".format(V1),("F"))
        
    elif string == "G":
        V2= number * 0.002205
        print("{:.6F}".format(V2),("LBS"))
       
    else:
        break
    
    
min_temp=float(input("Enter the minimum temperature: "))
max_temp=float(input("Enter the max temperature : "))


while True:
    n=float(input("enter the temperature:"))

    if n >= min_temp and n <= max_temp :
        print("Nothing to report")
    elif n == -999:
        break
    else:
        print("Alert!")

    
the_number=int(input("::"))
tries=0
while True:
    n=int(input("enter number from (1-10)"))
    tries +=1
    if the_number> n :
        print("it is more")
    elif the_number < n:
        print("it is less")
    elif the_number == n:
        print("you win")
        break
    else:
        print("try agin")

print(tries)
        

n=int(input("enter"))
x=0
print(n*("+___ "))
while x < n:
    print("|", x+1,"/",  end= '')
    x= x+1
print(n* (""))
print(n*("|___\\"))
print(n*("|    "))