import random
import math

#Initialization
total = 1000 #number of dart
hit = 0 #number of dart fall inside the circle's part
ndart = 0 #number of threw dart 
PI = 3.14 #pi

#Throw Dart
while (ndart <= total):
    Xrand = random.randint(0,1)
    Yrand = random.randint(0,1)
    
    #check condition
    if((Xrand**2) + (Yrand**2) <= 1):
        hit+=1
        
    ndart+=1

resultPI = (hit*4)/total
errorPI = abs(round(((PI - resultPI)/PI)*100,3))
#abs() berguna untuk merubah angka menjadi positif
#round() berguna untuk membulatkan angka 

print('Total Dart =',total)
print('Total Hit =',hit)
print('Hasil Pi =',resultPI)
print('Error Pi =',errorPI, '%')