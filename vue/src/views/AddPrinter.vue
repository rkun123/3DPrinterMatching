<template>
    <div>
        <form>
            <p>username:</p>
            <input v-model="form_data.name" />
            <p>e-mail:</p>
            <input v-model="form_data.max_width" autocomplete="email" />
            <p>password:</p>
            <input v-model="form_data.max_height" type="password" />
            <p>もう一度パスワードを入力してください</p>
            <input v-model="form_data.max_depth" type="password" />
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
                    max_width: null,
                    max_height: null,
                    max_depth: null,
                    user: null
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
                    headers: { "Content-Type": "application/json", "Authorization": this.$store.getter.getter.getKey },
                    body: payload

                }

                await fetch('http://127.0.0.1:8000/rest-auth/registration/', requestOptions)
                    .then(response => response.json())
                    .then(requestOptions => console.log(requestOptions))




            }
        },


    }
</script>

<style scoped>
</style>
