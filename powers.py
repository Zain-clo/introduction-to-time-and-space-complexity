def is_power_of_2(n):
    return  n > 0 and (n&(n-1))==0
print(is_power_of_2(8))

def is_power_of_4(n):
   if   (n&(n-1))!=0:
       return False
   count= 0
   while n> 1:
        n>>=1
        count+=1
   return count % 2 == 0
print(is_power_of_4(64))