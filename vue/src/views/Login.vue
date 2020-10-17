<template>
  <div>
    LoginPage<br />
    <p>username</p>
    <input v-model="form_data.username" placeholder="edit me" />
    <p>e-mail</p>
    <input v-model="form_data.email" placeholder="edit me" />
    <p>password</p>
    <input v-model="form_data.password" type="password" placeholder="edit me" />
    <br />
    <button v-on:click="post">Greet</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form_data: {
        username: "",
        email: "",
        password: "",
      },
    };
  },
  methods: {
    post: async function () {
      const payload = JSON.stringify(this.form_data);

      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: payload,
      };

      await fetch("http://127.0.0.1:8000/rest-auth/login/", requestOptions)
        .then((response) => response.json())
        .then((data) => {
          console.log(data.key);
          this.$store.dispatch("setUserKey", { key: data.key });
        })
        .then(() => {
          this.$router.push("/main");
        })
        .catch(() => {
          alert("ログインに失敗しました");
        });
    },
  },
};
</script>  
