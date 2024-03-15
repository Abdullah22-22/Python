class employee:
    def __init__(self, name, age, department, is_manger,rating,salary ) :
        self.name=name
        self.age=age
        self.department=department
        self.is_manger=is_manger
        self.rating=rating
        self.salary=salary
    def is_excellent(self):
        if self.rating >=4.5:
            return True
        else:
             return False
    def bonus(self):
        if self.age>=50:
            self.salary += 500
            print("salary increased to " + str(self.salary))
        else:
            print("ok")
class dector:
    def studied_yers(self):
        print("7 yers")
    def work_where(self):
        print("in hospital")
    def paid_by_who(self):
        print("by government")

# def sss_sss(*args):
#     result=1
#     for x in args:
#         result *= x
#     return result
# print(sss_sss(1,2,3,4,5))
# def sss_sss(**kwargs):
#     result=""
#     for x in kwargs.values():
#         result += x
#     return result
# print(sss_sss(a="abdullah", c="\n " ,b="26"))
# def sss_sss(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}:")
# sss_sss(name="abdullah",age=26,jop="student")
# sss_sss(name="ali",age=28,jop="tecchers",live="helsnki")
# def sss_sss(x,y,*args,option=True,**kwargs):
#     print(x,y)
#     print(args)
#     print(option)
#     print(kwargs)
# sss_sss(1,2, "3", "4", a="abdullah", b=26,option=False)
n=int(input("enter"))
x=0
print(n*("+___ "))
while x < n:
    print("|", x+1,"/",  end= '')
    x= x+1
print(n* (""))
print(n*("|___\\"))
print(n*("|    "))


