number=input("Enter the amount to check:")
original_number = number
reversed_number = number[::-1]
if original_number ==reversed_number:
    print(number,"is a palindrome number")
elif reversed_number:
    print(number, "is both")
else:
     print(number,"is  not a palindrome number")
     






a = int(input("Enter the bigger number: "))

b = int(input("Enter the smaller number: "))

while b > 0:

 r = a % b

 a = b

 b = r

GCD = a

print("the GCD is", GCD)