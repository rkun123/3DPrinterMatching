<template>
  <div>
    <form>
      <p>username:</p>
      <input v-model="form_data.username" />
      <p>e-mail:</p>
      <input v-model="form_data.email" autocomplete="email" />
      <p>password:</p>
      <input v-model="form_data.password1" type="password" />
      <p>もう一度パスワードを入力してください</p>
      <input v-model="form_data.password2" type="password" />
    </form>

    <GoogleMap @parentMethod="updatePosition" />
    <button v-on:click="post">Greet</button>
  </div>
</template>

<script>
import GoogleMap from "../components/GoogleMap.vue";

export default {
  data() {
    return {
      form_data: {
        username: "",
        email: "",
        password1: "",
        password2: "",
        lat: 0,
        lng: 0,
      },
    };
  },
  components: {
    GoogleMap,
  },
  methods: {
    post: async function () {
      const payload = JSON.stringify(this.form_data);

      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: payload,
      };

      await fetch(
        "http://127.0.0.1:8000/rest-auth/registration/",
        requestOptions
      )
        .then((response) => response.json())
        .then((requestOptions) => console.log(requestOptions));
    },
    updatePosition(Position) {
      this.lat = Position.lat;
      this.lng = Position.lng;
    },
  },
};
</script>

<style scoped></style>
