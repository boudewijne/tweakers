


# Geen voorloopnullen
# positief
# n + rev_n -> oneven


def isReversible(n):
    rev_n= int(str(n)[::-1])
    
    if (n < 0):
        return False
    if str(n)[0] == "0" or str(n)[::-1][0]=="0":
        return False
    str_som=str(n+rev_n)
    if ("0" in str_som) or ("2" in str_som) or ("4" in str_som) or ("6" in str_som) or ("8" in str_som):
        return False
    return True    
    

ctr=0
for i in (range( 1,100000000)):
    if i%1000000 ==0:
        print ("Counter "+str(i))
    if isReversible(i):
        ctr+=1
        
print (ctr)

#print (isReversible(10))