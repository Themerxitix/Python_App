# in dit bestand ga ik de API's aanroepen

import requests

def stads_data(stads_naam):
    # de url van OpenDataSoft
    url = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/geonames-all-cities-with-a-population-1000/records"

    params = {
        "field": "name",
        "where": f"name like \"{stads_naam}\"",
        "limit": 3
    }

    # response = requests.get(url, params=params)
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            response = response.json()
            #dataset results word teruggestuurd
            # print(response['results'])
            stad_resultaat = response['results']
            # print(resultaat)
            #print(response)
            # if not stad_resultaat:
            #     print(f"Het opgegeven stad is niet gevonden: '{stads_naam}'")
            return stad_resultaat

    except requests.RequestException as e:
        print(f'Fout bij het ophalen van stadsgegeven: {e}')

# stad_resultaat = stads_data('')
#
# print(stad_resultaat)

def financieel_data(landcode):
    # de url van WorldBank
    url = f'http://api.worldbank.org/v2/country/{landcode}/indicator/NY.GDP.PCAP.CD'

    params = {
        "format": "json",  # uit de API website, onder kopje respons format, daarom dit format wijziging.
        "per_page": "1",  # Vraagt slechts om een resultaat
        "date": "2020:2024",
        # "country": "value"
    }

    response = requests.get(url, params=params)

    try:
        if response.status_code == 200:
            response = response.json()

        if isinstance(response, list)and len(response) > 1 and response[1]:
            # print(response[1][0])
            financiele_resultaat = response[1][0]
            #land_resultaat = response[1][0]['country']['value']
            return financiele_resultaat

    except requests.RequestException as e:
        print(f'Fout bij het ophalen van stadsgegeven: {e}')

# financieel_data('NL')
# financiele_resultaat = financieel_data('NL')
# print(financiele_resultaat)

def steden_per_land(land_naam):

    url = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/geonames-all-cities-with-a-population-1000/records"
    params = {
        "where": f"cou_name_en like '{land_naam}'",
        "limit": 100
    }
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            response = response.json()
            sted_resultaat = response['results']
            return sted_resultaat
    except requests.RequestException as e:
        print(f'Fout bij het ophalen van stadsgegeven: {e}')
    return None

# if __name__ == "__main__":
#     land = input("Voer een landnaam in: ")
#     steden = steden_per_land(land)
#     if steden:
#         print(f"Gevonden steden in {land}:")
#         for stad in steden:
#             print(f"- {stad['name']} (Inwoners: {stad['population']})")
#     else:
#         print(f"Geen steden gevonden voor {land}")