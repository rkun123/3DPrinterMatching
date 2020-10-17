<template>
<<<<<<< HEAD
  <div class="start">
    <img src="../assets/logo.png" />
    <h1>3DPrinter Matching</h1>
    <h2>description</h2>
    <button @click="login">Login</button>
    <button @click="signup">Signup</button>
  </div>
</template>

<script>
export default {
  methods: {
    login() {
      this.$router.push("/login");
    },
    signup() {
      this.$router.push("/signup");
    },
  },
};
</script>

<style scoped>
button {
  margin: 10px;
  padding-top: 5px;
  padding-bottom: 5px;
  padding-left: 15px;
  padding-right: 15px;
}
</style>
=======
  <div>Start Page</div>
</template>

<script>
export default {};
</script>
>>>>>>> f092e2f... [add] page router
