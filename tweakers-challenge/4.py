import math


def generateFiboArray(elements):
    a =[0,1]
    for i in range(2,elements):
        a+= [a[i-1]+a[i-2]]
    return a
    
diameter = sum(generateFiboArray(1000))

print (diameter)

omtrek = math.pi*diameter
print (omtrek)
# pas op, goed afronden!