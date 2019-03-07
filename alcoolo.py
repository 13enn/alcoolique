# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 19:36:11 2019

@author: bleblanc
"""

V = float(raw_input("Combien de litres d'alcool? "))
type(V)

pc = float(raw_input("C'est quoi le pourcentage? "))
type(pc)

# find out combien d'alcool
alc=V*pc/100
# roughly 5 poucent de ton alcool est du méthanol, en ML (donc x1000)
meth = alc*0.05 * 1000


print("\n Tu as about "+str(meth)+" mL de méthanol, plaise")

