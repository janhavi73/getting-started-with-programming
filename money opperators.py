amount=int(input("please input the amount of money"))
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10

print("number of 100 rupe notes-:",note1)
print("number of 50 rupe notes-:",note2)
print("number of 10 rupe notes-:",note3)