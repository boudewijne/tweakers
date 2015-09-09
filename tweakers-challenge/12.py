#Een Warrior, Mage en Rogue trekken een kerker in om deze vrij te waren van monsters. De aanval op ieder nieuw monster begint hetzelfde: de Warrior leidt de aanval en brengt de eerste slag toe. De Mage start net voor de eerste aanval van de Warrior met de casting tijd en als laatste begint de Roque met aanvallen. Omdat de heren avonturiers zo op elkaar afgestemd zijn gebeurt dit alles in een fractie van een seconde.

#Warrior: Elke 4s 35 punten schade
#Mage: 2s casting tijd en daarna elke 8s 80 punten schade
#Rogue: Elke 4s 30 punten schade vanuit het primaire wapen en elke 3s 20 punten schade vanuit het secundaire wapen
#Wanneer twee of meer avonturiers in dezelfde seconde aanvallen wordt de schade die door de Warrior gedaan wordt altijd eerst berekend, gevolgd door de schade van de Mage terwijl de Rogue binnen die seconde pas als laatste zijn schade toedient.
#In de kerker komen de heren avonturiers de volgende monsters tegen

#Monster 1 met 300 hitpoints
#Monster 2 met 600 hitpoints
#Monster 3 met 850 hitpoints
#Monster 4 met 900 hitpoints
#Monster 5 met 1100 hitpoints
#Bossman met 3500 hitpoints

#Wat is de totale hoeveelheid overkill die de Warrior toebrengt aan de monsters waarbij hij de doodslag toedient? De overkill is de hoeveelheid 'overbodige' schade omdat het monster voor het toedienen daarvan al verslagen is.
#Antwoord met een positieve integer (bijv. 15000).


# retourneert overgebleven hitpoints. Van belang is je te realiseren dat OF de warrior iemand killt en dan is de overkill relevant, of iemand anders doet het en dan telt de overkill niet
def voerStrijd(vijand_hp):
    seconden=0
    while (vijand_hp > 0 ):
        #print ("Staat na seconden: "+str(seconden)+" @HP :"+str(vijand_hp))
        schade_deze_seconde=0
        # de warrior
        if (seconden %4 == 0):
            schade_deze_seconde += 35
            if vijand_hp-schade_deze_seconde<=0:
                return (abs(vijand_hp-schade_deze_seconde))
        # de mage
        if (seconden %8 == 2 ):
            schade_deze_seconde += 80
        # de rogue , primair
        if (seconden %4 == 0 ):
            schade_deze_seconde +=30
        # de rogue, secundair
        if ( seconden %3 ==0 ):
            schade_deze_seconde+=20
    
        seconden +=1
        vijand_hp-=schade_deze_seconde
        
    # de warrior heeft de vijand niet gedood dus score is niet relevant
    return 0    
        
warrior_overkill = voerStrijd(300)
warrior_overkill += voerStrijd(600)
warrior_overkill += voerStrijd(850)
warrior_overkill += voerStrijd(900)
warrior_overkill += voerStrijd(1100)
warrior_overkill += voerStrijd(3500)

print ("Warrior overkill: "+str(warrior_overkill))