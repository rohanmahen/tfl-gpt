import requests


def journey(origin: tuple, destination: tuple):
    """
    Retrieves the fastest journey information between two points from the TfL API.

    Parameters:
    origin (tuple): A tuple of latitude and longitude for the origin.
    destination (tuple): A tuple of latitude and longitude for the destination.

    Returns:
    str: A formatted string containing the details of the fastest journey, or an error message.
    """

    # Formatting the origin and destination coordinates into strings
    origin_str = f"{origin[0]},{origin[1]}"
    destination_str = f"{destination[0]},{destination[1]}"

    # Constructing the API endpoint URL
    api_url = f"https://api.tfl.gov.uk/journey/journeyresults/{origin_str}/to/{destination_str}"

    # Sending a GET request to the TfL API
    response = requests.get(api_url)

    # Check for successful response
    if response.status_code == 200:
        data = response.json()

        # Ensuring 'journeys' key exists in response data
        if "journeys" in data:
            journeys = data["journeys"]

            # Handling the case where no journeys are found
            if not journeys:
                return "No journeys found."
            else:
                # Identifying the fastest journey based on duration
                fastest_journey = min(
                    journeys, key=lambda journey: journey.get("duration", float("inf"))
                )

                # Constructing the journey information string
                journey_info = ["Fastest Journey:"]
                journey_info.extend(
                    [
                        f"Departure Time: {fastest_journey['startDateTime']}",
                        f"Arrival Time: {fastest_journey['arrivalDateTime']}",
                        f"Total Duration: {fastest_journey['duration']} minutes",
                    ]
                )

                # Adding fare information if available
                if "fare" in fastest_journey:
                    journey_info.append(
                        f"Total Cost: £{fastest_journey['fare']['totalCost'] / 100:.2f}"
                    )

                # Adding detailed leg information
                journey_info.append("Journey Details:")
                for leg in fastest_journey.get("legs", []):
                    journey_info.extend(
                        [
                            f"- Leg: {leg['instruction']['summary']}",
                            f"  - Departure Time: {leg['departureTime']}",
                            f"  - Arrival Time: {leg['arrivalTime']}",
                            f"  - Departure Point: {leg['departurePoint']['commonName']}",
                            f"  - Arrival Point: {leg['arrivalPoint']['commonName']}",
                            f"  - Line: {leg.get('lineName', 'N/A')}",
                        ]
                    )

                return "\n".join(journey_info)
        else:
            return "No journeys found in the data."
    else:
        # Handling API errors
        return f"Error: Unable to retrieve journey data. Status code: {response.status_code}"
