naam_lijst = []
leeftijd_lijst= []

def mijn_functie(x):
        naam = input("Typ een naam in: ")
        naam_lijst.append(naam)
        leeftijd = int(input("Typ een leeftijd in: "))
        leeftijd_lijst.append(leeftijd)
        verder = input("Toets enter om door te gaan of 'stop' om te printen: ")
        if verder != 'stop':
            print(x)

# while True:
    
        
#     print(mijn_functie())