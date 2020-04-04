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


def latest(request):
    new_data_dict = {}
    # context = {}
    url = "https://covidtracking.com/api/states"
    response = requests.get(url)
    data = response.json()
    # print(data)
    # for item in data:
    #     for key, value in item.items():
    #         print(key)
    #         print(value)
    #         print("\n")
        # print(data[item])
        # state_abbr = data[item]['state']
        # print(state_abbr)
        # positive_tests = data[item]['positive']
        # print("Positive Tests: {}".format(positive_tests))
        # negative_tests = data[item]['negative']
        # print("Negative Tests: {}".format(negative_tests))
        # pending_tests = data[item]['pending']
        # print("Pending Tests: {}".format(pending_tests))
        # hospitalized_currently = data[item]['hospitalizedCurrently']
        # print("Hospitalized Currently: {}".format(hospitalized_currently))
        # hospitalized_cumulative = data[item]['hospitalizedCumulative']
        # print("Hospitalized Cumulative: {}".format(hospitalized_cumulative))
        # # positive_score = data[item]['positiveScore']
        # # print("Positive Score: {}".format(positive_score))
        # # negative_score = data[item]['negativeScore']
        # # print("Negative Score: {}".format(negative_score))
        # # negative_regular_score = data[item]['negativeRegularScore']
        # # print("Negative Regular Score: {}".format(negative_regular_score))
        # # grade = data[item]['grade']
        # # print("Grade: {}".format(grade))
        # pending = data[item]['pending']
        # print("Pending: {}".format(pending))
        # print("\n")
    print(data)
    context = {
        'data': data,
    }
    for item in range(0, len(data)):
        print(data[item])
        state_abbr = data[item]['state']
        print(state_abbr)
        positive_tests = data[item]['positive']
        print("Positive Tests: {}".format(positive_tests))
        negative_tests = data[item]['negative']
        print("Negative Tests: {}".format(negative_tests))
        pending_tests = data[item]['pending']
        print("Pending Tests: {}".format(pending_tests))
        hospitalized_currently = data[item]['hospitalizedCurrently']
        print("Hospitalized Currently: {}".format(hospitalized_currently))
        hospitalized_cumulative = data[item]['hospitalizedCumulative']
        print("Hospitalized Cumulative: {}".format(hospitalized_cumulative))
        # negative_score = data[item]['negativeScore']
        # print("Negative Score: {}".format(negative_score))
        # negative_regular_score = data[item]['negativeRegularScore']
        # print("Negative Regular Score: {}".format(negative_regular_score))
        # grade = data[item]['grade']
        # print("Grade: {}".format(grade))
        pending = data[item]['pending']
        print("Pending: {}".format(pending))
        date_checked = data[item]['dateChecked']
        print("Date Checked: {}".format(date_checked))
        new_data_dict[item] = {
            "state_abbr": state_abbr,
            "positive_tests": positive_tests,
            "negative_tests": negative_tests,
            "pending_tests": pending_tests,
            "hospitalized_currently": hospitalized_currently,
            "hospitalized_cumulative": hospitalized_cumulative
        }
        print("\n")
    return render(request, 'covid_19_api_2020/latest.html', {"new_data_dict": new_data_dict})