# flight_prediction

collect_data_1.py 
Script to flight prices for  destinations with IATA code 'SFO', 'JFK', 'LAX' and 'BWI' from 'ORD' for departure dates 
30 Nov 2018 , 10th Dec 2018 and 26 Dec 2018 and 
 
collect_data_2.py
Script to flight prices for  destinations with IATA code 'DXB', 'HYD' and 'MAA' from 'ORD' for departure dates 
30 Nov 2018 , 10th Dec 2018 and 26 Dec 2018 and 

parse.py
Converts JSON data collected form collect_data_1.py and collect_data_2.py into useable features.
Futher parse.py removes outliers and assigns labels to samples.
Features used:
origin
destination 
num_hrs_until_flight
duration_of_flight_in_mins
num_of_stops
overnight_flight
day_of_week_collected
gross_fare
airline
flight_no


price.py
Implements Goibibo API which is called by collect_data_1.py and collect_data_2.py to extract realtime flight price data.

