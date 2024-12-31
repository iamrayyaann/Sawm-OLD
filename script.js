if ("geolocation" in navigator) {
    navigator.geolocation.getCurrentPosition(
        function (position) {

            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;
            console.log("Latitude is:", latitude);
            console.log("Longitude is:", longitude);

            // Fetch city and country based on lat and long using reverse geocoding API
            fetch(`https://api.bigdatacloud.net/data/reverse-geocode-client?latitude=${latitude}&longitude=${longitude}&localityLanguage=en`)
                .then(response => response.json())
                .then(geoData => {
                    const city = geoData.city || 'Unknown City';
                    const country = geoData.countryName || 'Unknown Country';
                    console.log(`City: ${city}, Country: ${country}`);
                })
                .catch(error => console.error('Error fetching city and country:', error));

            // Get the current date in the required format (DD-MM-YYYY)
            const currentDate = new Date();
            const formattedDate = `${currentDate.getDate()}-${currentDate.getMonth() + 1}-${currentDate.getFullYear()}`;
            console.log("Current Date is:", formattedDate);

            // Fetch prayer times for the current date and location using Al Adhan API
            fetch(`https://api.aladhan.com/v1/timings/${formattedDate}?latitude=${latitude}&longitude=${longitude}&method=1`)
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                    const { Fajr, Maghrib } = data.data.timings;

                    // Convert times to 12-hour format
                    const fajrTime12hr = convertTo12HourFormat(Fajr);
                    const maghribTime12hr = convertTo12HourFormat(Maghrib);

                    // Display times on the page
                    document.getElementById("suhoor").innerText = `${fajrTime12hr}`;
                    document.getElementById("iftar").innerText = `${maghribTime12hr}`;
                })
                .catch(error => console.error('Error fetching prayer times:', error));
        },
        function (error) {
            console.error("Error Code = " + error.code + " - " + error.message);
        }
    );
} else {
    console.log("Geolocation is not supported by this browser.");
}

// Function to convert 24-hour time format to 12-hour time format with AM/PM
function convertTo12HourFormat(time) {
    const [hours, minutes] = time.split(":").map(num => parseInt(num, 10));

    const period = hours >= 12 ? 'PM' : 'AM';
    const hours12 = hours % 12 || 12; // Convert 0 to 12 for 12-hour format
    const minutesFormatted = minutes < 10 ? `0${minutes}` : minutes;

    return `${hours12}:${minutesFormatted} ${period}`;
}