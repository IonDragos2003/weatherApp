from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
from weatherApp.const import API_KEY

#print(API_KEY)


# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['key'] = API_KEY
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.APIsApi(swagger_client.ApiClient(configuration))

def sum(a,b):
    return a+b

def astronomy_call(q, dt):
    try:
        # Astronomy API
        api_response = api_instance.astronomy(q, dt)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling APIsApi->astronomy: %s\n" % e)
    return api_response
