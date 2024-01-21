import requests


def location(address):
    base_url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": address,
        "format": "json",
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200 and len(data) > 0:
        # Extract the lat/lng from the response
        lat = float(data[0]["lat"])
        lng = float(data[0]["lon"])
        return lat, lng
    else:
        return None
