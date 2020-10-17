<template>
  <div>
    <form>
      <p>name:</p>
      <input v-model="form_data.name" />
      <p>e-mail:</p>
      <input v-model="form_data.stl" autocomplete="email" />
    </form>

    <button v-on:click="post">Greet</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form_data: {
        name: "",
        stl: null,
        user: null,
      },
    };
  },
  methods: {
    post: async function() {
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
  },
};
</script>

<style scoped></style>
