def firstsetbit(n):
    count  = 1
    while(n):
        if (n&1 ==1):
            break
         count+=1
        n= n>>1
    return count
print(firstsetbit)



def countsetbit(n):
    countzeros  = 0
    countones= 0
    while(n):
        if (n&1 ==1):
            countones+=1
        else:
            countzeros+=1
         n= n>>1
     return countzeros, countones

