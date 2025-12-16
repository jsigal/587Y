import requests
import json

base_url = 'https://pds.nasa.gov/api/search/1/'

endpoint = 'products'

params = {
    # 'q': '*',
    'limit': 10 # Optionally limit the results
}

try:
    # Make the GET request
    response = requests.get(f"{base_url}{endpoint}", params=params) #, verify=False)
    
    # Raise an exception for bad status codes (4xx or 5xx)
    response.raise_for_status()
    
    # Parse the JSON response
    data = response.json()
    
    # Print the results (or process them further)
    print(json.dumps(data, indent=2))

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")