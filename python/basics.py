#Calculator 
x=int(input("Please enter first Number : "))
while (x<0):
  x=int(input("Please enter first Number : "))    

y=int(input("Please enter second Number : "))
while (y<0):
      y=int(input("Please enter second Number : ")) 

print("Adiition of two numbers: ",x+y)
print("Subtaction of two numbers: ",x-y)
print("Multiplication of two numbers: ",x*y)
if(x<=0):
    m=int(input("Enter the first digit: "))
    while(m<=0):
        m=int(input("Enter the first digit: "))
else:
    m=x;    
if(x<=0):
    n=int(input("Enter the first digit: "))
    while(m<=0):
        m=int(input("Enter the first digit: "))
else:
    n=x; 
print("Floor Division of two numbers: ",m//n)
print("Moudular Division of two numbers: ", m%n ) 