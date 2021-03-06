const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
const map = L.map('map', {zoomSnap: 0})
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: attribution }).addTo(map);
const centres = JSON.parse(document.getElementById('centres-data').textContent);
let feature = L.geoJSON(centres);
let markers = L.markerClusterGroup();
markers.addLayer(feature).bindPopup(function (layer) { return layer.feature.properties.name; }).addTo(map);
map.addLayer(markers);
map.fitBounds(feature.getBounds(), { padding: [100, 100] });

const reload = document.querySelector('.leaflet-control-reload');

reload.addEventListener('click', (e) => {
    e.preventDefault();
    feature.clearLayers();
    markers.clearLayers();

    feature = L.geoJSON(centres);
    markers.addLayer(feature).bindPopup(function (layer) { return layer.feature.properties.name; }).addTo(map);
    map.addLayer(markers);
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

                // clear layer
                markers.clearLayers();

                const centres = data.data;
                feature = L.geoJSON(centres);
                markers.addLayer(L.geoJSON(centres)).bindPopup(function (layer) { return layer.feature.properties.name; }).addTo(map);
                map.addLayer(markers)
                map.flyToBounds(feature.getBounds(), { padding: [100, 100] });
            })
            .catch(err => console.warn('something went wrong ', err))
        }
    });
}

document.querySelector('#districts').addEventListener('input', onInput);

const onClick = () => {
    const checkBox = document.querySelector('#toggle-btn');

    // TODO: show loading spinner

    if (!checkBox.checked) {
        // get test centres from backend
        fetch("/ajax/centres/test?" + new URLSearchParams({section: 'test'}))
        .then(response => {
            if(response.ok) {
                return response.json();
            }
            return response;
        }).then(data => {
            // clear current layer
            markers.clearLayers();

            const centres = data.data;
            feature = L.geoJSON(centres).bindPopup(function (layer) { return layer.feature.properties.name; }).addTo(map);
            map.flyToBounds(feature.getBounds(), { padding: [100, 100] });

        })
        .catch(err => console.warn('something went wrong ', err))
        console.log('checked');
        
    } else {
        console.log('not checked');
        feature.clearLayers();

        feature = L.geoJSON(centres);
        markers.addLayer(feature).bindPopup(function (layer) { return layer.feature.properties.name; }).addTo(map);
        map.addLayer(markers);
        map.flyToBounds(feature.getBounds(), { padding: [100, 100] });
    }
}

document.querySelector('.slider').addEventListener('click', onClick);



