const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
const map = L.map('map')
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: attribution }).addTo(map);
const centres = JSON.parse(document.getElementById('centres-data').textContent);
let feature = L.geoJSON(centres).bindPopup(function (layer) { return layer.feature.properties.name; }).addTo(map);
map.fitBounds(feature.getBounds(), { padding: [100, 100] });

