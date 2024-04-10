// Function to make a reservation
function makeReservation() {
    const customerName = document.getElementById('customer-name').value;
    const reservationDate = document.getElementById('reservation-date').value;
    const reservationTime = document.getElementById('reservation-time').value;
    const partySize = document.getElementById('party-size').value;

    const reservationData = {
        customer_name: customerName,
        reservation_date: reservationDate,
        reservation_time: reservationTime,
        party_size: parseInt(partySize)
    };

    fetch('http://localhost:8080/reservations', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(reservationData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("Reservation successful!");
            window.location.href = "confirm.html"
        } else {
            alert("Sorry, all tables are reserved for this date and time.");
        }
        // Update reservation list
        getReservations();
    })
    .catch(error => console.error('Error:', error));
}

// Function to fetch and display reservations
function getReservations() {
    fetch('http://localhost:8080/reservations')
    .then(response => response.json())
    .then(data => {
        const reservationList = document.getElementById('reservation-list');
        
        // Clear previous list
        reservationList.innerHTML = '';

        // Append existing reservations
        if (data.reservations.length > 0) {
            data.reservations.forEach(reservation => {
                const listItem = document.createElement('li');
                listItem.textContent = `ID: ${reservation.reservation_id}, Name: ${reservation.customer_name}, Date: ${reservation.reservation_date}, Time: ${reservation.reservation_time}, Party Size: ${reservation.party_size}`;
                reservationList.appendChild(listItem);
            });
        } else {
            const noReservationItem = document.createElement('li');
            noReservationItem.textContent = 'No reservations available.';
            reservationList.appendChild(noReservationItem);
        }
    })
    .catch(error => console.error('Error:', error));
}




