def leesDrieHoekIn(bestand):  
    result =[]
    with open(bestand,'r') as f:
        result+= f.readlines()
    result = map(lambda x: map(lambda y: int(y),x.rstrip().split(" ")), result)
    return result


def reduceerRijen(r1, r2):
    if not (len(r2)-len(r1) == 1 ):
        print ("Lengte mismatch, stop er nu mee!" )
        exit(1)
    result=[]
    for i in range(0,len(r1)):
        if (r2[i] > r2[i+1]):
            result.append(r1[i]+r2[i])
        else:
            result.append(r1[i]+r2[i+1])
        
    return (result)



triangle=(leesDrieHoekIn("10.triangle.txt"))

# TODO: De functie omschrijven zodat hij reduceert, dan hoef je ook niet meer te indiceren.
# we gaan nu een voor een de rijen reduceren, van onderaf (daarom de truc met de indices)
for i in range(0,199):
    triangle[198-i]=reduceerRijen(triangle[198-i], triangle[198-i+1])

print(triangle)
