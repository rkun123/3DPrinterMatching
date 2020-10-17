<template>
    <div>
        <form>
            <p>printername:</p>
            <input v-model="form_data.name" />
            <p>maxwidth:</p>
            <input v-model="form_data.max_width" />
            <p>maxheight:</p>
            <input v-model="form_data.max_height"  />
            <p>maxdepth</p>
            <input v-model="form_data.max_depth" />
        </form>

        <button v-on:click="post">submit</button>
        {{form_data.user}}
    </div>
</template>

<script>
    export default {

        data() {
            return {
                form_data: {
                    name: "",
                    max_width: null,
                    max_height: null,
                    max_depth: null,
                    user: this.$store.state.UserState.pk
                }
            }
        },
        methods: {
            post: async function () {
                // メソッド内の `this` は、 Vue インスタンスを参照します
                alert('Hello ' + '!')

                const payload = JSON.stringify(this.form_data)

                const requestOptions = {
                    method: "POST",
                    headers: { "Content-Type": "application/json", "Authorization": "Token " + this.$store.state.UserKey },
                    body: payload

                }

                await fetch('http://127.0.0.1:8000/api/v1/printer3d/', requestOptions)
                    .then(response => response.json())
                    .then(requestOptions => console.log(requestOptions))




            }
        },


    }
</script>

<style scoped>
</style>
