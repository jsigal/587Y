from __future__ import print_function
import requests.exceptions

from pds.api_client.rest import ApiException
from pds.api_client import Configuration
from pds.api_client import ApiClient

from pds.api_client.api.by_product_classes_api import ByProductClassesApi
from pprint import pprint

try:
    # create an instance of the API class
    configuration = Configuration()
    configuration.host = 'https://pds.nasa.gov/api/search/1'
    api_client = ApiClient(configuration)




    classes = ByProductClassesApi(api_client)

    api_response = classes.class_list(
        'collection',
        # start=0,
        limit=20,
        fields=['ops:Label_File_Info.ops:file_ref']
    )
    pprint(api_response.summary.to_dict())
    print("API call successful!")
# except NotFoundException as e:
#     # Handle specific 404 errors (resource not found)
#     print(f"Error: Resource not found. Details: {e}")
# except UnauthorizedException as e:
#     # Handle specific 401/403 errors (authentication/permission issues)
#     print(f"Error: Authentication failed or forbidden. Details: {e}")
except ApiException as e:
    # Handle other general API errors caught by the client
    print(f"An API error occurred: {e}")
except requests.exceptions.RequestException as e:
    # Handle underlying network/connection errors (e.g., DNS failure, server offline)
    print(f"A connection error occurred: {e}")
except Exception as e:
    # Catch any other unexpected Python exceptions
    print(f"An unexpected error occurred: {e}")