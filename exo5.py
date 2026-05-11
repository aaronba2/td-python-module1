# EXERCICE 5 - Fonction de calcul de spread

def calcul_spread(bid, ask):
    return ask - bid


bid = 100.25
ask = 100.40

spread = calcul_spread(bid, ask)

print(spread)