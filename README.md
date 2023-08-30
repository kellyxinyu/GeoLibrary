# GeoLibrary
The GeoLibrary contains geocoder_gmap and distancematrix_gmap

### Installation
```bash
git clone https://github.com/kellyxinyu/GeoLibrary.git

# navigate to the cloned repository's directory
pip install .
```

### Usage
```python
from GeoLibrary import geocoder

geocoder.geocoder_gmap(street, city, state, api_key)
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
geocoder.distancematrix_gmap(start_latitude, start_longitude, end_latitude, end_longitude, api_key)
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
# LY api_key: 'AIzaSyBqr60VzhSJ7eRx6wAyyWG60WZ8tc-sfII'
```
