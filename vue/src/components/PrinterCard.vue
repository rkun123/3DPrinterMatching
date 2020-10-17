<template>
  <div class="l-wrapper">
    <article class="card">
      <h2>{{ title }}</h2>
      <p>幅:{{ width }} [mm]</p>
      <p>高さ:{{ height }} [mm]</p>
      <p>奥行き:{{ depth }} [mm]</p>
    </article>
  </div>
</template>

<script>
export default {
  name: "PrinterCard",
  props: {
    title: String,
    width: String,
    height: String,
    depth: String,
  },
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
  padding: auto;
  background-color: #fff;
  box-shadow: 0 0 8px rgba(0, 0, 0, 0.16);
  color: #212121;
  text-decoration: none;
}
</style>
