function planTrip() {
    // Get user inputs
    const destination = document.getElementById('destination').value;
    const startDate = document.getElementById('start-date').value;
    const endDate = document.getElementById('end-date').value;

    // Validate inputs
    if (!destination || !startDate || !endDate) {
        alert('Please fill in all fields.');
        return;
    }

    // Display trip information
    const tripInfo = `Destination: ${destination}<br>
                      Start Date: ${startDate}<br>
                      End Date: ${endDate}`;

    document.getElementById('trip-info').innerHTML = tripInfo;
}