#Je bent bezig met een kassasysteem voor de horeca. De afnemer heeft een speciale vraag: om te voorkomen dat de klanten continu met stapels muntgeld in hun broekzakken moeten rondlopen wil hij zo min mogelijk coins teruggeven. Concreet wil hij na 1 aankoop nooit meer dan 5 muntstukken teruggeven.
#Stel nu dat er in je kasla de volgende muntstukken liggen:
#4 * E 2,-
#2 * E 1,-
#8 * E 0,50
#1 * E 0,20
#4 * E 0,10
#3 * E 0,05
#Hoeveel unieke bedragen kun je teruggeven met minimaal 1 en maximaal 5 coins?
#Antwoord met een positieve integer (bijv. 15000).
import itertools

# we berekenen een cartesiaans product en doen de check op de aantallen pas later...
coins=[2,1,0.5,0.2,0.1,0.05]

def setIsValid(s):
    if (s.count(2.0) > 4 or  s.count(1.0) > 2 or s.count(0.5) > 5 or s.count(0.2) >1 or s.count(0.1) > 4 or s.count(0.05)>3):
        return False
    else:
        return True
    
    
results=[]
for i in range(1,6):
    # de results als een list geeft 137560 opties
    # als set daarentegen 1554...
    results+= set(itertools.product(coins,repeat=i))    
# filter alle invalide combinaties uit (dwz: teveel munten)
results=list(filter(setIsValid,results))
# en tel alle bedragen bij elkaar op en stop ze in een set zodat ze uniek zijn....
results=list(set(map(lambda i: round(sum(i),2),results)))
print(len(results))