# Dictionnaire des vainqueurs et finalistes de la Ligue des champions
vainqueurs = {
    "Real Madrid": [1956, 1957, 1958, 1959, 1960, 1966, 1998, 2000, 2002, 2014, 2016, 2017, 2018, 2022, 2024],
    "AC Milan": [1963, 1969, 1989, 1990, 1994, 2003, 2007],
    "Bayern Munich": [1974, 1975, 1976, 2001, 2013, 2020],
    "Liverpool": [1977, 1978, 1981, 1984, 2005, 2019],
    "FC Barcelone": [1992, 2006, 2009, 2011, 2015],
    "Ajax": [1971, 1972, 1973, 1995],
    "Inter Milan": [1964, 1965, 2010],
    "Manchester United": [1968, 1999, 2008],
    "Juventus": [1985, 1996],
    "Benfica": [1961, 1962],
    "Chelsea": [2012, 2021],
    "Nottingham Forest": [1979, 1980],
    "Porto": [1987, 2004],
    "Borussia Dortmund": [1997],
    "Celtic": [1967],
    "Hambourg": [1983],
    "Steaua Bucarest": [1986],
    "Marseille": [1993],
    "Manchester City": [2023],
    "Feyenoord": [1970],
    "Aston Villa": [1982],
    "PSV Eindhoven": [1988],
    "Étoile Rouge De Belgrade": [1991]
}

finalistes = {
    "Real Madrid": [1962, 1964, 1981],
    "AC Milan": [1958, 1993, 1995, 2005],
    "Bayern Munich": [1982, 1987, 1999, 2010, 2012],
    "Liverpool": [1985, 2007, 2018, 2022],
    "FC Barcelone": [1961, 1986, 1994],
    "Ajax": [1969, 1996],
    "Inter Milan": [1967, 1972, 2023],
    "Manchester United": [2009, 2011],
    "Juventus": [1973, 1983, 1997, 1998, 2003, 2015, 2017],
    "Benfica": [1963, 1965, 1968, 1988, 1990],
    "Chelsea": [2008],
    "Nottingham Forest": [],
    "Porto": [],
    "Borussia Dortmund": [2013, 2024],
    "Celtic": [1970],
    "Hambourg": [1980],
    "Steaua Bucarest": [1989],
    "Marseille": [1991],
    "Manchester City": [2021],
    "Feyenoord": [],
    "Aston Villa": [],
    "PSV Eindhoven": [],
    "Étoile Rouge De Belgrade": []
}

# Fonction pour afficher les clubs vainqueurs et finalistes
def show_vainqueurs_finalistes():
    while True:
        choice = input("Citez un club vainqueur de la Ligue des champions (ou tapez 'exit' pour quitter) : ").title()
        if choice == 'Exit':
            print("Fin du programme.")
            break

        if choice in vainqueurs:
            print(f"{choice} a gagné la Ligue des champions en {vainqueurs[choice]}. Finalistes : {finalistes[choice]}")
        else:
            print("Erreur 404 : Club non trouvé.")

# Lancer le programme
show_vainqueurs_finalistes()
