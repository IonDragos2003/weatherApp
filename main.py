# Write the API client
# Write the main logic
from weatherApp.const import API_KEY
from weatherApp.clients.api_client import astronomy_call

q = 'London' # str | Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name. Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to learn more. 
dt = '2013-10-20' # date | Date on or after 1st Jan, 2015 in yyyy-MM-dd format


api_response = astronomy_call(q, dt)
print(api_response)