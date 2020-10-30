print("Calculator");
print
print("Scripted by Andros");

a=int(input("Enter 1st number:"))
b=int(input("Enter second number"))

print("Operations are +,-,*,/");

c=input("Enter any operation");

if c=="+":
    print(a,"+",b,"=",a+b)
    print("Thanks for using this Calculator..")
    
elif c=="-":
    print(a,"-",b,"=",a-b)
    print("Thanks for using this Calculator..")

elif c=="*":
    print(a,"*",b,"=",a*b)
    print("Thanks for using this Calculator..")

elif c=="/":
    print(a,"/",b,"=",a/b)
    print("Thanks for using this Calculator..")

else:
    print("Wrong input...")
    print("Please try again.")
