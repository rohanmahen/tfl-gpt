import requests


def location(address):
    """
    Fetches the latitude and longitude for a given address using the Nominatim API.

    Parameters:
    address (str): The address for which the geographic coordinates are needed.

    Returns:
    tuple: A tuple containing the latitude and longitude of the address, or None if not found.
    """

    # Base URL for the Nominatim API
    base_url = "https://nominatim.openstreetmap.org/search"

    # Parameters for the API request
    params = {
        "q": address,
        "format": "json",
    }

    # Sending a GET request to the Nominatim API
    response = requests.get(base_url, params=params)
    data = response.json()

    # Check if the response is successful and contains data
    if response.status_code == 200 and len(data) > 0:
        # Extract the latitude and longitude from the response
        lat = float(data[0]["lat"])
        lng = float(data[0]["lon"])
        return lat, lng
    else:
        # Return None if no data is found or if there's an error
        return None
