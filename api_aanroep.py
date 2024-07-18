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
            if not stad_resultaat:
                print(f"Het opgegeven stad is niet gevonden: '{stads_naam}'")
            return stad_resultaat

    except requests.RequestException as e:
        print(f'Er is een fout opgetreden bij het ophalen van de : {e}')

# stad_resultaat = stads_data('')
#
# print(stad_resultaat)

def financieel_data(landcode):
    # de url van WorldBank
    url = f'http://api.worldbank.org/v2/country/{landcode}/indicator/NY.GDP.PCAP.CD'

    params = {
        "format": "json",  # uit de API website, onder kopje respons format, wordt aangegeven dat alle requests in XML worden teruggestuurd, daarom dit format wijziging.
        "per_page": "1",  # Vraagt slechts om een resultaat
        "date": "2020:2024"
    }

    response = requests.get(url, params=params)

    try:
        if response.status_code == 200:
            response = response.json()

        if len(response) > 1 and response[1]:
            # print(response[1][0])
            financiele_resultaat = response[1][0]
            return financiele_resultaat
        else:
            print('Geen economische gegevens gevonden!')

    except requests.RequestException as e:
        print(f'Fout bij het ophalen van stadsgegeven: {e}')

# financieel_data('NL')
# financiele_resultaat = financieel_data('NL')
# print(financiele_resultaat)