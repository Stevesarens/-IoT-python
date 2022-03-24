from itertools import product
from random import randint


n1 = randint(2,10)
n2 = randint(2,10)
print('Wat is het product van de volgende getallen?\n' ,n1,n2)
try:
    answer= answer = int(input('product:'))
except ValueError:
     print('Ongeldig getal')
product = n1 * n2
if answer == product:
    print('Gefeliciteerd!')
else:
    print('Het juiste anwoord was', product)