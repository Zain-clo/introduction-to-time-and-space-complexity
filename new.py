number = int(input("Enter the amt to check:  "))


if number > 1 :
     for i in range(2,number):
          if (number%i) == 0:
               print("This aint a prime number")
               break
        
     else:
        print("This is a prime number")




def sieve_of_erastothenes(n):
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False
    p = 2

    while p * p <= n:
        if primes[p]:
           for i in range(p*p, n+1, p ):
             primes[i] = False
        p += 1
    result = []
 
    for i in range(len(primes)):
        if primes[i]:
           result.append(i)
    return result

print(sieve_of_erastothenes(50))