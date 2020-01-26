import requests
import json


""" RETURNS FLIGHT INFORMATION """


def flights_search(date, origin, destination):
    # data must be in YYYY-MM-DD
    flight_data = requests.get('https://airdash-flight-engine.herokuapp.com/flights?date=' + date + '&origin=' + origin +
                               '&destination='+destination)
    # make sure data is received
    response_code = str(flight_data.status_code)
    # if data then fix data points and return values
    if '2' == response_code[0]:
        # convert from json
        flight_data_dict = json.loads(flight_data.text)
        # save all flights
        flights = []
        for z in range(0, len(flight_data_dict)):
            flight = []

            """FLIGHT NUMBER"""
            flight_number = flight_data_dict[z]['flightNumber']
            flight.append(flight_number)

            """ORIGIN"""
            # code, city, timezone, latitude, longitude
            origin = []
            for x in flight_data_dict[z]['origin']:
                if x == 'location':
                    origin.append(flight_data_dict[z]['origin'][x]['latitude'])
                    origin.append(flight_data_dict[z]['origin'][x]['longitude'])
                else:
                    origin.append(flight_data_dict[z]['origin'][x])
            flight.append(origin)

            """DESTINATION"""
            # code, city, timezone, latitude, longitude
            destination = []
            for m in flight_data_dict[z]['destination']:
                if m == 'location':
                    destination.append(flight_data_dict[z]['destination'][m]['latitude'])
                    destination.append(flight_data_dict[z]['destination'][m]['longitude'])
                else:
                    destination.append(flight_data_dict[z]['destination'][m])
            flight.append(destination)

            """DISTANCE"""
            distance = flight_data_dict[z]['distance']
            flight.append(distance)

            """DURATION"""
            # hours, minutes
            duration = [flight_data_dict[z]['duration']['hours'], flight_data_dict[z]['duration']['minutes']]
            flight.append(duration)

            """DEPARTURE TIME"""
            departure_time = flight_data_dict[z]['departureTime']
            flight.append(departure_time)

            """ARRIVAL TIME"""
            arrival_time = flight_data_dict[z]['arrivalTime']
            flight.append(arrival_time)

            """AIRCRAFT"""
            # model, passenger total, passenger total main, passenger total first, speed
            aircraft = []
            for y in flight_data_dict[z]['aircraft']:
                if y == 'passengerCapacity':
                    aircraft.append(flight_data_dict[z]['aircraft'][y]['total'])
                    aircraft.append(flight_data_dict[z]['aircraft'][y]['main'])
                    aircraft.append(flight_data_dict[z]['aircraft'][y]['first'])
                else:
                    aircraft.append(flight_data_dict[z]['aircraft'][y])
            flight.append(aircraft)

            # append all flight info to flights list
            flights.append(flight)
        return flights
    else:
        return -1
