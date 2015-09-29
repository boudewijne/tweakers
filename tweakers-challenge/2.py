#De Fibonaccireeks is een rij van getallen die ten grondslag ligt aan vele processen in de natuur, van de structuur van zonnebloemen tot de explosieve groei van een konijnenpopulatie.

#De reeks begint met de getallen 0 en 1, waarna ieder volgend getal de som is van zijn 2 voorgangers. Het begin is dus: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, etc.

#Stel dat je van alle Fibonaccigetallen tot 1.000.000.000.000.000.000 (1018) de afzonderlijke cijfers optelt, hoe vaak komt daar een getal uit dat zelf het kwadraat is van een geheel getal?
import math

MAX= 1000000000000000000

def expandFibArray(a, max):
    if len(a)<2:
        a=[0,1]
    new_elem = a[-1]+a[-2]
    if new_elem < max:
        return expandFibArray(a+[new_elem],max)
    else:
        return a
    
def telcijfersop(s):
    s=str(s)
    s=map(int,s)
    return (sum(s))
    
def isInt(n):
    if n == int(n):
        return True
    return False
    
fibonacci_list= (expandFibArray([],MAX))
added_numbers = map(telcijfersop,fibonacci_list)
roots = map(math.sqrt,added_numbers)
int_roots = filter(isInt,roots)

#print (fibonacci_list)
#print (added_numbers)
#print (roots)
#print (int_roots)
print (len(set(int_roots))+1)