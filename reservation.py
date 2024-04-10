import requests
import json

url = 'http://localhost:8080/reservations'

# Data to be inserted into the reservations table
reservation_data = {
    'customer_name': 'Austin Ngo',
    'reservation_date': '2022-04-16',
    'reservation_time': '19:30:00',
    'party_size': 6
}

# Convert the reservation data to JSON format
json_data = json.dumps(reservation_data)

# Set the headers to specify that the content type is JSON
headers = {'Content-Type': 'application/json'}

# Send a POST request with JSON data
response = requests.post(url, data=json_data, headers=headers)

# Print the response
print(response.text)
