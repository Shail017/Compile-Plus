print ('Hello World \n')

def hello():
    a=input("enter string to print")
    print(a)

ask=input("do you want to print statemnt?(Y or N?)")
if ask=="Y"or ask=="y" :
    hello()
    ask2=input("do you want to print more?(Y or N?)")
    if ask2=="Y"or ask2=="y":
        hello()
    else:
        print("thankyou")
    
    ask3=input("do you want to print more?(Y or N?)")
    if ask3=="Y"or ask3=="y":
        hello()
    else:
        print("thankyou!")
else:
    print ("thankyou!")
