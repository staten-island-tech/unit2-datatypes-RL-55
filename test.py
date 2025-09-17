def tipcalc():
    bill=input("Bill amount")
    bill=float(bill)
    tip=0.15*bill
    int(tip)
    total=bill+tip
    print(total)

def wordcount():
    sentence=input("Write a sentence.")
    y=sentence.split()
    x=0
    for i in y:
        x=x+1
    print(x)

def even():
    num=input("Number")
    str(num)
    if (num %2) == 1:
        print("Odd")
    else:
        print("Even")
even()
#name=input("What's your name?")
#print(name)
#def add(x,y):
#    return x*y
#z=add(input("Number One "),input("Number Two "))
#print(z)
#five=int('5')
#print(five+5)
#name="Mason"
#print(f"His name is {name}")
#bill=3.14159
#students=["Cadee","Mason","Andy"]
#students.append("Alina")
#print(students[2])
#for student in students:
#    print(student)
#Boolean true or false
#x=True
#evaluations use double==
#if x==True:
#    print()
#else:
#    print()
#y=False
#if y==True:
#elif y==None:
#else y==False:
#def and_movies(friend, money):
#if friend and money:
#print()