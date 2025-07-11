a = 0 
b = 1
c = 0

c = a+b
a = b 
b=c 
c = c + 1
print(c)  


while c < 20:
    c = a+b
    a = b 
    b = c
    c = c + 1
    print(c)
