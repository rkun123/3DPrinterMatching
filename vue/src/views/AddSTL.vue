<template>
  <div>
      <form>
          <p>name:</p>
          <input v-model="form_data.name" />
          <p>OMO</p>
          <img :src="stl" alt="Avatar" class="image">
          <label>
              selectfile
              <input type="file" @change="onFileChange" />
          </label>
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
        stl: '',
        user: this.$store.state.UserState.pk,
      },
    };
  },
  methods: {
      onFileChange(e) {
          const files = e.target.files || e.dataTransfer.files;
          this.createImage(files[0]);
      },
      // アップロードした画像を表示
      createImage(file) {
          const reader = new FileReader();
          reader.onload = e => {
              this.stl = e.target.result;
          };

          console.log(reader.readAsDataURL(file));
      },

    post: async function () {
      const payload = JSON.stringify(this.form_data);

      const requestOptions = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Authorization: "Token " + this.$store.state.UserKey,
        },
        body: payload,
      };

      await fetch(
        "http://127.0.0.1:8000/api/v1/object3d/",
        requestOptions
      )
        .then((response) => response.json())
        .then((requestOptions) => console.log(requestOptions));
    },
  },
};
</script>

<style scoped></style>
