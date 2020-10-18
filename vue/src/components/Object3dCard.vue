<template>
  <div class="l-wrapper">
    <article @click="createRequest" class="card">
      <h2>{{ title }}</h2>
      <p>{{ stl }}</p>
    </article>
  </div>
</template>

<script>
export default {
  name: "Object3dCard",
  props: {
    id: Number,
    title: String,
    stl: String
  },
  methods: {
    createRequest() {
      this.$router.push(`/object3ds/${this.id}/selectPrinter`)
    }
  }
};
</script>

<style scoped>
.l-wrapper {
  margin: 3rem auto;
  width: 200px;
}

* {
  margin: 5px;
  padding: 0;
}
.card {
  padding: 2rem;
  background-color: #fff;
  box-shadow: 0 0 8px rgba(0, 0, 0, 0.16);
  color: #212121;
  text-decoration: none;
  width: 80%;
  cursor: pointer;
}
</style>
