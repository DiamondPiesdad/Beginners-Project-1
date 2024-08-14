answer="code"
position=0
lengthcount=0
roundcount=0
length=len(answer)
numberofround=10
numberoftrue=0
winornot=False
output=[]
haveornot=False
passornot=False
store=set()
originalstore=set()
while not lengthcount==length:
    output.append("_")
    lengthcount+=1
while passornot==False:
    letterinput=input("guess a letter")
    store.add(letterinput)
    if originalstore==store:
        print("you have already guessed that")
    else:
        originalstore.add(letterinput)
        for answerletter in answer:
            if letterinput==answerletter:
                output[position]=letterinput
                haveornot=True
                numberoftrue+=1
            position+=1
        if haveornot==False:
            print("Nope")
        else:
            print(output)
        position=0
        roundcount+=1
        haveornot=False
        if numberoftrue==length:
            passornot=True
            winornot=True
        if roundcount==numberofround:
            passornot=True
if winornot==True:
    print("you win")
    print("the word is",answer)
else:
    print("he died rip")
    print("the word is",answer)