<template>
  <div>
    <GmapMap
      :center="center"
      :zoom="15"
      :options="{ streetViewControl: false }"
      map-type-id="terrain"
      style="width: auto; height: 300px"
      @click="mapClick"
    >
      <GmapMarker
        :key="index"
        v-for="(m, index) in markers"
        :position="m.position"
        :clickable="true"
        :draggable="true"
        @dragend="mapClick"
      />
    </GmapMap>
    <input type="text" v-model="address" />
    <button @click="Mapsearch()">change</button>
    <div>{{ msg }}</div>
  </div>
</template>

<script>
import { gmapApi } from "vue2-google-maps";

export default {
  name: "HelloWorld",
  data() {
    return {
      msg: "",
      address: "",
      text: "",
      geocoder: {},
      map: "",
      center: { lat: 35.66606091, lng: 139.41392096 },
      markers: [{ position: { lat: 35.66606091, lng: 139.41392096 } }],
    };
  },

  computed: { google: gmapApi },

  created: function () {
    this.$gmapApiPromiseLazy({}).then(() => {
      this.autocompleteService = new this.google.maps.places.AutocompleteService();
      this.geocoder = new this.google.maps.Geocoder();
      this.geocoderStatus = this.google.maps.GeocoderStatus;
    });
  },

  methods: {
    mapClick($event) {
      //$event.latLngにクリック地点が入っている
      this.msg = `(${$event.latLng
        .lat()
        .toFixed(7)} , ${$event.latLng.lng().toFixed(7)})`;
      this.markers = [{ position: $event.latLng }];
      const Lat = $event.latLng.lat();
      const Lng = $event.latLng.lng();
      const child_position = {
        lat: Lat,
        lng: Lng,
      };
      this.$emit("parentMethod", child_position);
    },

    Mapsearch() {
      this.geocoder.geocode(
        {
          address: this.address,
        },
        (results, status) => {
          if (status === this.geocoderStatus.OK) {
            const Lat = results[0].geometry.location.lat();
            const Lng = results[0].geometry.location.lng();
            this.msg = `(${Lat} ,  ${Lng}) ${results[0].formatted_address}`;
            this.center = { lat: Lat, lng: Lng };
            this.markers = [{ position: { lat: Lat, lng: Lng } }];
            this.$emit("parentMethod", this.center);
          } else {
            this.msg = "お探しの住所は存在しません。";
          }
        }
      );
    },
  },

  mounted() {
    const self = this;
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(function (position) {
        self.msg = `(${position.coords.latitude} , ${position.coords.longitude})`;
        self.center = {
          lat: position.coords.latitude,
          lng: position.coords.longitude,
        };
        self.markers = [
          {
            position: {
              lat: position.coords.latitude,
              lng: position.coords.longitude,
            },
          },
        ];
      });
    }
  },
};
</script>
