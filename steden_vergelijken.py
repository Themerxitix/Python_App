#importeer de api
from api_aanroep import stads_data, financieel_data

#functie aanmaken die de informatie geeft over de stad
def toon_stad_info(stad_naam, stad_data):
    print(f"\nInformaite over {stad_data['name']}:")
    print(f"Land: {stad_data['cou_name_en']}")
    print(f"Inwoners: {stad_data['population']:,}")

    eco_data = financieel_data(stad_data['country_code'])
    if eco_data:
        print(f"BBP per hoofd: ${eco_data['value']:,.2f}(Jaar: {eco_data['date']})")
    else:
        print("BBP gegevens zijn niet beschikbaar.")

#de bbp waarde van de staden vergelijken
def vergekijk_bbp(eerste_stad_data, tweede_stad_data):
    eerste_eco_data = financieel_data(eerste_stad_data['country_code'])
    tweede_eco_data = financieel_data(tweede_stad_data['country_code'])

    if eerste_eco_data and tweede_eco_data:
        if eerste_eco_data['value'] > tweede_eco_data['value']:
            bbp_verschil = eerste_eco_data['value'] - tweede_eco_data['value']
            print(f"\nBBP vergelijking:")
            print(f"Verschil in BBP per hoofd: ${bbp_verschil:,.2f}")
            print(f"{eerste_stad_data['name']} heeft een hoger BBP per hoofd.")
        elif eerste_eco_data['value'] < tweede_eco_data['value']:
            bbp_verschil = tweede_eco_data['value'] - eerste_eco_data['value']
            print(f"\nBBP vergelijking:")
            print(f"Verschil in BBP per hoofd: ${bbp_verschil:,.2f}")
            print(f"{tweede_stad_data['name']} heeft een hoger BBP per hoofd.")
        else:
            print("Beide steden hebben hetzelfde BBP per hoofd.")
    else:
        print("\nBBP vergelijking is niet mogelijk.")

def vergelijken():
    # input van gebruiker
    eerste_stad = input("Voer de naam van de eerste stad in: ")
    tweede_stad = input("Voer de naam van de tweede stad in: ")

    #de stad informatie ophalen
    eerste_steden = stads_data(eerste_stad)
    tweede_steden = stads_data(tweede_stad)

    if not eerste_steden:
        print(f"Geen gegevens gevonden voor {eerste_stad}")
    if not tweede_steden:
        print(f"Geen gegevens gevonden voor {tweede_stad}")

    if eerste_steden and tweede_steden:
        eerste_stad_data = eerste_steden[0]
        tweede_stad_data = tweede_steden[0]

        toon_stad_info(eerste_stad, eerste_stad_data)
        toon_stad_info(tweede_stad, tweede_stad_data)
        vergekijk_bbp(eerste_stad_data, tweede_stad_data)
    else:
        print("Vergelijking niet mogelijk.")

if __name__ == "__main__":
    vergelijken()