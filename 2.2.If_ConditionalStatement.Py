#if-elif-else statement

#1. WAP for Driver License Elligibilty
age = int(input("Enter age:"))
if(age>=18):
    print("Can apply for Driver License")
elif(age<0):
    print("Enter valid age")
else:
    print("You are not elligle yet")

#2. WAP to check if a number entered by user is odd or even
    
num = int(input("Enter a number:"))
if(num%2 ==0):
    print("Ur numer is Even")
else:
    print("ur Number is Odd")


#3. WAP to check if number is multiple of 7 or not 
    
num2 = int(input("Enter number to check multiple of 7 or not:"))
if(num2%7 == 0):
    print("Number is multiple of 7")
else:
    print("Number is not multiple of 7")


#4. WAP to find the greatest of 3 number entered by user
    
if((age>=num) and (age>=num2)):
    print("Age num is greater",age)
elif((num>=num2)):
    print("Num is gteater",num)
else:
    print("Num2 is greater",num2)