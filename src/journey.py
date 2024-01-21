import requests


def journey(origin: tuple, destination: tuple):
    # Convert the tuples to strings for the API endpoint
    origin_str = f"{origin[0]},{origin[1]}"
    destination_str = f"{destination[0]},{destination[1]}"

    # Define the API endpoint
    api_url = f"https://api.tfl.gov.uk/journey/journeyresults/{origin_str}/to/{destination_str}"

    # Make a GET request to the TfL API
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()

        # Check if journeys are present in the response
        if "journeys" in data:
            journeys = data["journeys"]

            if not journeys:
                return "No journeys found."
            else:
                # Find the fastest journey
                fastest_journey = min(
                    journeys, key=lambda journey: journey.get("duration", float("inf"))
                )

                journey_info = []
                journey_info.append("Fastest Journey:")
                journey_info.append(
                    f"Departure Time: {fastest_journey['startDateTime']}"
                )
                journey_info.append(
                    f"Arrival Time: {fastest_journey['arrivalDateTime']}"
                )
                journey_info.append(
                    f"Total Duration: {fastest_journey['duration']} minutes"
                )

                # Check if 'fare' information is available
                if "fare" in fastest_journey:
                    journey_info.append(
                        f"Total Cost: £{fastest_journey['fare']['totalCost'] / 100:.2f}"
                    )

                journey_info.append("Journey Details:")
                for leg in fastest_journey.get("legs", []):
                    journey_info.append(f"- Leg: {leg['instruction']['summary']}")
                    journey_info.append(f"  - Departure Time: {leg['departureTime']}")
                    journey_info.append(f"  - Arrival Time: {leg['arrivalTime']}")
                    journey_info.append(
                        f"  - Departure Point: {leg['departurePoint']['commonName']}"
                    )
                    journey_info.append(
                        f"  - Arrival Point: {leg['arrivalPoint']['commonName']}"
                    )
                    journey_info.append(f"  - Line: {leg.get('lineName', 'N/A')}")

                return "\n".join(journey_info)
        else:
            return "No journeys found in the data."
    else:
        return f"Error: Unable to retrieve journey data. Status code: {response.status_code}"


