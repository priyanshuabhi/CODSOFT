# User input opration

num1 = int(input("enter the value of 1 :"))
num2 = int(input("enter the value of 2 :"))
opration = input("enter the opration :")

# calculator opretion

if opration == "+" :
    print(num1+num2)
 
elif opration == "-" :
    print(num1-num2)

elif opration == "*" :
    print(num1*num2)

elif opration == "/" :
    print(num1/num2)

else:
    print("invelid opration....")