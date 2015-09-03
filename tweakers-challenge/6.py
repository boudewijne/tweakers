#Pascals driehoek is een bekende piramide waarbij het bovenste getal 1 is en de opvolgende rijen de som zijn van de 2 bovenliggende aangrenzende getallen. Zie hieronder een voorbeeld :
#
#      1
#     1 1
#    1 2 1
#   1 3 3 1
#  1 4 6 4 1
# 1 5 10 10 5 1

# Bereken de som van de onderste rij van een Pascal-driehoek met duizend rijen. De top van de driehoek telt niet mee als rij.
# Gebruik in je antwoord de wetenschappelijke notatie, rond af op 4 cijfers achter de komma, bijvoorbeeld: 1.0903E+23




# triangle is a [[]]
def expandTriangle(triangle):
    addition=[]
    if triangle==[]:
        addition=[[1]]
    elif triangle==[[1]]:
        addition=[[1,1]]
    else:
        addition=constructNewRow(triangle[-1])
    return triangle+addition


def constructNewRow(old_row):
    new_length=len(old_row)+1
    new_row=[-1]*new_length
    new_row[0]=1
    new_row[-1]=1
    for i in range(1,new_length-1):
        new_row[i]=old_row[i-1]+old_row[i]
    return [new_row]



t=[]

for i in range(0,10001):
#for i in range(0,1001):

    t=expandTriangle(t)
    if(i%100==0):
        print (i)
    if(i>=9999):
        uitkomst=(sum(t[-1]))
	print(uitkomst)
        #print ("{:.4E}".format(uitkomst))
        # >>> "{:.2E}".format(Decimal('40800000000.00000000000000'))

    #print(t[i])
#print(t)
#print(sum(t[-1]))
