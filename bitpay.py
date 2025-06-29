def swap(a,b):
    a=a^b
    b=a^b
    a=a^b
    print ("after swapping: a and b are", a,b)
swap(a=12,b=7)