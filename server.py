import http.server
import json
import mysql.connector
import cgi

# Total number of tables available in the restaurant
TOTAL_TABLES = 10

class ReservationServer(http.server.BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Thienandeptrai123',
                port=3306,
                database='reservations'
            )
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as err:
            print("Error connecting to MySQL:", err)
        super().__init__(*args, **kwargs)

    def _set_response(self, content_type='application/json'):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def create_table(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS reservations (
                    reservation_id INT AUTO_INCREMENT PRIMARY KEY,
                    customer_name VARCHAR(100) NOT NULL,
                    reservation_date DATE NOT NULL,
                    reservation_time TIME NOT NULL,
                    party_size INT NOT NULL
                )
            """)
            print("Table 'reservations' created successfully.")
        except mysql.connector.Error as err:
            print("Error creating table:", err)


    def do_GET(self):
        if self.path == '/reservations':
            self.create_table() # Create table if not exists
            self.cursor.execute("SELECT * FROM reservations")
            reservations = self.cursor.fetchall()
            remaining_tables = TOTAL_TABLES - len(reservations)
        
            # Format date and time fields
            formatted_reservations = []
            for reservation in reservations:
                formatted_reservation = {
                    'reservation_id': reservation[0],
                    'customer_name': reservation[1],
                    'reservation_date': reservation[2].strftime('%Y-%m-%d'),  # Format date
                    'reservation_time': str(reservation[3]),  # Convert time to string
                    'party_size': reservation[4]
                }
                formatted_reservations.append(formatted_reservation)

            response = {
                'reservations': formatted_reservations,
                'remaining_tables': remaining_tables
            }
            self._set_response()
            self.wfile.write(json.dumps(response).encode())
        else:
            self._set_response()
            response = {
                'message': 'Welcome to Restaurant Reservation System',
                'endpoints': [
                    {'reservations': 'Get all reservations'},
                    {'make_reservation': 'Make a reservation'}
                ]
            }
            self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        if self.path == '/reservations':
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            content_len = int(self.headers.get('content-length'))
        
            if ctype == 'application/json':
                post_data = self.rfile.read(content_len)
                new_reservation = json.loads(post_data.decode())
                self.cursor.execute("INSERT INTO reservations (customer_name, reservation_date, reservation_time, party_size) VALUES (%s, %s, %s, %s)", (new_reservation['customer_name'], new_reservation['reservation_date'], new_reservation['reservation_time'], new_reservation['party_size']))
                self.conn.commit()
                self._set_response()
                self.wfile.write(json.dumps(new_reservation).encode())
                self.wfile.write(json.dumps({'success': True}).encode())
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(json.dumps({'success': False, 'error': 'error'}).encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(json.dumps({'success': False, 'error': 'Invalid request format'}).encode())
            
    def do_DELETE(self):
        if self.path.startswith('/reservations/'):
            reservation_id = int(self.path.split('/')[-1])
            try:
                self.cursor.execute("DELETE FROM reservations WHERE reservation_id = %s", (reservation_id,))
                self.conn.commit()
                self._set_response()
                response = {'message': f"Reservation with ID {reservation_id} deleted successfully."}
                self.wfile.write(json.dumps(response).encode())
            except mysql.connector.Error as err:
                self.send_response(500)
                self.end_headers()
                response = {'error': f"Error deleting reservation: {err}"}
                self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.end_headers()
            response = {'error': 'Invalid endpoint for deletion.'}
            self.wfile.write(json.dumps(response).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()


    def __del__(self):
        # Close database connection
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    server_address = ('', 8080)
    httpd = http.server.HTTPServer(server_address, ReservationServer)
    print('Starting server...')
    httpd.serve_forever()
