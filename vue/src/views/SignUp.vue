<template>
<<<<<<< HEAD
  <div>
    <form>
      <p>username:</p>
      <input v-model="username" />
      <p>e-mail:</p>
      <input v-model="email" autocomplete="email" />
      <p>password:</p>
      <input v-model="password1" type="password" />
      <p>もう一度パスワードを入力してください</p>
      <input v-model="password2" type="password" />
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form_user: {
        username: "",
        email: "",
        password1: "",
        password2: "",
      },
    };
  },
};
</script>

<style scoped>
</style>
=======
  <div>SignUp</div>
</template>

<script>
export default {};
</script>
>>>>>>> f092e2f... [add] page router
