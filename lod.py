def recurse(n):
    if n ==0:
     return
    recurse(n//2)
    print(n)
recurse(32)