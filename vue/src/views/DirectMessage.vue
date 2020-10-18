<template>
  <div>
    <input type="text" v-model="sendMessage" />
    <button>送信</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      sendMessage: "",
      messages: [],
    };
  },
  async mounted() {
    const requestOptions = {
      method: "GET",
      headers: { Authorization: "Token " + this.$store.state.UserKey },
    };

    fetch("http://127.0.0.1:8000/api/v1/printer3d/", requestOptions)
      .then((response) => response.json())
      .then((data) => {
        for (var item in data) {
          console.log(item + ":" + data[item]["user"]["id"]);
        }
      });
  },
};
</script>
