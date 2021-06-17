const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
const map = L.map('map', {zoomSnap: 0})
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: attribution }).addTo(map);
const centres = JSON.parse(document.getElementById('centres-data').textContent);
let feature = L.geoJSON(centres).bindPopup(function (layer) { return layer.feature.properties.name; }).addTo(map);
map.fitBounds(feature.getBounds(), { padding: [100, 100] });

const reload = document.querySelector('.leaflet-control-reload');

reload.addEventListener('click', (e) => {
    e.preventDefault();

    map.flyToBounds(feature.getBounds(), { padding: [100, 100] });
})


// var corner1 = L.latLng(0.2480, 32.4363),
// corner2 = L.latLng(0.3737, 32.6509),
// bounds = L.latLngBounds(corner1, corner2);
// map.flyToBounds(bounds);

// var corner1 = L.latLng(0.2031, 32.5113),
// corner2 = L.latLng(0.3287, 32.7259),
// bounds = L.latLngBounds(corner1, corner2);
// map.flyToBounds(bounds);


const onInput = () => {
    let val = document.querySelector('#districts');
    let opts = document.querySelector('#districts-list').childNodes;

    opts.forEach(dist => {
        if(dist.value == val.value) {
            // send the value to backend
            fetch("/ajax/filter?" + new URLSearchParams({district: dist.value}))
            .then(response => {
                if(response.ok) {
                    return response.json()
                }
                return response;
            }).then(data => {
                // clear input
                val.value = ""
                const centres = data.data;
                let feature = L.geoJSON(centres).bindPopup(function (layer) { return layer.feature.properties.name; }).addTo(map);
                map.flyToBounds(feature.getBounds(), { padding: [100, 100] });
            })
            .catch(err => console.warn('something went wrong ', err))
        }
    });
}

document.querySelector('#districts').addEventListener('input', onInput);




