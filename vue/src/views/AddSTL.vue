<template>
  <div>
    <form>
      <p>name:</p>
      <input v-model="form_data.name" />
      <p>OMO</p>
      <label>
        <input type="file" id="stlFileInput" @change="onFileChange" />
      </label>
    </form>
    <button v-on:click="post" class="sendButton">Send</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form_data: {
        name: "",
        stl: "",
        user: this.$store.state.UserState.id,
      },
    };
  },
  methods: {
    onFileChange(e) {
      const files = e.target.files || e.dataTransfer.files;
      this.createImage(files[0]);
    },
    createImage(file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        this.stl = e.target.result;
      };

      console.log(reader.readAsDataURL(file));
    },

    post: async function() {
      const fileInput = document.querySelector('#stlFileInput');
      const formData = new FormData();
      formData.append("name", this.form_data.name);
      formData.append("stl", fileInput.files[0]);
      formData.append("user", this.form_data.user);

      console.log(this.form_data.user);

      const requestOptions = {
          method: "POST",
          headers: {
              "Content-Type": "multipart/form-data",
              Authorization: "Token " + this.$store.state.UserKey,
          },
          body: formData,
      };

      // ここで明示的に消してあげる
      delete requestOptions.headers['Content-Type'];

      // 設定したデータをPOST
      fetch('http://127.0.0.1:8000/api/v1/object3d/', requestOptions);

    },
  },
};
</script>

<style scoped>
.sendButton {
  padding: 0.2rem;
  margin-top: 1rem;
}
</style>
