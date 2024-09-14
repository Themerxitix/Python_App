
from api_aanroep import steden_per_land, financieel_data

def toon_top_steden():
    land = input("Voer het land in: ")
    steden = steden_per_land(land)

    if steden:
        print('-------------------------------------')
        print(f"Top vijf drukste steden in {land.capitalize()}:")
        print('-------------------------------------')

        for i in range(len(steden)):
            for j in range(i + 1, len(steden)):
                if steden[i]['population'] < steden[j]['population']:
                    steden[i], steden[j] = steden[j], steden[i]
        landcode = steden[0]['country_code']
        bbp_data = financieel_data(landcode)

        for i in range(min(5, len(steden))):
            stad = steden[i]
            print(f"{i + 1}. {stad['name']} (Inwoners: {stad['population']})")
            if bbp_data and 'value' in bbp_data and bbp_data['value'] is not None:
                print(f"   BBP per hoofd: ${bbp_data['value']:.2f}, (Jaar: {bbp_data['date']})")
                print('------------------------------')
            else:
                print("   BBP gegevens niet beschikbaar.")
                print('------------------------------')
    else:
        print(f"Geen steden gevonden in land: '{land}'")

    #     for stad in steden:
    #         print(f"- {stad['name']} (Inwoners: {stad['population']})")
    # else:
    #     print(f"Geen steden gevonden voor {land}")

# if __name__ == "__main__":
#     toon_top_steden()
