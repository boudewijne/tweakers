#In het oude Rome stond een sterk staaltje architectuur genaamd het 'Ominesium'. Op de gevel van het gebouw was met mozaiek aangegeven hoe oud het gebouw was in jaren. Uiteraard gaven de oude Romeinen dit aan met Romeinse cijfers. Deze Romeinen waren erg bij de tijd en gebruikten de moderne notatie voor Romeinse cijfers: 49 = XLIX, 4 = IV.

#Het gebouw is net na een stevige aardbeving voltooid, en het eerste mozaiek werd na een jaar aangebracht. Onze jaartelling begint bij 0, dus het eerste mozaiek werd geplaatst in het jaar 1.

#Het aantal mozaieksteentjes benodigd voor een symbool is 250. Het jaartal IV kostte dus 500 steentjes om op de muur aan te brengen.
#Om kleurverschil tegen te gaan werd bij elke plaatsing van een nieuw jaartal de complete mozaiek opnieuw geplaatst.
#Het was een regio met veel seismische activiteit; om de 43 jaar werd de regio getroffen door een zware aardbeving waarbij 15% van de voorraad steentjes verloren ging, per aardbeving afgerond naar boven op gehele steentjes. De eerste beving sinds de voltooiing van het gebouw vond plaats na 43 jaar.
#Aardbevingen vonden door een enorm toeval telkens plaats voordat het nieuwe mozaiek werd aangebracht.
#Na de voltooiing van het 'Ominesium' (en dus ook na de aardbeving in het jaar 0) was er nog een voorraad van 12.500.000 mozaieksteentjes beschikbaar voor de jaarlijkse renovatie van het mozaiek.
#In welk jaar was de voorraad steentjes niet meer voldoende om het nieuwe jaartal op het gebouw te plaatsen?

import math

# bron: http://code.activestate.com/recipes/81611-roman-numerals/
numeral_map = zip(
    (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
    ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
)

def int_to_roman(i):
    result = []
    for integer, numeral in numeral_map:
        count = int(i / integer)
        result.append(numeral * count)
        i -= integer * count
    return ''.join(result)

def roman_to_int(n):
    n = unicode(n).upper()

    i = result = 0
    for integer, numeral in numeral_map:
        while n[i:i + len(numeral)] == numeral:
            result += integer
            i += len(numeral)
    return result




BEGINSTEENTJES=12500500         # aantal steentjes bij start
AARDBEVINGSJAAR=43              # aantal jaren tussen bevingen
AARDBEVINGSRESTANT=0.85         # percentage dat overblijft na een beving
SYMBOOLPRIJS=250                # prijs per letter


def berekenSteentjes(jaartal, steentjesvoorraad):
    if (jaartal %AARDBEVINGSJAAR == 0):
        steentjesvoorraad=math.ceil(steentjesvoorraad*AARDBEVINGSRESTANT)
     
    dit_jaar = int_to_roman(jaartal)
   
    steentjesprijs = len(dit_jaar)*SYMBOOLPRIJS
    print ("Jaar: " +str(jaartal) +"\tvooraad: " +str(steentjesvoorraad)+"\t" + str(int_to_roman(jaartal))+"\tprijs " + str(steentjesprijs))   
    return(steentjesvoorraad-steentjesprijs)
    


steentjes_voorraad=[BEGINSTEENTJES]
for i in range(1,1000):
    steentjes_voorraad+=[berekenSteentjes(i,steentjes_voorraad[i-1])]
    if (steentjes_voorraad[i] < 0 ):
        print ("Eerste jaar met te weinig steentjes: "+str(i) + "(" + int_to_roman(i)+")")
        break
    