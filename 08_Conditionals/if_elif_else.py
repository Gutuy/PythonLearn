age=int(input("Enter your age: "))

if(age>18):
    print("you can drive")
elif(age==18):
    print("let us schedule a driving test for you")
elif(age==0):
    print("you are just born, you cannot drive")
else:
    print("sorry you cannot drive ")