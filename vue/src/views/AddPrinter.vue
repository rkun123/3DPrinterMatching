<template>
    <div>
        <form>
<<<<<<< HEAD
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
=======
            <p>username:</p>
            <input v-model="form_data.name" />
            <p>e-mail:</p>
            <input v-model="form_data.max_width" autocomplete="email" />
            <p>password:</p>
            <input v-model="form_data.max_height" type="password" />
            <p>‚à‚¤ˆê“xƒpƒXƒ[ƒh‚ğ“ü—Í‚µ‚Ä‚­‚¾‚³‚¢</p>
            <input v-model="form_data.max_depth" type="password" />
        </form>

        <button v-on:click="post">Greet</button>

>>>>>>> fa23ae6... [fix]403è§£æ¶ˆ
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
<<<<<<< HEAD
                    user: this.$store.state.UserState.pk
=======
                    user: null
>>>>>>> fa23ae6... [fix]403è§£æ¶ˆ
                }
            }
        },
        methods: {
            post: async function () {
                // ƒƒ\ƒbƒh“à‚Ì `this` ‚ÍA Vue ƒCƒ“ƒXƒ^ƒ“ƒX‚ğQÆ‚µ‚Ü‚·
                alert('Hello ' + '!')

                const payload = JSON.stringify(this.form_data)

                const requestOptions = {
                    method: "POST",
<<<<<<< HEAD
                    headers: { "Content-Type": "application/json", "Authorization": "Token " + this.$store.state.UserKey },
=======
                    headers: { "Content-Type": "application/json", "Authorization": this.$store.getter.getter.getKey },
>>>>>>> fa23ae6... [fix]403è§£æ¶ˆ
                    body: payload

                }

<<<<<<< HEAD
                await fetch('http://127.0.0.1:8000/api/v1/printer3d/', requestOptions)
=======
                await fetch('http://127.0.0.1:8000/rest-auth/registration/', requestOptions)
>>>>>>> fa23ae6... [fix]403è§£æ¶ˆ
                    .then(response => response.json())
                    .then(requestOptions => console.log(requestOptions))




            }
        },


    }
</script>

<style scoped>
</style>
