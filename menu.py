#Menu
def hoofdmenu():
    while True:
        print('Hoofdmenu \n-------------')
        print('1. Stadsinformatie')
        print('2. Steden vergelijken')
        print('3. Top 5 duurste staden per land')
        print('0. Stoppen\n')


        try:
            gebruikers_invoer = input('Uw keuze: ')
        except ValueError:
            gebruikers_invoer = -1

        if gebruikers_invoer == '1':
            print('Stadsinformatie\n')
        elif gebruikers_invoer == '2':
            print('Steden vergelijken\n')
        elif gebruikers_invoer == '3':
            print('Top 5\n')
        elif gebruikers_invoer == '0':
            print('Bedankt en tot ziens')
            break
        else:
            print('Ongeldige keuze, probeer het opnieuw\n')

# hoofdmenu() anders wordt dit automatisch uitgevoerd
