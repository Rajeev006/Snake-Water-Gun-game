import random
''' 
1 for snake
-1 for water
0 for gun

'''
computer=random.choice([-1, 0, 1])
yourstr=input("Enter your choice : ")
youdict={"s":1 ,"w": -1, "g":0}
reversedict={1:"Snake",-1:"Water",0:"Gun"}

you=youdict[yourstr]

print(f"Computer choose: {reversedict[computer]}\n You choose: {reversedict[you]}")

if(computer==you):
    print("Its's a Draw")

elif(computer ==-1 and you==1):
    print("You Win!")

elif(computer ==-1 and you==0):
    print("You Lose!")

elif(computer ==1 and you==-1):
    print("You Lose!")

elif(computer ==-1 and you==0):
    print("You Win!")

elif(computer ==0 and you==-1):
    print("You Win!")

elif(computer ==0 and you==1):
    print("You Lose!")

else:
    print("Something wrong!!")