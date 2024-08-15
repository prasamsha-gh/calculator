print("select an operation to perform:")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()

if operation == "1":
    num1 = input("enter the 1st number:")
    num2= input("enter the 2nd number:")
    print("The sum is : " + str(int(num1) + int(num2)))

elif operation == "2":
     num1 = input("enter the 1st number:")
     num2= input("enter the 2nd number:")
     print("The difference is : " + str(int(num1) - int(num2)))
 
elif operation == "3":
     num1 = input("enter the 1st number:")
     num2= input("enter the 2nd number:")
     print("The product is : " + str(int(num1) * int(num2)))
 
elif operation == "4":
     num1 = input("enter the 1st number:")
     num2= input("enter the 2nd number:")
     print("The result is : " + str(int(num1) / int(num2)))

else:
     print("Invalid Entry")