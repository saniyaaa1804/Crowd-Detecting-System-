let map;

function initMap() {
    const mumbai = { lat: 19.0760, lng: 72.8777 };
    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 12,
        center: mumbai
    });
}

function fetchCrowdData() {
    let station = document.getElementById("station").value;
    
    // Simulated API call (replace with your actual API endpoint)
    $.get(`/get_crowd_density?station=${station}`, function(data) {
        // Simulated response data (for demonstration purposes)
        const simulatedData = {
            density: Math.floor(Math.random() * 100), // Random density for demo
        };

        // Use simulated data instead of actual API response
        document.getElementById("crowd-density").innerText = simulatedData.density;
    });
}

function exitWebsite() {
    window.close(); // Close the current window (may not work in all browsers)
}
