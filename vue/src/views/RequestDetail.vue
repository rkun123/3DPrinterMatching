<template>
  <div>
    <h1>{{ this.request.id }}</h1>
    <h1>プリンター: {{ this.printer.name }}</h1>
    <a :href="this.object3d.stl"> <h1>ファイル: {{ this.object3d.name }}</h1> </a>
  </div>
</template>

<script>
export default {
  data() {
    return {
      request: {},
      printer: {},
      object3d: {},
      dm: []
    };
  },
  created() {
    const requestId = this.$route.params.id
    const requestOptions = {
      method: "GET",
      headers: { Authorization: "Token " + this.$store.state.UserKey },
    };
    console.log("fetching")
    // fetch request
    fetch(`http://127.0.0.1:8000/api/v1/requests/${requestId}/`, requestOptions)
      .then((response) => response.json())
      .then((req) => {
        this.request = req
        console.log(this.request)
        fetch(`http://127.0.0.1:8000/api/v1/printer3d/${req.printer3d}/`, requestOptions)
          .then((response) => response.json())
          .then((data) => {
            this.printer = data
            console.log(this.request)
            fetch(`http://127.0.0.1:8000/api/v1/object3d/${req.object3d}/`, requestOptions)
              .then((response) => response.json())
              .then((data) => {
                this.object3d = data
                console.log(this.request)
                fetch(`http://127.0.0.1:8000/api/v1/requests/${requestsId}/di`, requestOptions)
                  .then((response) => response.json())
                  .then((data) => {
                    this.object3d = data
                    console.log(this.request)
                  })
              })
          })
      })
  },
};
</script>
