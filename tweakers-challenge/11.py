# experimentje in de shell: als we gaan filteren op duplicaten is dat aantal niet significant genoeg... maar wel aardig om even mee te pakken
# johns-MacBook-Pro:tweakers-challenge john$ tr ' ' '\n' < 11.txt  | sort -u | wc -l 
#   45595
#johns-MacBook-Pro:tweakers-challenge john$ tr ' ' '\n' < 11.txt  |  wc -l 
#   54998
# voordeel is ook nog dat we hier elk getal op 1 regel hebben, en het hoogste getal meteen duidelijk is (262141)
# maarja dit kan ook in python

import math

# het importeren van het bestand in een array...
lines=[]
with open('11.txt','r') as f:
    lines+= f.readlines()
    
input_getallen=[]
for i in lines:
    input_getallen+=map(lambda x: int(x), i.rstrip().split(" "))

# nu hebben we een list met de getallen uit de file.we sorteren die ook maar meteen.
input_getallen=sorted(input_getallen)

# we kunnen elk getal wel controleren op of het priem is, maar waarom niet alle priemgetallen tot het grootste getal uit de array nemen en die 2 sets over elkaar leggen?
#bron: http://stackoverflow.com/questions/21783160/sieve-of-atkin-implementation-in-python
def sieveOfAtkin(limit):
    P = [1,2,3]
    sieve=[False]*(limit+1)
    for x in range(1,int(math.sqrt(limit))+1):
        for y in range(1,int(math.sqrt(limit))+1):
            n = 4*x**2 + y**2
            if n<=limit and (n%12==1 or n%12==5) : sieve[n] = not sieve[n]
            n = 3*x**2+y**2
            if n<= limit and n%12==7 : sieve[n] = not sieve[n]
            n = 3*x**2 - y**2
            if x>y and n<=limit and n%12==11 : sieve[n] = not sieve[n]
    for x in range(5,int(math.sqrt(limit))):
        if sieve[x]:
            for y in range(x**2,limit+1,x**2):
                sieve[y] = False
    for p in range(5,limit):
        if sieve[p] : P.append(p)
    return P

# genereer alle priemgetallen tot het hoogste getal in. We maken er een set van omdat we zo een union operatie willen gebruiken 
priemgetallen=sorted(set(sieveOfAtkin(input_getallen[-1]+1)))

# deze filter en lambda voert in feite een intersectie in beide sets uit... items worden alleen bewaard indien ze in beide sets voorkomen
input_getallen=filter(lambda x: x in priemgetallen, input_getallen)
print (len(input_getallen))
