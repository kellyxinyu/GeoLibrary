import time
import requests

def geocoder_gmap(street, city, state, api_key):
    """
    Get latitude and longitude using Google Maps Geocoder API.

    Parameters:
    street (str): street address
    city (str): city of the address
    state (str): state of the address
    api_key (str): Google Maps API key for authentication.

    Returns:
    List or None: A list containing latitude and longitude information.
                 If the API call fails or no data is available, returns None.
    """

    LatLngData = []
    StreetAddress = str(street)
    idpnd = StreetAddress.find('#')
    
    if idpnd != -1:
        StreetAddress = StreetAddress[:idpnd]
        
    CityAddress = str(city).strip()
    StateAddress = str(state).strip()
    
    request_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={StreetAddress.replace(" ", "+")},+{CityAddress.replace(" ", "+")},+{StateAddress.replace(" ", "+")}&key={api_key}'
    
    try:
        GeoData = requests.get(request_url).json()
    except:
        time.sleep(5)
        GeoData = requests.get(request_url).json()
        
    if GeoData['status'] in ('ZERO_RESULTS', 'OVER_QUERY_LIMIT'):
        LatLngData = [float('nan'), float('nan')]
        return LatLngData
      

    if isinstance(GeoData['results'], list):
        latLngData = [GeoData['results'][0]['geometry']['location']['lat'], GeoData['results'][0]['geometry']['location']['lng']]
    else:
        latLngData = [GeoData['results']['geometry']['location']['lat'], GeoData['results']['geometry']['location']['lng']]

    return latLngData


def distancematrix_gmap(start_latitude, start_longitude, end_latitude, end_longitude, api_key):
    """
    Get drive time and distance information using Google Maps Distance Matrix API.

    Parameters:
    start_latitude (float): Latitude of the starting location.
    start_longitude (float): Longitude of the starting location.
    end_latitude (float): Latitude of the destination location.
    end_longitude (float): Longitude of the destination location.
    api_key (str): Google Maps API key for authentication.

    Returns:
    dict or None: A dictionary containing drive time and distance information.
                 If the API call is successful, the dictionary has the following keys:
                 - 'drive_time_minutes': Drive time in minutes.
                 - 'distance_miles': Distance in miles.
                 If the API call fails or no data is available, returns None.
    """

    request_url = f'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={start_latitude},{start_longitude}&destinations={end_latitude},{end_longitude}&key={api_key}'

    distancematrix = requests.get(request_url).json()

    if 'status' in distancematrix and distancematrix['status'] == 'OK':
        if 'elements' in distancematrix['rows'][0]:
            elements = distancematrix['rows'][0]['elements']
            if 'distance' in elements[0] and 'duration' in elements[0]:
                mile2km = 0.621371
                drive_time_minutes = [round(element['duration']['value'] / 60, 2) for element in elements]
                distance_miles = [round(element['distance']['value'] * mile2km / 1000, 1) for element in elements]
                return {
                    'drive_time_minutes': drive_time_minutes[0],
                    'distance_miles': distance_miles[0]
                }
    return None