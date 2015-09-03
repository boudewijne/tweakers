#  Een object zweeft met een vaste snelheid van 20 punten p/s door de ruimte. 
# Op het moment van schrijven bevindt het object zich op positie x: 30, y: 50 en z: 90. Het object beweegt naar x: 46, y: 48 en z: 9.
# Wat zijn de coordinaten van het object na 25 minuten. Afgerond op 2 decimalen
# Voorbeeldnotatie antwoord: x:1.200,12 y:24.150,00 z:160,98

from math import *

# horizontale vlak...
x_start=30
y_start=50
z_start=90

x_target = pow(4,6)
y_target = pow(4,8)
z_target = 9

delta_x = x_target-x_start
delta_y = y_target-y_start
delta_z = z_target-z_start

points_total=sqrt(pow(delta_x,2)+pow(delta_y,2)+pow(delta_z,2))

points_traveled=20*(60*25) 


print ("Points total: "+str(points_total))
print ("Points traveled in 25m: "+str(points_traveled))

factor=points_traveled/points_total
print ("Factor: "+str(factor))


x_end=x_start+(delta_x*factor)
y_end=y_start+(delta_y*factor)
z_end=z_start+(delta_z*factor)

print("X eindpunt "+str(round(x_end,2)))
print("Y eindpunt "+str(round(y_end,2)))
print("Z eindpunt "+str(round(z_end,2)))


#x:1.889,11 y:29.992,32 z:52,96