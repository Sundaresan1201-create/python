def big(a,b,c):
    if a>b and a>c :
        return a is biggest
    elif b>a and b>c :
        return b is biggest
    else:
        return c is biggest

a = int(input("enter a number:"))
b = int(input("enter a number:"))
c = int(input("enter a number:"))
big(a,b,c)
