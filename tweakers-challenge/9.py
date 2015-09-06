#Neem het getal 5128
#Hoeveel enen komen er voor in de binaire representatie van dit getal?
#Antwoord als positief integer, bijvoorbeeld: 15000

print (len(filter(lambda x: x== "1", str(bin(5**128)))))