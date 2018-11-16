const mymap = L.map('mapid').setView([55.75497, 37.62432], 10);
L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1Ijoia3kzaGU0aWsiLCJhIjoiY2pvZnA0d3BzMDY3bDN4cXJ4eDg3NjE3NSJ9.SiLSIUGchbNQWCLmwSpTxQ', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.streets',
    accessToken: 'your.mapbox.access.token'
}).addTo(mymap);

var marker = L.marker([55.75497, 37.62432]).addTo(map);
    marker.bindPopup(marker.latlng).openPopup();
function onMapClick(e) {
    marker.setLatLng(e.latlng);

     popup
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " + e.latlng.toString())
        .openOn(mymap);
}

function onClick(e) {
    marker.bindPopup(e.latlng).openPopup();
}

marker.on('click', onClick);
mymap.on('click', onMapClick);