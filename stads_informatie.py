
from api_aanroep import stads_data, financieel_data

def toon_stads_info():
    #input van gebruiker
    voer_stad_in = input("Voer een stad in: ")

    #hier mee worden de gegevens opgehaald
    steden = stads_data(voer_stad_in)

    if steden:
        for stad in steden:
            print('---------------------------------------')
            print(f"Informatie over de stad: {stad['name']}")
            print(f"Land: {stad['cou_name_en']}")
            print(f"Aantal inwoners: {stad['population']}")

            try:
                #  economische gegevens worden opgehaald
                print(f"Ophalen van economische data voor landcode: {stad['country_code']}")
                economische_data = financieel_data(stad['country_code'])
                print(f"Ontvangen economische data: {economische_data}")
                if economische_data and 'value' in economische_data and economische_data['value'] is not None:
                    # Toon bruto binnenlands product (BBP) daarnaast ook uit welke jaar deze gegevens zijn
                    print(f"BBP per hoofd van de bevolking: ${economische_data['value']:,.2f}, (Jaar: {economische_data['date']})")
                else:
                    print("BBP is niet beschikbaar.")
            except KeyError:
                print("Er is een fout opgetreden bij het ophalen van BBP.")
    else:
        print(f"Het opgegeven stad '{voer_stad_in}' is niet gevonden.")


if __name__ == "__main__":
    toon_stads_info()