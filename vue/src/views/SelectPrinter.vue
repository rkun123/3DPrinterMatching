<template>
  <div>
    <div v-for="printer in printers" :key="printer.name">
      <div class="card" @click="createRequest(printer.id)">
        <h2>距離: {{ printer.distance }}m</h2>
        <h3>{{ printer.name }}</h3>
        <p></p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      printers: [],
    };
  },
  async mounted() {
    const requestOptions = {
      method: "GET",
      headers: { Authorization: "Token " + this.$store.state.UserKey },
    };

    fetch(`http://127.0.0.1:8000/api/v1/object3d/${this.$route.params.id}/printables/`, requestOptions)
      .then((response) => response.json())
      .then((data) => {
        this.printers = data;
      });
  },
  methods: {
    createRequest(printerId) {
      const objectId = this.$route.params.id

      const body = {
        object3d: parseInt(objectId),
        printer3d: parseInt(printerId)
      }
      const requestOptions = {
        method: "POST",
        headers: { 
          Authorization: "Token " + this.$store.state.UserKey,
          "Content-type": "application/json"
        },
        body: JSON.stringify(body)
      };

      fetch("http://127.0.0.1:8000/api/v1/requests/", requestOptions)
        .then((response) => response.json())
        .then((data) => {
          this.$router.push(`/request/${data.id}`);
        });

    }
  }
};
</script>

<style scoped>
.card {
  padding: 1rem;
  margin-top: 1rem;
  border: solid 2px black; 
}
</style>
