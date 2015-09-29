# Sommige positieve getallen n hebben de eigenschap dat de som [ n + reverse(n) ] volledig bestaat uit oneven nummers. Bijvoorbeeld, 36 + 63 = 99 en 409 + 904 = 1313. Deze getallen noemen we omkeerbaar; dus 36, 63, 409, en 904 zijn omkeerbaar. Voorlopende nullen in n or reverse(n) zijn niet toegestaan.
#
# Er zijn 120 omkeerbare getallen onder 1000.
#
# Hoeveel omkeerbare getallen zijn er onder 100 miljoen (108)?



def isReversible(n):    
    if (n < 0):
        return False
    
    # controleer op voor danwel naloop nullen
    if str(n)[0] == "0" or n%10==0:
        return False
    rev_n= int(str(n)[::-1])
    str_som=str(n+rev_n)
    if ("0" in str_som) or ("2" in str_som) or ("4" in str_som) or ("6" in str_som) or ("8" in str_som):
        return False
    return True
    
results=filter(isReversible, range( 1,100000000))
print(len(results))

