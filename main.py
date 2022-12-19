#import sys for sys.exit() command 
import sys

#making a simpler exit command which displays score when called
def exit():
    #print score
    print("your score was " + str(score))
    #exit
    sys.exit()

#choosing to use lists lol
first = ['that', 'cool', 'really', 'is']
second = ['pretty', 'are', 'really', 'you']
third = ['it', 'a', 'is', 'beautiful', 'day']
score = 0


#introduction
print("hello, welcome to the list change program. You get to change one element of each list in order to make it a functioning sentence. ")
print("Lets play!!")


#first question
print(first)
answer = input("which word do you wish to change? Cool/That: ")
if answer.lower().strip() == "cool":
    print("well done")
    score = score + 1
else:
    print("fail")
    exit()
    
#second question
    print(second)
answer = input("Which word do you wish to change? You/Really: ")
if answer.lower().strip() == "you":
    print("well done, next question")
    score = score + 1
else:
    print("fail")
    exit()
    
#third question
print(third)
answer = input("Which word do you wish to change? beautfiul/A: ")
if answer.lower().strip() == "a":
    print("well done, you got 3 out of 3")
else:
    print("fail")
    exit()
    

