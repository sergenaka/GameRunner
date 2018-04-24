def line (n):
    if(n==0):
        return ""
    else:
        rest=line(n-1)
        return "*"+rest

def rectangle (r,c):
    if(r==0):
        return ""
    else:
        half = r//2

    if((r % 2)==0):
        add = ""
    else:
        add = line(r) + half
    
    half_rectangle = rectangle((r//2),c)
    return half_rectangle + add + half_rectangle

r = rectangle((int(input)),(int(input)))


