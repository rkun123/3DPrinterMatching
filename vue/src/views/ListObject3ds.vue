<template>
  <div>
    <div v-for="obj in objs" :key="obj">
      <Object3dCard
        :title="obj.name"
        :stl="obj.stl"
        :id="obj.id"
      />
    </div>
  </div>
</template>

<script>
import Object3dCard from "../components/Object3dCard.vue";

export default {
  data() {
    return {
      objs: [],
    };
  },
  components: {
    Object3dCard,
  },
  async mounted() {
    const requestOptions = {
      method: "GET",
      headers: { Authorization: "Token " + this.$store.state.UserKey },
    };

    fetch(`http://localhost:8000/api/v1/users/${this.$store.state.UserState.id}/object3ds/`, requestOptions)
      .then((response) => response.json())
      .then((data) => {
        this.objs = data;
      });
  },
};
</script>

<style scoped></style>
