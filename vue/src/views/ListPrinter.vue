<template>
  <div>
    <div v-for="form_data_in in form_data" :key="form_data_in">
      <div>
        {{ form_data_in.name }}
        {{ form_data_in.max_width }}
        {{ form_data_in.max_height }}
        {{ form_data_in.max_depth }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form_data: [],
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
        this.form_data = data;

        console.log(this.form_data);
      });
  },
};
</script>

<style scoped></style>
