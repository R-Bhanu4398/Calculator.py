def add(a,b):
   return a+b
def sub(a,b):
   return a-b
def multi(a,b):
   return a*b
def div(a,b):
   if b==0:
      return "It is not Possible"
   else:
      return a/b
def modulus(a,b):
   if b==0:
      return "It is not possible"
   else:
      return a%b


while True:
   a=int(input("Enter the number :"))
   b=int(input("Enter the number :"))
   c=input("Operators (+ | - | * | / | % | all | exit) :")
   if c=="exit":
      break
   elif c=="+":
      print(add(a,b))
   elif c=="-":
      print(sub(a,b))
   elif c=="*":
      print(multi(a,b))
   elif c=="/":
      print(div(a,b))
   elif c=="%":
      print(modulus(a,b))
   elif c=="all":
      print(add(a,b))
      print(sub(a,b))
      print(multi(a,b))
      print(div(a,b))
      print(modulus(a,b))
   else:
      print("Invalid Operator")

