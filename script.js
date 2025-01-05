// Check if Geolocation is Supported
if ("geolocation" in navigator) {
    navigator.geolocation.getCurrentPosition(
        // Success Callback
        function (position) {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;

            console.log("Latitude:", latitude);
            console.log("Longitude:", longitude);

            // Fetch City and Country
            fetch(`https://api.bigdatacloud.net/data/reverse-geocode-client?latitude=${latitude}&longitude=${longitude}&localityLanguage=en`)
                .then(response => response.json())
                .then(geoData => {
                    const city = geoData.city || 'Unknown City';
                    const country = geoData.countryName || 'Unknown Country';
                    console.log(`City: ${city}, Country: ${country}`);
                })
                .catch(error => console.error("Error fetching city and country:", error));

            // Get Current Date in Required Format
            const currentDate = new Date();
            const formattedDate = `${currentDate.getDate()}-${currentDate.getMonth() + 1}-${currentDate.getFullYear()}`;

            console.log("Current Date:", formattedDate);

            // Fetch Prayer Times
            fetch(`https://api.aladhan.com/v1/timings/${formattedDate}?latitude=${latitude}&longitude=${longitude}&method=1`)
                .then(response => response.json())
                .then(data => {
                    const { Fajr, Maghrib } = data.data.timings;

                    // Convert Times to 12-Hour Format
                    document.getElementById("suhoor").textContent = convertTo12HourFormat(Fajr);
                    document.getElementById("iftar").textContent = convertTo12HourFormat(Maghrib);
                })
                .catch(error => {
                    console.error("Error fetching prayer times:", error);
                    document.getElementById("suhoor").textContent = "Error fetching time.";
                    document.getElementById("iftar").textContent = "Error fetching time.";
                });
        },
        // Error Callback
        function (error) {
            console.error("Geolocation error:", error.message);
            document.getElementById("suhoor").textContent = "Location access denied.";
            document.getElementById("iftar").textContent = "Location access denied.";
        }
    );
} else {
    console.log("Geolocation not supported.");
    document.getElementById("suhoor").textContent = "Geolocation not supported.";
    document.getElementById("iftar").textContent = "Geolocation not supported.";
}

// Function to Convert 24-Hour Time to 12-Hour Format
function convertTo12HourFormat(time) {
    const [hours, minutes] = time.split(":").map(Number);
    const period = hours >= 12 ? "PM" : "AM";
    const hours12 = hours % 12 || 12;
    return `${hours12}:${minutes < 10 ? "0" + minutes : minutes} ${period}`;
}

// Set Current Year in Footer
document.getElementById("year").textContent = new Date().getFullYear();