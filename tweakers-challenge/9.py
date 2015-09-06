#Neem het getal 5128
#Hoeveel enen komen er voor in de binaire representatie van dit getal?
#Antwoord als positief integer, bijvoorbeeld: 15000

#1: reken het getal uit.
#2: maak dat binair
#3: maak er een string van
#4: filter alles wat niet "1" is uit (dat doet de filter met lambda functie)
#5: tel wat over blijft

print (len(filter(lambda x: x== "1", str(bin(5**128)))))