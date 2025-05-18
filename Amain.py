def printNumber(n):
    steps=0
    print(f"the number is {n}")
    steps+=1
    print (f"the number of steps is {steps}")

printNumber(100)
printNumber(1000)

def OnTime(n):
    steps=0
    for i in range(1,n+1):
     steps+=1
    print (f"when n is {n}, the steps are {steps}")

OnTime(5)
OnTime(10)

def OnSquared(n):
    steps=0
    for i in range(0,n):
       for j in range(0,n):
          steps+=1
    print(f"when n is {n}, the steps are {steps}")

OnSquared(2)
OnSquared(14)