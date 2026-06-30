reversed=0;
number=int(input("Enter a number: "))
while number>0:
    digit=number%10
    reversed=reversed*10+digit
    number=number//10
print("The reversed number is:",reversed)