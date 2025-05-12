def func1(number):
    return number*(number+1)/2
def func2(number):
    sum=0
    for i in range(1,number+1):
        sum+=i
    return sum
print(func1(10))
print(func2(10))