function initMap() {
    const myLatlng = { lat: 55.756272, lng: 37.618746 };
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 6,
      center: myLatlng,
    });
    // Create the initial InfoWindow.
    let infoWindow = new google.maps.InfoWindow({
      content: "Click on map to get location!",
      position: myLatlng,
    });
    infoWindow.open(map);

    var marker = new google.maps.Marker({map: map})
    map.addListener("click", (mapsMouseEvent) => {
        infoWindow.close();
        document.getElementById("lat_dest").value = mapsMouseEvent.latLng.lat();
        document.getElementById("lon_dest").value = mapsMouseEvent.latLng.lat();
        placeMarker();
     });
  }
  function placeMarker() {
        lat = document.getElementById("lat_dest").value
        lon = document.getElementById("lon_dest").value

        marker.setPosition(lat, lon);
    }