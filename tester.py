# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
#print(sum(i for i in range(1,1000) if i%3 == 0 or i%5 == 0))
        

a, b = 1, 2
resultat = 0
while b <= 4000000:
    if b % 2 == 0:
        resultat += b
    a, b = b, a + b
print(resultat)
    

        
