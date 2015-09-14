# De zombie apocalypse heeft toegeslagen. Patient zero is besmet geraakt nadat hij was gebeten door een mier tijdens het nachtelijk wildplassen. Precies om 0:00 zelfs.
# De volgende waarden zijn van toepassing
# *Op het moment van de besmetting van patient zero zijn er 7.000.000.000 mensen niet besmet.
# *Elke zombie valt 2 mensen aan per uur tussen 8:00 en 22:00. In de nachtelijke uren is dit er 1 per uur.
# *Elk uur raakt per 5 aanvallen afgerond naar beneden gemiddeld 1 lichaam van een gezond persoon te zwaar beschadigd om opnieuw op te staan. Deze persoon kan dus geen anderen infecteren.
# *Vanaf 8:00 op de eerste dag heeft de mensheid door wat er aan de hand is en weet vanaf dan elk uur per drie aanvallen een aanval af te slaan en daarbij aan de zombie te ontsnappen.
# *Omdat we uitgaan van gemiddelden, beginnen we elk uur opnieuw met het tellen van beschadigde lichamen en afgeweerde zombies.
# 
#Na hoeveel uren is het menselijk ras uitgestorven?
#
#Antwoord met een positieve integer (bijv. 15000).
import math

mensen=7000000000
tijd=0
zombies=1


    
    
    
while mensen > 0:
    tijd+=1
    uur = tijd % 24 
    aanvallen_per_uur=1 
    # aanvallen...
    if uur >=8 and uur < 22 : 
        aanvallen_per_uur=2
    aanvallen_per_uur*=zombies
    
    # de te zwaar gewonde persoons
    #mensen-= math.ceil(aanvallen_per_uur*0.2)

    if tijd > 8:
        aanvallen_per_uur=math.ceil(aanvallen_per_uur*0.6666666666666666666666666666666666)
        
    mensen-=aanvallen_per_uur
    zombies+=aanvallen_per_uur    
        
    print ("Tijd: "+str(tijd)+ " \t Uur: "+str(uur)+"  \tAanvallen per uur: "+str(aanvallen_per_uur)+" \tMensen "+str(mensen)+"\t Zombies: "+str(zombies))

