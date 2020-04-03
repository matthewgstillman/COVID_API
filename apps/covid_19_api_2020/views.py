from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    data_dict = {}
    url = "https://coronavirus-tracker-api.herokuapp.com/v2/locations"
    response = requests.get(url)
    data = response.json()
    # print(type(data))
    # print(data['latest'])
    for key, value in data.items():
        print(key)
        latest = data['locations']
        for i in range(0, len(latest)):
            country_id = latest[i]['id']
            # print("Country ID: " + str(country_id))
            country = latest[i]['country']
            # print("Country: " + str(country))
            country_code = latest[i]['country_code']
            # print("Country Code: " + str(country_code))
            population = latest[i]['country_population']
            # print("Population: " + str(population))
            province = latest[i]['province']
            # print("Province: " + str(province))
            last_updated = latest[i]['last_updated']
            # print("Last Updated: " + str(last_updated))
            coordinates = latest[i]['coordinates']
            # print("Coordinates: " + str(coordinates))
            latitude = coordinates['latitude']
            # print("Latitude: " + str(latitude))
            longitude = coordinates['longitude']
            # print("Longitude: " + str(longitude)) 
            latest_info = latest[i]['latest']
            # print("Latest Info: " + str(latest_info))
            confirmed = latest_info['confirmed']
            # print("Confirmed: " + str(confirmed))
            deaths = latest_info['deaths']
            # print("Deaths: " + str(deaths))
            recovered = latest_info['recovered']
            # print("recovered: " + str(recovered))
            # print("\n")
            data_dict[i] = {
                'Country_ID': country_id,
                'Country': country,
                'Country_Code': country_code,
                'Population': population,
                'Province': province,
                'last_updated': last_updated,
                'coordinates': coordinates,
                'latitude': latitude,
                'longitude': longitude,
                'latest_info': latest_info,
                'confirmed': confirmed,
                'deaths': deaths,
                'recovered': recovered
            }
    return render(request, 'covid_19_api_2020/index.html', {"data_dict": data_dict})