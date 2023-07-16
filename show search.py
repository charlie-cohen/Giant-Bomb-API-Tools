import requests
import json

api_key = input("Please Enter Your API Key: ")
useragent = input("Please Enter Your GB Account Name: ")
header = {
    'User-Agent': useragent,
    'Authorization': 'Bearer ' + api_key
}

url = 'https://www.giantbomb.com/api/video_shows/'
params = {
    'api_key': api_key,
    'format': 'json'
}

response = requests.get(url, headers=header, params=params)

if response.status_code == 200:
    data = response.json()
    if data['number_of_total_results'] > 0:
        results = data['results']
        for result in results:
            try:
                show_id = result['id']
                show_name = result['title']

                print(f"Show ID: {show_id}")
                print(f"Show Name: {show_name}")
                print()  # Print a blank line for separation
            except KeyError:
                print("Error: 'name' key not found in the result JSON.")
                print(json.dumps(result, indent=2))
                print()
    else:
        print('No results found for the query.')
else:
    print('Error occurred while making the API request.')
    print()
