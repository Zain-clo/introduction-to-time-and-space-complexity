a=int(input("eneter the firdst number"))
b=int(input("eneter the second number"))


if (a^b ==0):
    print("numnbers are equal")
else:
    print("numbers are not equal")



arr=[5,5,6,6,6,2,2]
result=0
for num in arr:
    result = result^ num

print("the number  that appers an odd number of times is",result)