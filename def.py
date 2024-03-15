def values():
    x,y=input("enter number:"), input("enter number:")
    return x,y

def some():
    x,y = values()
    x,y= int(x),int(y)
    print("result", x+y)

some()

ur_input=int(input("enetr number"))
match ur_input:
    case 1:
        print("ok")
    case 2:
        print("good")
    case _:
        print("unvaild number")
        
def multiplication(number):
    for i in range(1,11):
        print(f"{number}x{i}={number *i}")
multiplication(7)

def cleanword(word):#wwwooorrldd
    if len(word) == 1:
        return word
    if word[0] ==word[1]:
         #print(f"before condition {word}")
         return cleanword(word[1:])
    #print(f"before returen {word}")
    return word[0]+cleanword(word[1:])


print(cleanword("wwwooorrldd"))

x=[1,2,3,]
if all(x):
    print(True)
else: 
    print(False)

a=1
b=2
print(id(a))
print(id(b))

a=[1,2,2]
print(sum(a))
print(sum(a,30))

print(round(100.500))
print(round(100.501))
print(round(100.501,2))


