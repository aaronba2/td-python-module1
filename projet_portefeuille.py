# PROJET - Contrôle simple d’un portefeuille

positions = [12000, -5000, 8000, -2500, 15000]

# Calcul total portefeuille
total = sum(positions)

# Comptage positions négatives
negatives = 0

for position in positions:
    if position < 0:
        negatives += 1

# Affichage
print("Total portefeuille :", total)
print("Positions négatives :", negatives)

# Vérification profit/perte
if total > 0:
    print("Portefeuille profitable")
else:
    print("Portefeuille en perte")

# BONUS 1
print("Position la plus élevée :", max(positions))

# BONUS 2
moyenne = total / len(positions)
print("Moyenne des positions :", moyenne)

# BONUS 3
def verifier_risque(valeur):
    if valeur > 10000:
        print("Risque élevé")
    else:
        print("Risque acceptable")


verifier_risque(15000)