
from stads_informatie import toon_stads_info
from steden_vergelijken import vergelijken
from top_steden import toon_top_steden
def hoofdmenu():

    while True:
        print('Hoofdmenu \n-------------')
        print('1. Stadsinformatie')
        print('2. Steden vergelijken')
        print('3. Top drukste steden per land')
        print('0. Stoppen\n')


        try:
            gebruikers_invoer = input('Uw keuze: ')
        except ValueError:
            gebruikers_invoer = -1

        if gebruikers_invoer == '1':
            print('Stadsinformatie\n')
            toon_stads_info()
            print('\n-------------')
        elif gebruikers_invoer == '2':
            print('Steden vergelijken\n')
            vergelijken()
            print('\n-------------')
        elif gebruikers_invoer == '3':
            print('Top drukste steden per land\n')
            toon_top_steden()
            print('\n-------------')
        elif gebruikers_invoer == '0':
            print('Bedankt en tot ziens')
            break
        else:
            print('Ongeldige keuze, probeer het opnieuw\n')

# hoofdmenu()
