print("please enter the scores you gotin these 4 subjects:")
maths=int(input("please enter your maths score"))
english=int(input("please enter your english score"))
science=int(input("please enter your science score"))
art=int(input("please enter your art score"))

sum=maths+english+science+art
print("the sum of your scores are:",sum)

perc=(sum/400)*100
print("the percentage of your score is:",perc)
