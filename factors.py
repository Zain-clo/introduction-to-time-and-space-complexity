def factors(number):
    for i in range (1,number+1):
        if(number%i==0):
            print(i)
factors(24)



number=int(input("Enter the ammount to check"))
lenght=len(str(number))



temp=number
sum=0
while temp>0:
    digit = temp%10
    sum+=digit**lenght
    temp//=10
if number ==sum:
    print("armstroong number")
else:
    print("NOT an amstrong number")